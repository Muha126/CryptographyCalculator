"""GUI for calculator."""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QGridLayout, QLineEdit
from PyQt6.QtCore import Qt
from calculator import evaluateExpression, PyCalc
import usb.core
import os
import sqlite3


WINDOW_SIZE = 400
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40
enc_dir = 'C:/Users/umaro/Desktop/Projects/CryptographyCalculator/enc_data'
enc_path = os.path.join(enc_dir, "enc_data.db")
key_dir = 'C:/Users/umaro/Desktop/Projects/CryptographyCalculator/keys'
key_path = os.path.join(key_dir, "keys.db")


connection = sqlite3.connect(enc_path)
cursor = connection.cursor()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS enc_data(
            id integer PRIMARY KEY AUTOINCREMENT,
            usb TEXT UNIQUE NOT NULL,
            encrypted_data BLOB NOT NULL
        );
     """)
connection = sqlite3.connect(key_path)
cursor = connection.cursor()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS keys(
            id integer PRIMARY KEY AUTOINCREMENT,
            public_key TEXT NOT NULL
        );
     """)
connection.commit()
connection.close

class encryptedWindow(QMainWindow):
    """Create window with encrypted data"""

    def __init__(self):
        """Window and its parameters."""
        super().__init__()
        self.setWindowTitle("Encrypted Data")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.input = QLineEdit(self)
        self.input.move(150,150)



class PyCalcWindow(QMainWindow):
    """Create window and its parameters."""

    def __init__(self):
        """Window and its parameters."""
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()
        self.encryptedWindowInstance = None
    

    def _createDisplay(self):
        """Creates Display for displaying numbers and results."""
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)


    def _createButtons(self):
        """Create buttons on calculator."""
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "()"],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]
        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)
        self.generalLayout.addLayout(buttonsLayout)


    def setDisplayText(self, text):
        """Set the displays text."""
        self.display.setText(text)
        self.display.setFocus()


    def displayText(self):
        """Get the display's text."""
        return self.display.text()
    

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")


    def trigger(self):
        if self.display.text() == "1337*1337":
            self.encryptedWindowInstance = encryptedWindow()
            self.encryptedWindowInstance.show() 


def main():
    """Executes window."""
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    PyCalc(model=evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcApp.exec())
    


if __name__ == "__main__":
    main()





