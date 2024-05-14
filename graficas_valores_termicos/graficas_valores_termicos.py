import time
from PySide6.QtCore import QThread, Signal
from comunicacion_serial.comunicion_serial import comunicacion_serial
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
import numpy as np

class AdquisionValoresTermicos(QThread):
    actualizar_valores_termicos_signal = Signal(float, float)
    def __init__(self, grafica):
        super(AdquisionValoresTermicos, self).__init__() 
        self.grafica = grafica
        self.data_maxima_temperatura = []
        self.data_minima_temperatura = []
    
    def run(self):
        while True:
            self.actualizar_datos()
            time.sleep(.050)

    def actualizar_datos(self):
        if len(self.data_maxima_temperatura) == 200:
            self.data_maxima_temperatura.pop(0)
        
        if len(self.data_minima_temperatura) == 200:
            self.data_minima_temperatura.pop(0)

        self.actualizar_graficas(self.data_maxima_temperatura, self.data_minima_temperatura)

    def actualizar_graficas(self, data1, data2):
        self.grafica.g.clear()
        self.grafica.g2.clear()
        self.grafica.g.plot(data1, '-o')
        self.grafica.g2.plot(data2, '-o')
        self.grafica.g.set_title("Temperatura maxima")
        self.grafica.g2.set_title("Temperatura minima")
        self.grafica.g.set_xlabel("Muestra")
        self.grafica.g2.set_xlabel("Muestra")
        self.grafica.g.set_ylabel("Temperatura (°C)")
        self.grafica.g2.set_ylabel("Temperatura (°C)")
        self.grafica.draw()


class GraficaValoresTermicos(FigureCanvasQTAgg):
    def __init__(self):
        figura = Figure(layout='tight') 
        super(GraficaValoresTermicos, self).__init__(figura)
        self.g = figura.add_subplot(211)
        self.g.grid()
        self.g2 = figura.add_subplot(212)
        self.g2.grid()
    