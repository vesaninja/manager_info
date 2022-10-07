# This Python file uses the following encoding: utf-8
import sys
import os
from kiltabotti import BotController
from nysse_api import NysseApi

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import QTimer, QTime

# current_dir = os.path.dirname(os.path.abspath(__file__))
# Form, Base = loadUiType(os.path.join(current_dir, "form.ui"))

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_InfoScreen


class InfoScreen(QWidget):
    def __init__(self, bot_controller, nysse_api, parent=None):
        super().__init__(parent)
        self.ui = Ui_InfoScreen()
        self.ui.setupUi(self)
        self.showFullScreen()
        self.bot_controller = bot_controller
        self.nysse_api = nysse_api

        # Set background image
        bg = self.findChild(QLabel, "Background")
        bg.setPixmap(QPixmap("media/infoscreen.png"))
        bg.show()

        self.clock = self.setup_clock()
        self.spotify_code_label = self.setup_spotify_code()
        self.timetable = self.setup_timetable()
        self.setup_timers()

    def setup_timers(self):
        """ Set up different timers that update infoscreen elements. """
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.timeout.connect(self.update_spotify_code)
        timer.timeout.connect(self.update_timetable)
        timer.start(5000)

        spotify_timer = QTimer(self)
        spotify_timer.timeout.connect(self.bot_controller.spotify_api.update_auth_token)
        spotify_timer.start(10800000)

    def setup_clock(self):
        """ Setup a digital clock. """
        clock = self.findChild(QLabel, "Clock")
        clock.setStyleSheet("color: white")
        clock.setGraphicsEffect(QGraphicsDropShadowEffect())
        return clock

    def update_time(self):
        """ Update the digital clock time """
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm')
        self.clock.setText(label_time)

    def setup_spotify_code(self):
        """ Set up a label that shows the current spotify code. """
        spotify_code = self.findChild(QLabel, "SpotifyCode")
        spotify_code.setStyleSheet("color: white")
        spotify_code.setText("1234")
        return spotify_code

    def update_spotify_code(self):
        """ Show update the spotify auth token """
        # self.bot_controller.spotify_api.update_auth_token()
        token = self.bot_controller.spotify_api.get_token()
        self.spotify_code_label.setText(token)

    def setup_timetable(self):
        """ Set up a table to show arriving buses. """
        timetable = self.findChild(QLabel, "Timetable")
        timetable.setStyleSheet("color: white")
        timetable.setText("Bussiaikataulut")
        return timetable

    def update_timetable(self):
        """ Update the bus information. """
        buses = self.nysse_api.get_stop_info()
        self.timetable.setText(str(buses))


if __name__ == "__main__":
    bot_controller = BotController(True)
    nysse_api = NysseApi()
    app = QApplication(sys.argv)
    info_screen = InfoScreen(bot_controller, nysse_api)
    info_screen.show()
    # info_screen.Clock
    sys.exit(app.exec())
