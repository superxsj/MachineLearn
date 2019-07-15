import sys
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from PyQt5.QtWidgets import QApplication , QWidget , QMainWindow , QMessageBox
from first import *
import matplotlib.pyplot as plt

class MyfisrtWeight(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyfisrtWeight, self).__init__(parent)
        self.setupUi(self)
        self.DM3_4.clicked.connect(DataDeal.makeblods)

class DataDeal():
    def makeblods(self):
        data = make_blobs(n_samples=200,centers=2,random_state=8)
        X,y = data
        plt.scatter(X[:,0],X[:,1],c = y,cmap=plt.cm.spring,edgecolors='k')
        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyfisrtWeight()
    myWidget.show()
    sys.exit(app.exec())