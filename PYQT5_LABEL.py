# In this code we can understand about the labels in GUI by PyQt5 library......


import sys 
import os  
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
 

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__()   
        
        self.setWindowTitle("My First App")
        self.setGeometry(200, 200, 500, 300)
        self.setWindowIcon(QIcon("Yuvraaj.ico"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial" , 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color : blue;"
                            "Background-color : #6fdcf7;"
                            "font-weight: bold;"
                            "font-style : italic;"
                            "text-decoration : underline;")
        
        # label.setAlignment(Qt.AlignTop) # it can tranfer the text at the top of the window
        # label.setAlignment(Qt.AlignVcenter) # for center and for bottom use bottom
        
        # label.setAlignment(Qt.AlignRight) # it can help to make its horizonttal right the text
        # label.setAlignment(Qt.AlignHCenter) # help to set in horizontall center 
        # label.setAlignment(Qt.Alignleft)
        
        # label.setAlignment(Qt.AlignHCenter | Qt.AignTop)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        # label.setAlignment(Qt.AlignHCenter | Qt.Alignvcenter)
        label.setAlignment(Qt.AlignCenter)

        print(os.getcwd())  
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
