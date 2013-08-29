import vtk
from PyQt4 import QtCore, QtGui

class camera_buttons_functions():
    #camera buttons - left-upper side of the window 
    def set_view(self):
        print "set_view"
        view_string=str(self.textEdit.toPlainText())
        print view_string
        view=[1,0,0]
        view_str_arr =view_string.split()
        if len(view_str_arr)>2:
            view[0]=float(view_str_arr[0])
            view[1]=float(view_str_arr[1])
            view[2]=float(view_str_arr[2])
        renderer=self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer()
        renderer.GetActiveCamera().SetViewUp(view)
        renderer.ResetCamera()
    def x_view(self):
        print "x_view"
        renderer=self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer()
        renderer.GetActiveCamera().SetViewUp(1,0,0)
        renderer.ResetCamera()
    def y_view(self):
        print "y_view"
        renderer=self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer()
        renderer.GetActiveCamera().SetViewUp(0,1,0)
        renderer.ResetCamera()
    def z_view(self):
        print "z_view"
        renderer=self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer()
        renderer.GetActiveCamera().SetViewUp(0,0,1)
        renderer.ResetCamera()
    def reset_camera(self):
        print "reset_camera"
        renderer=self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer()
        renderer.ResetCamera()
        
    #zoom button
    def apply(self):
        print "apply_zoom"
    def photo(self):
        print "photo"
        
        magnif=str(self.plainTextEdit_2.toPlainText ()) 
        
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
  
