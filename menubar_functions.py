from PyQt4 import QtCore, QtGui


class menubar_functions():
    def background_color(self):
        print "background_color"
        #color=QtGui.QColorDialog.getColor(directory ="..")
        #color=[color.red(),color.green(),color.blue()]
        #print color
        renderer=self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer()
        renderer.SetBackground(self.qcolor2rgb(QtGui.QColorDialog.getColor()))
        
    def qcolor2rgb(self, qcolor):
		return [qcolor.red(),qcolor.green(),qcolor.blue()]
