import sys
from time import strftime, gmtime
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

curr_time = strftime("%H:%M:%S", gmtime())

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./UI/main.qml')
engine.rootObjects()[0].setProperty('currTime', curr_time)
sys.exit(app.exec())