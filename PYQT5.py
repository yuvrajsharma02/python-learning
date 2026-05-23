#PYQT5 = , developed by Riverbank Computing. It allows you to build powerful, cross-platform graphical user interface (GUI) applications for Windows, macOS, Linux, Android, and iOS

import sys #sys = system- specific parameter and function (help to acces some variable or function that interact act strongly with interpreter)
import os  #It acts as a bridge between Python and your computer's file system (it help for ico)
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
 

class MainWindow(QMainWindow):  #"मेरी window, QMainWindow की सारी powers use करेगी"
    def __init__(self): #  jab bhi MainWindow() likho, yeh automatically chalta
        super().__init__()  #Parent class (QMainWindow) का constructor भी चलाओ     
        
        self.setWindowTitle("My First App")
        self.setGeometry(200, 200, 500, 300)
        self.setWindowIcon(QIcon("Yuvraaj.ico"))

        print(os.getcwd())  # Get current working directory

def main(): #Ek function jo poora app start karta hai
 #Isko alag isliye rakhte hain taaki code clean aur organized rahe
    app = QApplication(sys.argv)
    window = MainWindow() #Isi waqt __init__ chalta hai
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# PyQt5 = GUI banane ki library
# QtWidgets = saare visible widgets yahan hain (buttons, windows, etc.)
# QApplication = poore app ka manager — sirf ek baar banta hai
# QMainWindow = ek ready-made window with menu bar, toolbar support


