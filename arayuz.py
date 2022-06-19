import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
class MainWindow(QWidget):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.timer = QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.setInterval(10) # in milliseconds, so 5000 = 5 seconds
        self.timer.timeout.connect(self.loop)
        self.timer.start()
        self.resize(700, 700)
        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Kapat")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)
        self.port_secim_label = QtWidgets.QLabel(self)
        self.port_secim_label.setGeometry(QtCore.QRect(460, 50, 31, 20))
        self.port_secim_label.setObjectName("port_secim_label")
        self.Baudrate_label = QtWidgets.QLabel(self)
        self.Baudrate_label.setGeometry(QtCore.QRect(430, 80, 101, 20))
        self.Baudrate_label.setObjectName("Baudrate_label")
        self.port_secim_ComboBox = QtWidgets.QComboBox(self)
        self.port_secim_ComboBox.setGeometry(QtCore.QRect(490, 80, 69, 22))
        self.port_secim_ComboBox.setObjectName("port_secim_ComboBox")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.Baudrate_ComboBox = QtWidgets.QComboBox(self)
        self.Baudrate_ComboBox.setGeometry(QtCore.QRect(490, 50, 69, 22))
        self.Baudrate_ComboBox.setObjectName("Baudrate_ComboBox")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.baglan_buton = QtWidgets.QPushButton(self)
        self.baglan_buton.setGeometry(QtCore.QRect(490, 120, 75, 23))
        self.baglan_buton.setObjectName("baglan_buton")
        self.baglan_label = QtWidgets.QLabel(self)
        self.baglan_label.setGeometry(QtCore.QRect(490, 140, 91, 20))
        self.baglan_label.setObjectName("baglan_label")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(450, 450, 251, 251))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pashala logo tasarım 1 (5).png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(150, 70, 231, 271))
        self.retranslateUi(self)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.port_secim_label.setText(_translate("Dialog", "Port/"))
        self.Baudrate_label.setText(_translate("Dialog", "BaudRate/"))
        self.port_secim_ComboBox.setCurrentText(_translate("Dialog", "9600"))
        self.port_secim_ComboBox.setItemText(0, _translate("Dialog", "4800"))
        self.port_secim_ComboBox.setItemText(1, _translate("Dialog", "9600"))
        self.port_secim_ComboBox.setItemText(2, _translate("Dialog", "14400"))
        self.port_secim_ComboBox.setItemText(3, _translate("Dialog", "19200"))
        self.port_secim_ComboBox.setItemText(4, _translate("Dialog", "28800"))
        self.port_secim_ComboBox.setItemText(5, _translate("Dialog", "31250"))
        self.port_secim_ComboBox.setItemText(6, _translate("Dialog", "38400"))
        self.port_secim_ComboBox.setItemText(7, _translate("Dialog", "57600"))
        self.port_secim_ComboBox.setItemText(8, _translate("Dialog", "115200"))
        self.Baudrate_ComboBox.setItemText(0, _translate("Dialog", "COM1"))
        self.Baudrate_ComboBox.setItemText(1, _translate("Dialog", "COM2"))
        self.Baudrate_ComboBox.setItemText(2, _translate("Dialog", "COM3"))
        self.Baudrate_ComboBox.setItemText(3, _translate("Dialog", "COM4"))
        self.Baudrate_ComboBox.setItemText(4, _translate("Dialog", "COM5"))
        self.Baudrate_ComboBox.setItemText(5, _translate("Dialog", "COM6"))
        self.Baudrate_ComboBox.setItemText(6, _translate("Dialog", "COM7"))
        self.Baudrate_ComboBox.setItemText(7, _translate("Dialog", "COM8"))
        self.Baudrate_ComboBox.setItemText(8, _translate("Dialog", "COM9"))
        self.Baudrate_ComboBox.setItemText(9, _translate("Dialog", "COM10"))
        self.Baudrate_ComboBox.setItemText(10, _translate("Dialog", "COM11"))
        self.Baudrate_ComboBox.setItemText(11, _translate("Dialog", "COM12"))
        self.Baudrate_ComboBox.setItemText(12, _translate("Dialog", "COM13"))
        self.Baudrate_ComboBox.setItemText(13, _translate("Dialog", "COM14"))
        self.Baudrate_ComboBox.setItemText(14, _translate("Dialog", "COM15"))
        self.baglan_buton.setText(_translate("Dialog", "Bağlan"))
        self.baglan_label.setText(_translate("Dialog", "Bağlantı Bekleniyor"))
    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            print("W")
        elif event.key() == Qt.Key_S:
            print("S")
        elif event.key() == Qt.Key_A:
            print("A")
        elif event.key() == Qt.Key_D:
            print("D") 
    def CancelFeed(self):
        exit()
    def loop(self):
        pass
class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(400, 400, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()
    
if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())
