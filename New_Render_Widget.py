# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_render_window.ui'
#
# Created: Sat Mar 19 18:54:14 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import threading
from QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk

class New_Render_Widget_Package(threading.Thread):
    def __init__(self,actor):
        threading.Thread.__init__(self)
        window = QtGui.QMainWindow()
        self.widget=New_Render_Widget(window)
        self.widget.add_actor(actor)
        window.show()
        QtGui.QMessageBox.information(self, "Hello!" , "Hello %s", QtGui.QMessageBox.Ok)  # bez tego okienko otwiera sie i od razu znika LOL
		

class New_Render_Widget(QtGui.QWidget):
    def __init__(self, parent=None):
        
        parent.resize(765,545)
        parent.setWindowTitle('Render scene')
        self.qvtkWidget = QVTKRenderWindowInteractor(parent)
        self.qvtkWidget.setGeometry(QtCore.QRect(0, 0, 761, 521))
        self.qvtkWidget.setObjectName("qvtkWidget")
        self.PhotoButton = QtGui.QPushButton(parent)
        self.PhotoButton.setGeometry(QtCore.QRect(0, 523,50, 20))
        self.Label = QtGui.QLabel(parent)
        self.Label.setGeometry(QtCore.QRect(55, 523,100, 20))
        self.plainTextEdit = QtGui.QPlainTextEdit(parent)
        self.plainTextEdit.setGeometry(QtCore.QRect(160, 523, 50, 20))
        
        self.XviewButton = QtGui.QPushButton(parent)
        self.XviewButton.setGeometry(QtCore.QRect(215, 523,50, 20))
        
        self.YviewButton = QtGui.QPushButton(parent)
        self.YviewButton.setGeometry(QtCore.QRect(270, 523,50, 20))
        
        self.ZviewButton = QtGui.QPushButton(parent)
        self.ZviewButton.setGeometry(QtCore.QRect(325, 523,50, 20))
        
        self.ResetCameraButton = QtGui.QPushButton(parent)
        self.ResetCameraButton.setGeometry(QtCore.QRect(380, 523,80,20))
        
        self.BackgroundColorButton = QtGui.QPushButton(parent)
        self.BackgroundColorButton.setGeometry(QtCore.QRect(465, 523,150,20))       
        
        self.PhotoButton.setText(QtGui.QApplication.translate("SubWindow", "Photo !", None, QtGui.QApplication.UnicodeUTF8))
        self.Label.setText(QtGui.QApplication.translate("MainWindow", "Set magnification", None, QtGui.QApplication.UnicodeUTF8))
        self.XviewButton.setText(QtGui.QApplication.translate("MainWindow", "Xview", None, QtGui.QApplication.UnicodeUTF8))
        self.YviewButton.setText(QtGui.QApplication.translate("MainWindow", "Yview", None, QtGui.QApplication.UnicodeUTF8))
        self.ZviewButton.setText(QtGui.QApplication.translate("MainWindow", "Zview", None, QtGui.QApplication.UnicodeUTF8))
        self.ResetCameraButton.setText(QtGui.QApplication.translate("MainWindow", "Reset Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.BackgroundColorButton.setText(QtGui.QApplication.translate("MainWindow", "Change background color", None, QtGui.QApplication.UnicodeUTF8))                
        
        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground(1,1,1)
        self.renderer.ResetCamera()
        self.qvtkWidget.GetRenderWindow().AddRenderer(self.renderer)
               
        QtCore.QObject.connect(self.PhotoButton,QtCore.SIGNAL('clicked()'),self.photo)
        QtCore.QObject.connect(self.XviewButton,QtCore.SIGNAL('clicked()'),self.x_view)
        QtCore.QObject.connect(self.YviewButton,QtCore.SIGNAL('clicked()'),self.y_view)
        QtCore.QObject.connect(self.ZviewButton,QtCore.SIGNAL('clicked()'),self.z_view)
        QtCore.QObject.connect(self.ResetCameraButton,QtCore.SIGNAL('clicked()'),self.reset_camera)
        QtCore.QObject.connect(self.BackgroundColorButton,QtCore.SIGNAL('clicked()'),self.change_background_color)

    def add_actor(self, actor):
        try:
			self.renderer.AddActor(actor)
        except:
			self.renderer.AddVolume(actor)
        self.renderer.Render()

    def photo(self):
        magnif=str(self.plainTextEdit.toPlainText ()) 
        
        if magnif=="":
            magnif=1
        else:
			magnif=int(magnif)
		          
        w2if=vtk.vtkWindowToImageFilter()
        w2if.Update()
        renderLarge= vtk.vtkRenderLargeImage()
        renderer=self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer()
        renderLarge.SetInput(renderer)
        renderLarge.SetMagnification(magnif)
        writer=vtk.vtkPNGWriter()
        writer.SetInputConnection(renderLarge.GetOutputPort())
        writer.SetFileName(str(QtGui.QFileDialog.getOpenFileName(directory ="./output")))
        writer.Write()

    def x_view(self):
        try:
            self.renderer.GetActiveCamera().SetViewUp(1,0,0)
            self.renderer.ResetCamera()
        except:
            print "x_view"		
   
    def y_view(self):
        try:
            self.renderer.GetActiveCamera().SetViewUp(0,1,0)
            self.renderer.ResetCamera()
        except:
		    print "y_view"
        
    def z_view(self):
        try:
            self.renderer.GetActiveCamera().SetViewUp(0,0,1)
            self.renderer.ResetCamera()
        except:
			print "z_view"
        
    def reset_camera(self):
        try:
            self.renderer.ResetCamera()
        except:
			print "reset_camera"
			
    def change_background_color(self):
        try:
            self.renderer.SetBackground(self.qcolor2rgb(QtGui.QColorDialog.getColor()))   
        except:
			print "change background color"
        
    def qcolor2rgb(self, qcolor):
		return [qcolor.red()/255.0,qcolor.green()/255.0,qcolor.blue()/255.0]
        
