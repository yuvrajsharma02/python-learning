import sys   # here we import the library
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLayout, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

class MainWindow(QMainWindow):  #create a main window 
    def __init__(self):  #define a constructor here 
        super().__init__() 
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):   # define a function init ui and give a para meter self 
        central_widget = QWidget()   # central_widget (ek variable jo humne define kiya hai ..)
        self.setCentralWidget(central_widget)  # self(main window ), setcentralwidgets (buit in function)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color : red")
        label2.setStyleSheet("background-color : green")
        label3.setStyleSheet("background-color : pink")
        label4.setStyleSheet("background-color : yellow")
        label5.setStyleSheet("background-color : blue")

        vbox = QVBoxLayout()

        vbox.addWidget(label1)  
        vbox.addWidget(label2)  
        vbox.addWidget(label3)  
        vbox.addWidget(label4)  
        vbox.addWidget(label5)

        central_widget.setLayout(vbox)  



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
