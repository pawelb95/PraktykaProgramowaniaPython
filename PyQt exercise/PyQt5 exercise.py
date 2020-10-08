from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QWidget, QPushButton
from PyQt5.QtWidgets import QFileDialog, QLabel, QGridLayout, QLineEdit, QSpinBox, QPlainTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt5 exercise')
        self.setGeometry(300, 300, 800, 600)

        self.create_menu()
        self.create_tabs()
        self.label = QLabel(self.tab_1)

    def create_menu(self):
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        self.task1_menu = self.menu.addMenu("Task 1")
        self.task2_menu = self.menu.addMenu("Task 2")
        self.task3_menu = self.menu.addMenu("Task 3")
        self.file_menu.addAction('Exit', self.close)
        self.task1_menu.addAction('Open  (Ctrl+G)', self.task1_open)
        self.task3_menu.addAction('Close  (Ctrl+Q)', self.task3_clear)
        self.task2_menu.addAction('Clear  (Ctrl+W)', self.task2_clear)
        self.task2_filename = None
        self.task2_menu.addAction('Open  (Ctrl+O)', self.task2_open)
        self.task2_menu.addAction('Save  (Ctrl+S)', self.task2_save)
        self.task2_menu.addAction('SaveAs  (Ctrl+K)', self.task2_saveas)

    def create_tabs(self):
        self.tabs = QTabWidget()

        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tab_3 = QWidget()

        self.textbox = QPlainTextEdit(self.tab_2)
        self.textbox.setGeometry(10, 10, 770, 450)
        save_button = QPushButton(self.tab_2)
        save_button.setGeometry(10, 470, 375, 50)
        save_button.setText("Zapisz")
        save_button.clicked.connect(self.task2_save)
        clear_button = QPushButton(self.tab_2)
        clear_button.setGeometry(395, 470, 375, 50)
        clear_button.setText("Wyczyść")
        clear_button.clicked.connect(self.task2_clear)

        layout = QGridLayout()

        label1 = QLabel("Pole A")
        label2 = QLabel("Pole B")
        label3 = QLabel("Pole C")
        label4 = QLabel("Pole A+B+C")
        self.line_edit1 = QLineEdit(self)
        self.line_edit2 = QLineEdit()
        self.spin_box3 = QSpinBox()
        self.line_edit4 = QLineEdit()
        self.line_edit1.textChanged.connect(self.task3_field_changed)
        self.line_edit2.textChanged.connect(self.task3_field_changed)
        self.spin_box3.textChanged.connect(self.task3_field_changed)

        layout.addWidget(label1, 0, 0)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.line_edit1, 0, 1)
        layout.addWidget(self.line_edit2, 1, 1)
        layout.addWidget(self.spin_box3, 2, 1)
        layout.addWidget(self.line_edit4, 3, 1)

        self.tab_3.setLayout(layout)

        self.tabs.addTab(self.tab_1, "Task 1")
        self.tabs.addTab(self.tab_2, "Task 2")
        self.tabs.addTab(self.tab_3, "Task 3")

        self.setCentralWidget(self.tabs)

    def keyPressEvent(self, event):
        k = event.key()
        m = int(event.modifiers())
        if k == Qt.Key_Escape:
            self.close()
        elif QKeySequence(m + k) == QKeySequence('Ctrl+G'):
            self.task1_open()
        elif QKeySequence(m + k) == QKeySequence('Ctrl+Q'):
            self.task3_clear()
        elif QKeySequence(m + k) == QKeySequence('Ctrl+W'):
            self.task2_clear()
        elif QKeySequence(m + k) == QKeySequence('Ctrl+O'):
            self.task2_open()
        elif QKeySequence(m + k) == QKeySequence('Ctrl+S'):
            self.task2_save()
        elif QKeySequence(m + k) == QKeySequence('Ctrl+K'):
            self.task2_saveas()

    def task1_open(self):
        file_name, selected_filter = QFileDialog.getOpenFileName(self.tab_1,
                                                                 "Wybierz plik obrazu",
                                                                 "Początkowa nazwa pliku",
                                                                 "PNG (*.png)")
        if file_name:
            print(file_name)
            self.tabs.setCurrentWidget(self.tab_1)
            self.tab_1.hide()
            self.label.clear()
            self.label = QLabel(self.tab_1)
            self.pixmap = QPixmap(file_name)
            self.label.setPixmap(self.pixmap)
            self.tab_1.show()

    def task2_clear(self):
        self.textbox.clear()
        self.task2_filename = None

    def task2_open(self):
        self.task2_filename, selectedfilter = QFileDialog.getOpenFileName(self.tab_2,
                                                                          "Wybierz plik tekstowy",
                                                                          "",
                                                                          "TXT (*.txt)")
        if self.task2_filename:
            file_text = open(self.task2_filename).read()
            self.textbox.clear()
            self.textbox.setPlainText(file_text)
            self.tabs.setCurrentWidget(self.tab_2)

    def task2_save(self):
        if self.task2_filename:
            file_text = open(self.task2_filename, "w")
            file_text.write(self.textbox.toPlainText())
        else:
            self.task2_saveas()

    def task2_saveas(self):
        self.task2_filename, selectedfilter = QFileDialog.getSaveFileName(self.tab_2,
                                                                          "Wybierz plik tekstowy",
                                                                          "",
                                                                          "TXT (*.txt)")
        if self.task2_filename:
            file_text = open(self.task2_filename, "w")
            file_text.write(self.textbox.toPlainText())

    def task3_clear(self):
        self.line_edit1.clear()
        self.line_edit2.clear()
        self.spin_box3.setValue(0)

    def task3_field_changed(self):
        self.line_edit4.clear()
        self.line_edit4.setText(self.line_edit1.text() + self.line_edit2.text() + self.spin_box3.text())


# Uruchomienie okna
app = QApplication([])
win = Window()
win.show()
app.exec_()
