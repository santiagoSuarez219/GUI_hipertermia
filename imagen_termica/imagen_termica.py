import time
from PySide6.QtCore import QThread, Signal
from comunicacion_serial.comunicion_serial import comunicacion_serial
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
import numpy as np
import matplotlib.pyplot as plt

class ImagenTermica(QThread):
    actualizar_labels_signal = Signal(float, float, float)
    def __init__(self, grafica):
        super(ImagenTermica, self).__init__() 
        self.grafica = grafica
        self.comunicacion_serial = comunicacion_serial(vid=0x1A86, pid=0x7523, baudrate=115200)
        self.comunicacion_serial.conectar()
        self.data_imagen_termica = self.comunicacion_serial.leer()

    def run(self):
        while True:
            self.actualizar_datos()
            time.sleep(.050)

    def actualizar_datos(self):
        self.data_imagen_termica = self.comunicacion_serial.leer()
        maxima = np.max(self.data_imagen_termica)
        self.grafica.actualizar_graficas(self.data_imagen_termica)
        minima = np.min(self.data_imagen_termica)
        promedio = np.mean(self.data_imagen_termica)
        self.actualizar_labels_signal.emit(maxima, minima, promedio)

class Grafica(FigureCanvasQTAgg):
    # actualizar_temperatura_signal = pyqtSignal(float)
    def __init__(self):
        # Crear la figura y asignarle el mismo tamaño que el widget y color de fondo oscuro
        figura = Figure(layout='tight') 
        super(Grafica, self).__init__(figura)
        self.g1 = figura.add_subplot(111)
        self.data_imagen_termica = np.zeros((24, 32))
        self.area_seleccionada = None
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.selector_rectangular = None
        self.isSelecting = False

        self.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.figure.canvas.mpl_connect('button_release_event', self.on_release)
        # self.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)
    
    def on_press(self, event):
        self.isSelecting = True
        self.x0 = event.xdata
        self.y0 = event.ydata
        self.selector_rectangular = None
    
    def on_release(self, event):
        self.x1 = event.xdata
        self.y1 = event.ydata
        self.isSelecting = False
        
    # def on_motion(self, event):
    #     if self.isSelecting:
    #         self.x1 = event.xdata
    #         self.y1 = event.ydata
    #         if self.selector_rectangular:
    #             self.selector_rectangular.remove()
    #         self.selector_rectangular = Rectangle((self.x0, self.y0), self.x1 - self.x0, self.y1 - self.y0, edgecolor='black', facecolor='none')
    #         self.g1.add_patch(self.selector_rectangular)
    #         self.draw()

    def actualizar_graficas(self, data_g1):
        self.data_imagen_termica = data_g1
        self.g1.clear()
        if self.x0 != 0 and self.y0 != 0 and self.x1 != 0 and self.y1 != 0 and not self.isSelecting:
            x_min, x_max = sorted([int(round(self.x0)), int(round(self.x1))])
            y_min, y_max = sorted([int(round(self.y0)), int(round(self.y1))])   
            self.area_seleccionada = self.data_imagen_termica[int(y_min):int(y_max), int(x_min):int(x_max)]
            self.selector_rectangular = Rectangle((x_min, y_min), x_max - x_min, y_max - y_min, edgecolor='red', facecolor='none')
            self.g1.add_patch(self.selector_rectangular)
            print(f"Temperatura promedio en el area seleccionada: {np.mean(self.area_seleccionada)}")
        self.g1.imshow(data_g1, cmap='jet')
        self.draw()