from graficas_valores_termicos.graficas_valores_termicos import AdquisionValoresTermicos, GraficaValoresTermicos
from control_temperatura.control_tempertatura import ControlTemperatura
from imagen_termica.imagen_termica import Grafica, ImagenTermica
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.mainwindow import Ui_MainWindow
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
        self.toggleControl.toggled.connect(self.toogle_control)
        self.toogleLazoAbierto.setChecked(True)
        # self.actuador_value_send.clicked.connect(self.enviar_actuador)
        self.send_button.clicked.connect(self.enviar_parametros_control)

    def actualizar_labels_temperatura(self, maxima, minima, promedio):
        self.temperatura_maxima_value.setText(f"{maxima:.2f} °C")
        self.temperatura_minima_value.setText(f"{minima:.2f} °C")
        self.temperatura_promedio_value.setText(f"{promedio:.2f} °C")
        if self.toggleControl.isChecked():
            self.control_temperatura.temperatura_camara = maxima
        self.adquision_valores_termicos.data_maxima_temperatura.append(maxima)
        self.adquision_valores_termicos.data_minima_temperatura.append(minima)
    
    def toogle_control(self):
        if self.toggleControl.isChecked():
            self.toogleLazoAbierto.setChecked(False)
            self.control_temperatura = ControlTemperatura(self.imagen_termica.maxima_temperatura_actual)
            self.control_temperatura.start()
        else:
            self.control_temperatura.terminate()
        
    # def enviar_actuador(self):
    #     if self.toogleLazoAbierto.isChecked():
    #         print(self.actuado_value)
    
    def enviar_parametros_control(self):
        setpoint = float(self.temperatura_maxima_deseada_value)
        self.control_temperatura.modificar_setpoint(setpoint)
    
    def closeEvent(self, event):
        if self.toggleControl.isChecked():
            self.control_temperatura.handle_close()
        event.accept()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())