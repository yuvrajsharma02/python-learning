import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # QMainWindow ka kaam pehle kar (window, close button, resize)
        
        self.setGeometry(700, 300, 1000, 1000)  # window ki position(700,300) aur size(1000,1000)
        
        # Radio buttons banana - har ek ka label aur parent window set ki
        self.radio1 = QRadioButton("visaa", self)
        self.radio2 = QRadioButton("master-card", self)
        self.radio3 = QRadioButton("Gift card", self)
        self.radio4 = QRadioButton("In-store", self)
        self.radio5 = QRadioButton("Online", self)
        
        # 2 alag groups banaye - dono groups se ek ek button select ho sakta hai
        self.button_group1 = QButtonGroup(self)  # payment type group (visa, mastercard, gift)
        self.button_group2 = QButtonGroup(self)  # shopping mode group (in-store, online)
        
        self.initUI()  # UI ka baaki kaam is function mein hai

    def initUI(self):
        # Har button ki position aur size set ki (x, y, width, height)
        self.radio1.setGeometry(0, 0, 300, 50)    # sabse upar
        self.radio2.setGeometry(0, 50, 300, 50)   # radio1 ke neeche
        self.radio3.setGeometry(0, 100, 300, 50)  # radio2 ke neeche
        self.radio4.setGeometry(0, 150, 300, 50)  # radio3 ke neeche
        self.radio5.setGeometry(0, 200, 300, 50)  # radio4 ke neeche

        # Saare radio buttons ki styling ek saath ki (CSS jaisa)
        self.setStyleSheet("QRadioButton{"
                           "font-size : 40px;"    # bada font
                           "font-family : Arial;" # Arial font
                           "padding : 10px;"      # thodi space
                           "}")
        
        # Group 1 mein payment wale buttons daale
        # in teeno mein se sirf ek hi select ho sakta hai
        self.button_group1.addButton(self.radio1)  # visa
        self.button_group1.addButton(self.radio2)  # mastercard
        self.button_group1.addButton(self.radio3)  # gift card
        
        # Group 2 mein shopping mode wale buttons daale
        # in dono mein se sirf ek hi select ho sakta hai
        self.button_group2.addButton(self.radio4)  # in-store
        self.button_group2.addButton(self.radio5)  # online

        # Har button ko ek hi function se connect kiya
        # jab bhi koi button click ho - radio_button_changed() chalegi
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()  # pata karo konse button ne bulaya
        
        if radio_button.isChecked():  # sirf tab print karo jab button ON ho
            # button ka label nikalo aur print karo
            print(f"{radio_button.text()} is selected")


if __name__ == '__main__':
    app = QApplication(sys.argv)  # PyQt5 application banaya
    window = MainWindow()         # hamari window banai
    window.show()                 # window screen pe dikhao
    sys.exit(app.exec_())         # app chalao, band hone par cleanly exit karo