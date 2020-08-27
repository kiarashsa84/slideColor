import sys 
from PyQt5.QtWidgets import QApplication , QWidget , QFrame, QSlider
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import random

class F(QWidget):
    def __init__(self): 
        super().__init__()
        self.setUI()
    
    def setUI(self):
        self.setGeometry(500,400,500,600)
        self.setWindowTitle("Table")

        self.Qf = QFrame(self)
        self.Qf.setGeometry(100 , 10 , 300 , 300)

        self.Qs = QSlider(Qt.Horizontal , self)
        self.Qs.setGeometry(100 , 520 , 300 ,15)


        self.pa = self.Qf.palette()
        role = self.Qf.backgroundRole()
        self.pa.setColor(role,QColor( 255 , 255 ,  255))
        self.Qf.setPalette(self.pa)
        self.Qf.setAutoFillBackground(True)

        self.Qs.valueChanged.connect(self.paint)



        self.show()


    def paint(self):

        R = []
        G = []
        B = []
        

        for i in range(0 , 100):
            R.append(random.randrange(0, 256))
            G.append(random.randrange(0, 256))
            B.append(random.randrange(0, 256))

        rang = []
        jam = []

        slideval= self.Qs.value()

        for b in range(0 , 100):
            rang=[R[b] , G[b] , B[b]]
            jam.append(rang)


        

        print(jam)

        self.palette = self.Qf.palette()
        r = self.Qf.backgroundRole()


        if slideval == 0 :
            self.x= 255
            self.y= 255
            self.z= 250


            self.palette.setColor(r , QColor(self.x , self.y, self.z))
            self.Qf.setPalette(self.palette)
            self.Qf.setAutoFillBackground(True)
        

        elif slideval== 99:
            self.x = 0
            self.y= 0
            self.z=0
            self.palette.setColor(r , QColor(self.x,self.y,self.z))
            self.Qf.setPalette(self.palette)
            self.Qf.setAutoFillBackground(True)

        else :
            self.x,self.y,self.z=jam[slideval]
            self.palette.setColor(r , QColor(self.x,self.y,self.z))
            self.Qf.setPalette(self.palette)
            self.Qf.setAutoFillBackground(True)




         




if __name__== "__main__":
    print(__name__)
    app = QApplication(sys.argv)
    ex=F()
    sys.exit(app.exec_())