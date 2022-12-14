# This Python file uses the following encoding: utf-8
import logging
import sys
import os
from kiltabotti import BotController
from nysse_api import NysseApi
from restaurant_api import get_newton_menu, get_reaktori_menu, get_hertsi_menu

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGraphicsDropShadowEffect, QListWidget, QFrame, QProgressBar
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import QTimer, QTime, QPropertyAnimation, Qt

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
        self.current_restaurant = "NEWTON"

        # Set background image
        bg = self.findChild(QLabel, "Background")
        bg.setPixmap(QPixmap("media/infoscreen.png"))
        bg.show()

        self.clock = self.setup_clock()
        self.spotify_code_label = self.setup_spotify_code()
        self.timetable1 = self.setup_timetable("Timetable1")
        self.timetable2 = self.setup_timetable("Timetable2")
        self.now_playing = self.setup_now_playing()
        self.progressbar = self.setup_progress_bar()
        self.food_menu = self.setup_foodmenu()
        self.restaurant_label = self.setup_restaurant_label()
        self.setup_timers()

    def setup_timers(self):
        """ Set up different timers that update infoscreen elements. """
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.timeout.connect(self.update_spotify_code)
        timer.timeout.connect(self.update_timetable)
        timer.timeout.connect(self.update_now_playing)
        timer.timeout.connect(self.update_progress_bar)
        timer.start(5000)

        restaurant_timer = QTimer(self)
        restaurant_timer.timeout.connect(self.update_foodmenu)
        restaurant_timer.start(15000)

        spotify_timer = QTimer(self)
        spotify_timer.timeout.connect(self.bot_controller.spotify_controller.update_auth_token)
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
        token = self.bot_controller.spotify_controller.get_token()
        self.spotify_code_label.setText(token)

    def setup_now_playing(self):
        """ Set up a label that shows currently playing spotify song. """
        now_playing = self.findChild(QLabel, "NowPlaying")
        now_playing.setStyleSheet("color: white")
        now_playing.setText("Infonäyttöön liittyviä kehitysehdotuksia voi lähettää Vesalle")
        return now_playing

    def update_now_playing(self):
        """ Update currently playing spotify song. """
        try:
            song_data = self.bot_controller.spotify_controller.spotify_api.currently_playing()
            current_artist = song_data["item"]["artists"][0]["name"]
            current_song = song_data["item"]["name"]
            song_text = "{} - {}".format(current_artist, current_song)
        except:
            song_text = "Infonäyttöön liittyviä kehitysehdotuksia voi lähettää Vesalle"
        self.now_playing.setText(song_text)

    def setup_timetable(self, timetable_name):
        """ Set up a table to show arriving buses. """
        timetable = self.findChild(QListWidget, timetable_name)
        timetable.setStyleSheet("color: white")
        timetable.addItem("Bussiaikataulut")
        timetable.setStyleSheet("background-color: transparent; color: white")
        timetable.setFrameShape(QFrame.NoFrame)
        timetable.setSpacing(-2)
        return timetable

    def update_timetable(self):
        """ Update the bus information. """
        try:
            buses = self.nysse_api.get_stop_info("3735")
        except:
            buses = None
        self.timetable1.clear()
        if buses:
            for bus in buses[0:4]:
                string = "{} - {}".format(bus[0], bus[1])
                self.timetable1.addItem(string)
        try:
            trams = self.nysse_api.get_stop_info("0833")
        except:
            trams = None
        self.timetable2.clear()
        if trams:
            for tram in trams[0:2]:
                string = "{} - {}".format(tram[0], tram[1])
                self.timetable2.addItem(string)

    def setup_progress_bar(self):
        """ Set up a spotify song progress bar """
        progressbar = self.findChild(QProgressBar, "ProgressBar")
        progressbar.setValue(0)
        progressbar.setTextVisible(False)
        self.setStyleSheet("QProgressBar { min-height: 5px; max-height: 5px; border-radius: 6px; border-radius: 6px;"
                           " background-color: transparent}"
                           "QProgressBar::chunk { background-color: white; width: 1px}")
        return progressbar

    def update_progress_bar(self):
        """ Update the now playing progress """
        try:
            data = self.bot_controller.spotify_controller.spotify_api.currently_playing()
            new_value = int(int(data["progress_ms"]) / int(data["item"]["duration_ms"]) * 100)
            if new_value < self.progressbar.value():
                new_value = 0
        except:
            new_value = 0
        animation = QPropertyAnimation(self.progressbar, b"value", self)
        animation.setDuration(3000)
        animation.setStartValue(self.progressbar.value())
        animation.setEndValue(new_value)
        animation.start()

    def setup_foodmenu(self):
        """ Set up a table to show restauran menus. """
        food_menu = self.findChild(QLabel, "FoodMenu")
        food_menu.setStyleSheet("color: white")
        food_menu.setText("Suljettu")
        food_menu.setWordWrap(True)
        food_menu.setAlignment(Qt.AlignTop)
        return food_menu

    def setup_restaurant_label(self):
        """ Set up a table to show restaurant name. """
        restaurant_label = self.findChild(QLabel, "Restaurant")
        restaurant_label.setStyleSheet("color: white")
        restaurant_label.setText("Newton")
        restaurant_label.setWordWrap(True)
        restaurant_label.setAlignment(Qt.AlignTop)
        restaurant_label.setGraphicsEffect(QGraphicsDropShadowEffect())
        return restaurant_label

    def update_foodmenu(self):
        """ Update the restauran menu information. """
        try:
            if self.current_restaurant == "HERTSI":
                menu = get_newton_menu()
                self.current_restaurant = "NEWTON"
            elif self.current_restaurant == "NEWTON":
                menu = get_reaktori_menu()
                self.current_restaurant = "REAKTORI"
            elif self.current_restaurant == "REAKTORI":
                menu = get_hertsi_menu()
                self.current_restaurant = "HERTSI"
            formated_menu = ""
            for line in menu.splitlines():
                formated_menu += "{}<br>".format(line)
        except:
            formated_menu = "Oops minulla on ongelma!"
        self.food_menu.setText(formated_menu)
        self.restaurant_label.setText(self.current_restaurant)


if __name__ == "__main__":
    bot_controller = BotController(True)
    nysse_api = NysseApi()
    app = QApplication(sys.argv)
    info_screen = InfoScreen(bot_controller, nysse_api)
    info_screen.show()
    sys.exit(app.exec())
