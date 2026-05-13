# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class uiRoot(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")
        root.resize(500, 300)
        self.centralwidget = QWidget(root)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.grpTemp = QGroupBox(self.centralwidget)
        self.grpTemp.setObjectName(u"grpTemp")
        self.gridLayout = QGridLayout(self.grpTemp)
        self.gridLayout.setObjectName(u"gridLayout")
        self.entFahrenheit = QLineEdit(self.grpTemp)
        self.entFahrenheit.setObjectName(u"entFahrenheit")

        self.gridLayout.addWidget(self.entFahrenheit, 0, 1, 1, 1)

        self.lblEnt = QLabel(self.grpTemp)
        self.lblEnt.setObjectName(u"lblEnt")

        self.gridLayout.addWidget(self.lblEnt, 0, 0, 1, 1)

        self.lblResult = QLabel(self.grpTemp)
        self.lblResult.setObjectName(u"lblResult")
        self.lblResult.setMinimumSize(QSize(50, 20))

        self.gridLayout.addWidget(self.lblResult, 1, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.grpTemp)

        self.fraButtons = QFrame(self.centralwidget)
        self.fraButtons.setObjectName(u"fraButtons")
        self.fraButtons.setAutoFillBackground(False)
        self.fraButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.fraButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.fraButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnConvert = QPushButton(self.fraButtons)
        self.btnConvert.setObjectName(u"btnConvert")
        self.btnConvert.setMinimumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.btnConvert)

        self.btnReset = QPushButton(self.fraButtons)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setMinimumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.btnReset)

        self.btnExit = QPushButton(self.fraButtons)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setMinimumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.btnExit)


        self.verticalLayout.addWidget(self.fraButtons)

        root.setCentralWidget(self.centralwidget)

        self.retranslateUi(root)

        QMetaObject.connectSlotsByName(root)
    # setupUi

    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", u"Converter", None))
        self.grpTemp.setTitle(QCoreApplication.translate("root", u"Temperature Data", None))
        self.lblEnt.setText(QCoreApplication.translate("root", u"Enter Temp (F):", None))
        self.lblResult.setText("")
        self.btnConvert.setText(QCoreApplication.translate("root", u"Convert", None))
        self.btnReset.setText(QCoreApplication.translate("root", u"Clear", None))
        self.btnExit.setText(QCoreApplication.translate("root", u"Exit", None))
    # retranslateUi


