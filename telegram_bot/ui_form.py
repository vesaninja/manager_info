# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_InfoScreen(object):
    def setupUi(self, InfoScreen):
        if not InfoScreen.objectName():
            InfoScreen.setObjectName(u"InfoScreen")
        InfoScreen.resize(1920, 1080)
        self.Clock = QLabel(InfoScreen)
        self.Clock.setObjectName(u"Clock")
        self.Clock.setGeometry(QRect(1780, 1015, 151, 61))
        font = QFont()
        font.setPointSize(40)
        font.setStrikeOut(False)
        self.Clock.setFont(font)
        self.Background = QLabel(InfoScreen)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(0, 0, 1920, 1080))
        self.Background.setAutoFillBackground(False)
        self.Background.raise_()
        self.Clock.raise_()

        self.retranslateUi(InfoScreen)

        QMetaObject.connectSlotsByName(InfoScreen)
    # setupUi

    def retranslateUi(self, InfoScreen):
        InfoScreen.setWindowTitle(QCoreApplication.translate("InfoScreen", u"InfoScreen", None))
        self.Clock.setText(QCoreApplication.translate("InfoScreen", u"Kello", None))
        self.Background.setText("")
    # retranslateUi
