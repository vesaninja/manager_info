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
from PyQt5.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget, QListWidget, QProgressBar)

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
        self.SpotifyCode.setGeometry(QRect(1600, 10, 300, 100))
        spotify_font = QFont()
        spotify_font.setPointSize(50)
        spotify_font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 15)
        self.SpotifyCode.setFont(spotify_font)

        self.Timetable1 = QListWidget(InfoScreen)
        self.Timetable1.setObjectName(u"Timetable1")
        self.Timetable1.setGeometry(QRect(1450, 280, 500, 500))
        self.Timetable1.setAutoFillBackground(False)
        font = QFont()
        font.setPointSize(30)
        self.Timetable1.setFont(font)

        self.Timetable2 = QListWidget(InfoScreen)
        self.Timetable2.setObjectName(u"Timetable2")
        self.Timetable2.setGeometry(QRect(1450, 580, 500, 500))
        self.Timetable2.setAutoFillBackground(False)
        font = QFont()
        font.setPointSize(30)
        self.Timetable2.setFont(font)

        self.Restaurant = QLabel(InfoScreen)
        self.Restaurant.setObjectName(u"Restaurant")
        self.Restaurant.setGeometry(QRect(290, 125, 300, 200))
        font = QFont()
        font.setPointSize(45)
        self.Restaurant.setFont(font)

        self.FoodMenu = QLabel(InfoScreen)
        self.FoodMenu.setObjectName(u"FoodMenu")
        self.FoodMenu.setGeometry(QRect(90, 300, 500, 700))
        font = QFont()
        font.setPointSize(15)
        self.FoodMenu.setFont(font)

        self.NowPlaying = QLabel(InfoScreen)
        self.NowPlaying.setObjectName(u"NowPlaying")
        self.NowPlaying.setGeometry(QRect(80, 930, 1000, 50))
        font = QFont()
        font.setPointSize(25)
        # font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 15)
        self.NowPlaying.setFont(font)

        self.ProgressBar = QProgressBar(InfoScreen)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setGeometry(QRect(0, 920, 1088, 50))

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

