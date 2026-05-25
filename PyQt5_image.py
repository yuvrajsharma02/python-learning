# PyQt5 images
import sys 
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow (QMainWindow):  # here in this code we can learn about the set image on gui 
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)  

        label = QLabel(self)  #Window के अंदर एक QLabel बनाया
        label.setGeometry(0, 0, self.width(), self.height()) #Label को window के बिल्कुल corner (0,0) से शुरू किया, size भी 500x500

        pixmap = QPixmap("yuvrajsharma.jpeg")  #"yuvrajsharma.jpeg" file को QPixmap में load किया
        label.setPixmap(pixmap)  #वो image label पर set कर दी

        label.setScaledContents(True) #Image को label की size के अनुसार stretch/fit कर दिया

        print(os.getcwd()) 

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ =="__main__":
    main()
