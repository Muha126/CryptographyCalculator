"""GUI for calculator."""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QGridLayout, QLineEdit, QComboBox
from PyQt6.QtCore import Qt, QTimer
from calculator import evaluateExpression, PyCalc
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import wmi
import os
import sqlite3


WINDOW_SIZE = 400
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40
enc_dir = 'C:/Users/umaro/Desktop/Projects/CryptographyCalculator/enc_data'
enc_path = os.path.join(enc_dir, "enc_data.db")

def get_usb_drives():
    c = wmi.WMI()
    drives = []
    for disk in c.Win32_LogicalDisk(DriveType=2):
        drives.append((disk.DeviceID, disk.VolumeName))
    return drives

usb_drives = get_usb_drives()

connection = sqlite3.connect(enc_path)
cursor = connection.cursor()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS enc_data(
            id integer PRIMARY KEY AUTOINCREMENT,
            usb TEXT UNIQUE NOT NULL,
            encrypted_data BLOB NOT NULL
        );
     """)
connection.commit()
connection.close()

class encryptedWindow(QMainWindow):
    """Create window with encrypted data"""

    def __init__(self):
        """Window and its parameters."""
        ###make all this lines funcitons
        super().__init__()
        self.setWindowTitle("Encrypted Data")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.generalLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.generalLayout)
        self.input = QLineEdit(self)
        self.input.setFixedSize(350,50)
        self.input.move(30,30)
        button = QPushButton("Encrypt and write")      
        button.clicked.connect(self.get)
        self.generalLayout.addWidget(button)
        self.UsbSelector = QComboBox()
        self.generalLayout.addWidget(self.UsbSelector)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_usb_list)
        self.timer.start(2000)
        self.current_usb_set = set()
        self.refresh_usb_list()
        self.UsbSelector.addItem("Choose USB drive:")
        self.UsbSelector.setCurrentIndex(0)
        self.UsbSelector.model().item(0).setEnabled(False)


    
    
    
    def refresh_usb_list(self):
        drives = get_usb_drives()
        new_usb_set = set(drives)
        if new_usb_set != self.current_usb_set:
            self.current_usb_set = new_usb_set
            self.UsbSelector.clear()
            self.UsbSelector.addItem("Choose USB drive:")
            self.UsbSelector.model().item(0).setEnabled(False)
        for device_id, volume_name in drives:
            display_text = f"{device_id} = {volume_name}" if volume_name else device_id
            self.UsbSelector.addItem(display_text, device_id)
    

    def get(self):
        from PyQt6.QtWidgets import QMessageBox

        text = self.input.text().strip()
        if not text:
            QMessageBox.warning(self, "Input Error", "Введите текст для шифрования.")
            return

        """Generating RSA"""
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()

        """Encrypting text"""
        try:
            encrypted = public_key.encrypt(
                text.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        except Exception as e:
            QMessageBox.critical(self, "Encryption Error", f"Ошибка шифрования: {e}")
            return

        """Get USB"""
        index = self.UsbSelector.currentIndex()
        if index <= 0:
            QMessageBox.warning(self, "USB Error", "Выберите USB-накопитель.")
            return
        usb_path = self.UsbSelector.currentData()

        """Save key on USB"""
        try:
            private_bytes = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
            with open(os.path.join(usb_path, "private_key.pem"), "wb") as f:
                f.write(private_bytes)
        except Exception as e:
            QMessageBox.critical(self, "Write Error", f"Не удалось записать ключ: {e}")
            return

        """Save data in DB"""
        try:
            connection = sqlite3.connect(enc_path)
            cursor = connection.cursor()
            cursor.execute(
                "INSERT OR REPLACE INTO enc_data (usb, encrypted_data) VALUES (?, ?)",
                (usb_path, encrypted)
            )
            connection.commit()
            connection.close()
        except Exception as e:
            QMessageBox.critical(self, "DB Error", f"Ошибка записи в БД: {e}")
            return

        QMessageBox.information(self, "Success", "Успешно зашифровано и записано на USB.")
        self.input.clear()



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





