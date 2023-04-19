import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, \
     QWidget, QGridLayout, QLineEdit, QPushButton, QMainWindow
from  PyQt6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        # Menu bar widgets
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        # Sub bar
        add_student_action = QAction("Add Student", self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)





app = QApplication(sys.argv)
student_data = MainWindow()
student_data.show()
sys.exit(app.exec())