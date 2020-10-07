from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar

# Tworzenie klasy głównego okna aplikacji dziedziczącej po QMainWindow
class Window(QMainWindow):
    #Dodanie konstruktora przyjmującego okno nadrzędne
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt5 Lab')

# Uruchomienie okna
app = QApplication([])
win = Window()
win.show()
app.exec_()