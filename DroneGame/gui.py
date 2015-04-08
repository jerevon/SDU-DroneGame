import sys
import rospy
from geometry_msgs.msg import Point
from threading import Thread
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("testui.ui")[0]                 # Load the UI

def ros_thread():
	rospy.spin()
	


class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #self.buttonOk.clicked.connect(self.button_ok_clicked)  # Bind the event handlers
        #self.buttonCancel.clicked.connect(self.button_cancel_clicked)  #   to the buttons

    '''def button_ok_clicked(self):                  # CtoF button event handler
	self.labelOut.setText("Ok clicked")
    def button_cancel_clicked(self):                 # FtoC button event handler
	self.labelOut.setText("Cancel clicked")'''

    def moveLabel(self, msg):
	self._labelDrone.move(msg.x,msg.y)

    def callback(self, msg):
	self.moveLabel(msg)

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)

rospy.init_node('drone_game_v1', anonymous=True)
rospy.Subscriber("positionPublisher5", Point, myWindow.callback)
thread = Thread(target = ros_thread)
thread.start()
#thread.join()

myWindow.show()
app.exec_()
