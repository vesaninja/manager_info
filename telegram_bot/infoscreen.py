# This Python file uses the following encoding: utf-8
import sys
import os
from kiltabotti import BotController

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InfoScreen()
        self.ui.setupUi(self)
        self.showFullScreen()

        # Set background image
        # bg = QLabel(self)
        bg = self.findChild(QLabel, "Background")
        bg.setPixmap(QPixmap("media/infoscreen.png"))
        bg.show()

        self.clock = self.setup_clock()

    def setup_clock(self):
        """ Setup a digital clock. """
        clock = self.findChild(QLabel, "Clock")
        clock.setStyleSheet("color: white")
        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(1000)
        return clock

    def show_time(self):
        """ Show current time in digital clock format """
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm')
        self.clock.setText(label_time)

if __name__ == "__main__":
    BotController(True)
    app = QApplication(sys.argv)
    info_screen = InfoScreen()
    info_screen.show()
    # info_screen.Clock
    sys.exit(app.exec())
