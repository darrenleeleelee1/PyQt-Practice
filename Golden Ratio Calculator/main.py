from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
import datetime
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Golden Ratio Calculator")
        # width of window 
        self.w_width = 400
  
        # height of window 
        self.w_height = 430
  
        # setting geometry 
        # (start_x, start_y, width, height)
        self.setGeometry(800, 300, self.w_width, self.w_height)

        self.UiComponents()
        self.show()
    
    def UiComponents(self): 

        # creating head label 
        head = QLabel("Golden Ratio Calculator", self) 
        head.setWordWrap(True)
        head.setGeometry(0, 10, 400, 60)
        # font 
        font = QFont('Times', 15) # (字體, 大小) 
        font.setBold(True) # 粗體
        font.setItalic(True) # 斜體
        font.setUnderline(True) # 底線 
        # setting font to the head 
        head.setFont(font) 

        # setting alignment of the head 
        # Qt is defined in QtCore
        head.setAlignment(Qt.AlignCenter) 

        # setting color effect to the head 
        color = QGraphicsColorizeEffect(self) 
        color.setColor(Qt.darkGreen)
        head.setGraphicsEffect(color)

        # creating a radio button 
        self.length1 = QRadioButton("First Length (A)", self)
        # equal to
        # self.length1 = QRadioButton("First Length (A)")
        # self.layout().addWidget(self.length1) 
        
        # setting geometry 
        self.length1.setGeometry(50, 90, 140, 40) 
        # setting font 
        self.length1.setFont(QFont('Times', 9)) 

        # creating a spin box 
        self.l1 = QSpinBox(self) 
        self.l1.setMaximum(999999)
        # setting geometry to the spin box 
        self.l1.setGeometry(200, 90, 160, 40)
        # setting font
        self.l1.setFont(QFont('Times', 9)) 
        # setting alignment SpinBox裡面的文字置中
        self.l1.setAlignment(Qt.AlignCenter)


        self.length2 = QRadioButton("Second Length (B)", self)
        self.length2.setGeometry(50, 150, 140, 40)
        self.l2 = QSpinBox(self)
        self.l2.setMaximum(999999)
        self.l2.setGeometry(200, 150, 160, 40)
        self.l2.setFont(QFont('Time', 9))
        self.l2.setAlignment(Qt.AlignCenter)

        self.length3 = QRadioButton("First + Second", self)
        self.length3.setGeometry(50, 210, 140, 40)
        self.l3 = QSpinBox(self)
        self.l3.setMaximum(999999)
        self.l3.setGeometry(200, 210, 160, 40)
        self.l3.setFont(QFont('Time', 9))
        self.l3.setAlignment(Qt.AlignCenter)

        self.btn = QPushButton("Calculate", self)
        self.btn.setGeometry(int(self.w_width/2) - int(self.w_width/4), 270, int(self.w_width/2), 40)
App = QApplication(sys.argv) 
mw = MainWindow()
sys.exit(App.exec_()) 

