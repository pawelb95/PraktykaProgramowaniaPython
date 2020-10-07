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
        
        self.createMenu()
        
    
    # Stworzenie funkcji dodającej pasek menu do okna
    def createMenu(self):
        # Stworzenie paska menu
        self.menu = self.menuBar()
        # Dodanie do paska listy rozwijalnej o nazwie File
        self.fileMenu = self.menu.addMenu("File")
        # Dodanie do menu File pozycji zamykającej aplikacje
        self.fileMenu.addAction('Exit', self.close)


# Uruchomienie okna
app = QApplication([])
win = Window()
win.show()
app.exec_()

