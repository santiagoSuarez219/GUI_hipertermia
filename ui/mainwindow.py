# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowQHRwTI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1127, 654)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(800, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.imagen_termica_layout = QVBoxLayout()
        self.imagen_termica_layout.setObjectName(u"imagen_termica_layout")

        self.verticalLayout_4.addLayout(self.imagen_termica_layout)


        self.horizontalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_7 = QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.maxima_temperatura_layout = QVBoxLayout()
        self.maxima_temperatura_layout.setObjectName(u"maxima_temperatura_layout")

        self.verticalLayout_7.addLayout(self.maxima_temperatura_layout)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.horizontalLayout_2.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.widget)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 16, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(QFont.Bold)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.temperatura_maxima = QLabel(self.centralwidget)
        self.temperatura_maxima.setObjectName(u"temperatura_maxima")
        font1 = QFont()
        font1.setPointSize(10)
        self.temperatura_maxima.setFont(font1)

        self.verticalLayout.addWidget(self.temperatura_maxima)

        self.temperatura_maxima_value = QLabel(self.centralwidget)
        self.temperatura_maxima_value.setObjectName(u"temperatura_maxima_value")
        self.temperatura_maxima_value.setFont(font1)

        self.verticalLayout.addWidget(self.temperatura_maxima_value)

        self.temperatura_minima = QLabel(self.centralwidget)
        self.temperatura_minima.setObjectName(u"temperatura_minima")
        self.temperatura_minima.setFont(font1)

        self.verticalLayout.addWidget(self.temperatura_minima)

        self.temperatura_minima_value = QLabel(self.centralwidget)
        self.temperatura_minima_value.setObjectName(u"temperatura_minima_value")
        self.temperatura_minima_value.setFont(font1)

        self.verticalLayout.addWidget(self.temperatura_minima_value)

        self.temperatura_promedio = QLabel(self.centralwidget)
        self.temperatura_promedio.setObjectName(u"temperatura_promedio")
        self.temperatura_promedio.setFont(font1)

        self.verticalLayout.addWidget(self.temperatura_promedio)

        self.temperatura_promedio_value = QLabel(self.centralwidget)
        self.temperatura_promedio_value.setObjectName(u"temperatura_promedio_value")
        self.temperatura_promedio_value.setFont(font1)

        self.verticalLayout.addWidget(self.temperatura_promedio_value)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")

        self.verticalLayout.addWidget(self.spinBox)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout.addWidget(self.label_4)

        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.verticalLayout.addWidget(self.spinBox_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.horizontalLayout_3.addWidget(self.doubleSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout.addWidget(self.radioButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1127, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Aplicativo Hipertermia", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Parametros termicos", None))
        self.temperatura_maxima.setText(QCoreApplication.translate("MainWindow", u"Temperatura maxima:", None))
        self.temperatura_maxima_value.setText(QCoreApplication.translate("MainWindow", u"43 \u00b0C", None))
        self.temperatura_minima.setText(QCoreApplication.translate("MainWindow", u"Temperatura minima:", None))
        self.temperatura_minima_value.setText(QCoreApplication.translate("MainWindow", u"30 \u00b0C", None))
        self.temperatura_promedio.setText(QCoreApplication.translate("MainWindow", u"Temperatura promedio", None))
        self.temperatura_promedio_value.setText(QCoreApplication.translate("MainWindow", u"35 \u00b0C", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Control de temperatura", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Temperatura maxima deseada", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Temperatura minima deseada", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Tomar datos CSV", None))
    # retranslateUi

