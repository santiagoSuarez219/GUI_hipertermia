import time
from PySide6.QtCore import QThread, Signal
from comunicacion_serial.comunicion_serial import comunicacion_serial
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.widgets import RectangleSelector
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
        self.grafica.actualizar_graficas(self.data_imagen_termica)
        if self.data_imagen_termica is not None:
            maxima = np.max(self.data_imagen_termica)
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
        self.RS = RectangleSelector(self.g1, self.line_select_callback, useblit=True,
                                    button=[1], minspanx=5, minspany=5, spancoords='pixels',
                                    interactive=True)

    
    def line_select_callback(self, eclick, erelease):
        """
        Callback for line selection.

        *eclick* and *erelease* are the press and release events.
        """
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        self.area_seleccionada = self.data_imagen_termica[int(y1):int(y2), int(x1):int(x2)]
        if self.area_seleccionada is not None:
            print(f"Temperatura promedio en el área seleccionada: {np.mean(self.area_seleccionada)}")

    def actualizar_graficas(self, data_g1):
        self.data_imagen_termica = data_g1
        self.g1.clear()
        if data_g1 is not None:
            self.g1.imshow(data_g1, cmap='jet')
        self.draw()