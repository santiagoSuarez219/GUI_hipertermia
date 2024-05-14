from PySide6.QtCore import QThread
import pandas as pd
import numpy as np
import serial
import time

class ControlTemperatura(QThread):
    def __init__(self, run_time=15.0, setpoint = 50.0, temperatura_camara = 23.0):
        super(ControlTemperatura, self).__init__()
        self.puerto_serie = serial.Serial('COM8', 9600)
        self.temperatura_camara = temperatura_camara
        self.loops = int(60.0*run_time)
        self.setpoint = np.ones(self.loops) * setpoint
        self.tm = np.zeros(self.loops)
        self.T1 = np.ones(self.loops) * temperatura_camara
        self.error_sp = np.zeros(self.loops)
        self.Q1 = np.ones(self.loops) * 0.0
        self.data_csv = {
            'tm':[],
            #'T1': [],
            #'P': [],
            #'I': [],
            #'D': [],
            #'setpoint': [],
            'temperatura camara': [],
            #'ITAE': [],
            #'error_sp': [],
            #'Q1': []
        }
    
    def run(self):
        ITAE = 0.0
        start_time = time.time()
        prev_time = start_time
        dt_error = 0.0
        ierr = 0.0
        try:
            for i in range(1,self.loops):
                sleep_max = 1.0
                sleep = sleep_max - (time.time() - prev_time) - dt_error
                if sleep>=1e-4:
                    time.sleep(sleep-1e-4)
                else:
                    print('exceeded max cycle time by ' + str(abs(sleep)) + ' sec')
                    time.sleep(1e-4) 

                t = time.time()
                dt = t - prev_time 
                if (sleep>=1e-4):
                    dt_error = dt-1.0+0.009
                else:
                    dt_error = 0.0
                prev_time = t
                self.tm[i] = t - start_time
                self.T1[i] = self.temperatura_camara

                [self.Q1[i],P,ierr,D] = self.pid(self.setpoint[i],self.T1[i],self.T1[i-1],ierr,dt)
                ITAE = ITAE + (abs(self.setpoint-self.T1[i]))*(i+1)
                self.data_csv['tm'].append(self.tm[i])
                # self.data_csv['T1'].append(self.T1[i])
                # self.data_csv['P'].append(P)
                # self.data_csv['I'].append(ierr)
                # self.data_csv['D'].append(D)
                # self.data_csv['setpoint'].append(self.setpoint[i])
                if self.temperatura_camara is not None:
                    self.data_csv['temperatura camara'].append(self.temperatura_camara)
                else:
                    self.data_csv['temperatura camara'].append(0.0)
                # self.data_csv['ITAE'].append(ITAE[i])
                # self.data_csv['error_sp'].append((self.setpoint-self.T1[i])[i])
                # self.data_csv['Q1'].append(self.Q1[i])
                self.enviar_actuador(30*255/100)
                time.sleep(0.1)
        except:            # Disconnect from Arduino
            self.puerto_serie.write(str(0).encode())
            print('Error: Shutting down')
            self.puerto_serie.close()

        return ITAE
    
    def handle_close(self):
        df = pd.DataFrame(self.data_csv)
        df.to_csv('data_lazo_abierto.csv')
        self.puerto_serie.write(str(0).encode())
        self.puerto_serie.close()

    
    def modificar_setpoint(self, setpoint):
        self.setpoint = np.ones(self.loops) * setpoint

    def pid(self,sp,pv,pv_last,ierr,dt):
        Kp = 0.5 
        Kc   = 10.0 # K/%Heater
        tauI = 50.0 # sec
        tauD = 1.0  # sec
        # Parameters in terms of PID coefficients
        KP = Kc
        KI = Kc/tauI
        KD = Kc*tauD
        # ubias for controller (initial heater)
        op0 = 0 
        # upper and lower bounds on heater level
        ophi = 100
        oplo = 0
        # calculate the error
        error = sp-pv
        # calculate the integral error
        ierr = ierr + KI * error * dt
        # calculate the measurement derivative
        dpv = (pv - pv_last) / dt
        # calculate the PID output
        P = KP * error
        I = ierr
        D = -KD * dpv
        op = op0 + P + I + D
        # implement anti-reset windup
        if op < oplo or op > ophi:
            I = I - KI * error * dt
            # clip output
            op = max(oplo,min(ophi,op))
        # return the controller output and PID terms
        return [op,P,I,D]
    
    def enviar_actuador(self, value):
        self.puerto_serie.write(str(value).encode())