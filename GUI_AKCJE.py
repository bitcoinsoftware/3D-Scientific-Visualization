from PyQt4 import QtCore, QtGui
from function_buttons_functions import function_buttons_functions
from camera_buttons_functions import camera_buttons_functions
from lists_buttons_functions import lists_buttons_functions
from menubar_functions import *
import vtk

class GUI_AKCJE(function_buttons_functions, camera_buttons_functions, lists_buttons_functions, menubar_functions):    
    def connections(self):
        QtCore.QObject.connect(self.pushButton_25,QtCore.SIGNAL('clicked()'),self.hello_world)
        QtCore.QObject.connect(self.pushButton_8,QtCore.SIGNAL('clicked()'),self.axes)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL('clicked()'),self.isosurface)
        QtCore.QObject.connect(self.pushButton_5,QtCore.SIGNAL('clicked()'),self.layers_dots)
        QtCore.QObject.connect(self.pushButton_4,QtCore.SIGNAL('clicked()'),self.mat_plot_3d)
        QtCore.QObject.connect(self.pushButton_7,QtCore.SIGNAL('clicked()'),self.outline)
        QtCore.QObject.connect(self.pushButton_6,QtCore.SIGNAL('clicked()'),self.vector_field)
        QtCore.QObject.connect(self.pushButton_3,QtCore.SIGNAL('clicked()'),self.xy_plot)
        QtCore.QObject.connect(self.pushButton_2,QtCore.SIGNAL('clicked()'),self.xyz_plot)
        QtCore.QObject.connect(self.pushButton_13,QtCore.SIGNAL('clicked()'),self.sphere_volume)
        QtCore.QObject.connect(self.pushButton_14,QtCore.SIGNAL('clicked()'),self.scalar_bar)
        QtCore.QObject.connect(self.pushButton_15,QtCore.SIGNAL('clicked()'),self.volume)
        
        
        QtCore.QObject.connect(self.kurlrequester,QtCore.SIGNAL('urlSelected(KUrl)'),self.open_file)
        QtCore.QObject.connect(self.kurlrequester,QtCore.SIGNAL('returnPressed()'),self.open_file)
        
        QtCore.QObject.connect(self.pushButton_10,QtCore.SIGNAL('clicked()'),self.set_view)
        QtCore.QObject.connect(self.pushButton_26,QtCore.SIGNAL('clicked()'),self.x_view)
        QtCore.QObject.connect(self.pushButton_27,QtCore.SIGNAL('clicked()'),self.y_view)
        QtCore.QObject.connect(self.pushButton_28,QtCore.SIGNAL('clicked()'),self.z_view)
        QtCore.QObject.connect(self.pushButton_9,QtCore.SIGNAL('clicked()'),self.reset_camera)
        
        QtCore.QObject.connect(self.pushButton_11,QtCore.SIGNAL('clicked()'),self.apply)
        
        QtCore.QObject.connect(self.pushButton_12,QtCore.SIGNAL('clicked()'),self.photo)
        
        QtCore.QObject.connect(self.pushButton_16,QtCore.SIGNAL('clicked()'),self.delete_data_object)
        QtCore.QObject.connect(self.pushButton_29,QtCore.SIGNAL('clicked()'),self.cut_data_set)
        
        
        QtCore.QObject.connect(self.pushButton_21,QtCore.SIGNAL('clicked()'),self.new_window)
        QtCore.QObject.connect(self.pushButton_18,QtCore.SIGNAL('clicked()'),self.hide)
        QtCore.QObject.connect(self.pushButton_19,QtCore.SIGNAL('clicked()'),self.show)
        QtCore.QObject.connect(self.pushButton_20,QtCore.SIGNAL('clicked()'),self.delete_all_rendered_objects)
        QtCore.QObject.connect(self.pushButton_17,QtCore.SIGNAL('clicked()'),self.delete_rendered_object)
        QtCore.QObject.connect(self.actionBackground_color,QtCore.SIGNAL('activated()'),self.background_color)
        self.make_renderer()

        
    def make_renderer(self):
        self.qvtkWidget.Initialize()
        self.qvtkWidget.Start()
        # if you dont want the 'q' key to exit comment this.
        #self.qvtkWidget.AddObserver("ExitEvent", lambda o, e, a=app: a.quit())
        self.Renderer = vtk.vtkRenderer()
        self.Renderer.SetBackground(0,1,0)
        self.qvtkWidget.GetRenderWindow().AddRenderer(self.Renderer)
        # show the widget
        self.qvtkWidget.show()
        self.scalar_bar_number=0
