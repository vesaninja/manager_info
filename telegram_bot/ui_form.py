# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_InfoScreen(object):
    def setupUi(self, InfoScreen):
        if not InfoScreen.objectName():
            InfoScreen.setObjectName(u"InfoScreen")
        InfoScreen.resize(1830, 985)

        self.Background = QLabel(InfoScreen)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(0, 0, 1830, 985))
        self.Background.setAutoFillBackground(False)

        self.Clock = QLabel(InfoScreen)
        self.Clock.setObjectName(u"Clock")
        self.Clock.setGeometry(QRect(1680, 895, 200, 120))
        font = QFont()
        font.setPointSize(35)
        font.setStrikeOut(False)
        self.Clock.setFont(font)

        self.SpotifyCode = QLabel(InfoScreen)
        self.SpotifyCode.setObjectName(u"SpotifyCode")
        self.SpotifyCode.setGeometry(QRect(1700, 30, 160, 90))
        self.SpotifyCode.setAutoFillBackground(False)
        self.SpotifyCode.setFont(font)

        self.Timetable = QLabel(InfoScreen)
        self.Timetable.setObjectName(u"Timetable")
        self.Timetable.setGeometry(QRect(1300, 300, 500, 500))
        self.Timetable.setAutoFillBackground(False)
        self.Timetable.setFont(font)

        # self.Background.raise_()
        self.Clock.raise_()
        self.SpotifyCode.raise_()

        self.retranslateUi(InfoScreen)

        QMetaObject.connectSlotsByName(InfoScreen)
    # setupUi

    def retranslateUi(self, InfoScreen):
        InfoScreen.setWindowTitle(QCoreApplication.translate("InfoScreen", u"InfoScreen", None))
        self.Clock.setText(QCoreApplication.translate("InfoScreen", u"Kello", None))
        self.Background.setText("")
    # retranslateUi

