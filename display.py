import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QApplication, QDialog

class FrequencyPlot(QtGui.QWidget):
    def __init__(self):
        super(FrequencyPlot, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 400, 800, 450)
        self.setWindowTitle('Transcription')
        self.show()

def main():
    app = QApplication(sys.argv)
    w = FrequencyPlot()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
