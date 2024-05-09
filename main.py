from PySide6.QtWidgets import QApplication, QMainWindow
from ui.mainwindow import Ui_MainWindow
from imagen_termica.imagen_termica import Grafica, ImagenTermica
from graficas_valores_termicos.graficas_valores_termicos import AdquisionValoresTermicos, GraficaValoresTermicos
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.grafica = Grafica()
        self.imagen_termica = ImagenTermica(self.grafica)
        self.imagen_termica.start()
        self.grafica_valores_termicos = GraficaValoresTermicos()
        self.adquision_valores_termicos = AdquisionValoresTermicos(self.grafica_valores_termicos)
        self.adquision_valores_termicos.start()
        self.imagen_termica.actualizar_labels_signal.connect(self.actualizar_labels_temperatura)
        self.imagen_termica_layout.addWidget(self.grafica)
        self.maxima_temperatura_layout.addWidget(self.grafica_valores_termicos)

    def actualizar_labels_temperatura(self, maxima, minima, promedio):
        self.temperatura_maxima_value.setText(f"{maxima:.2f} °C")
        self.temperatura_minima_value.setText(f"{minima:.2f} °C")
        self.temperatura_promedio_value.setText(f"{promedio:.2f} °C")
        self.adquision_valores_termicos.data_maxima_temperatura.append(maxima)
        self.adquision_valores_termicos.data_minima_temperatura.append(minima)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())