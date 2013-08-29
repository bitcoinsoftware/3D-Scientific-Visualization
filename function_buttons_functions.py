	#buttons on the right side of the rendered window
from PyQt4 import QtCore, QtGui
from PyKDE4.kdeui import KDoubleNumInput, KLineEdit

from Data_Reader import *
from Outline import *
from data_list_and_actor_list_functions import *
from Sphere_Volume import *
from rendering_scene_functions import *
from Vector_Field import *
from Cone import *
from Volume import *
from Layers_Dots import *
from Isosurface import *
from Axes import *
from Scalar_Bar import *
from Contour import *
from Color_Map import *
from XY_Plot import *
from MatPlot3d import *

class function_buttons_functions(data_list_and_actor_list_functions,rendering_scene_functions):	
    data_set_list=[]
    rendered_objects_list=[]
   
    def volume(self):
        print "volume"
        self.czarna_robota(Volume)
        self.frame_2.hide()
        self.frame_2.destroy()
        self.frame_2 = QtGui.QFrame(self.centralwidget) 
        self.frame_2.setGeometry(QtCore.QRect(0, 340, 120, 331))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.pushButton = QtGui.QPushButton(self.frame_2)
        self.frame_2.pushButton.setGeometry(QtCore.QRect(0, 40, 121, 21))
        self.frame_2.show()

    def selectFile(self):
        bubu=QtCore.QFileDialog.getOpenFileName()
        print bubu
        
    def axes(self):
        print "axes"
        renderer=self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer()
        self.czarna_robota2(Axes,renderer)
              
    def isosurface(self):
        print "isosurface"

        #self.removeChild(self.frame_2)
        self.frame_2.hide()
        self.frame_2.destroy()
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 340, 120, 331))
        label = QtGui.QLabel(self.frame_2)
        label.setGeometry(QtCore.QRect(0, 0, 121, 16))
        label.setText(QtGui.QApplication.translate("frame_2", "Scalar range:", None, QtGui.QApplication.UnicodeUTF8))
        
        label_2 = QtGui.QLabel(self.frame_2)
        label_2.setGeometry(QtCore.QRect(0, 18, 121, 16))
        label_2.setText(QtGui.QApplication.translate("frame_2", str(self.current_reader().get_scalar_range()), None, QtGui.QApplication.UnicodeUTF8))
        
        self.frame_2.kdoublenuminput = KDoubleNumInput(self.frame_2, decimals=5, singleStep=0.00001)
        self.frame_2.kdoublenuminput.setGeometry(QtCore.QRect(0, 37, 111, 21))
        
        pushButton = QtGui.QPushButton(self.frame_2)
        pushButton.setGeometry(QtCore.QRect(0, 60, 121, 21))
        pushButton.setText(QtGui.QApplication.translate("frame_2", "Single isosurface", None, QtGui.QApplication.UnicodeUTF8))
        StartLable = QtGui.QLabel(self.frame_2)
        StartLable.setGeometry(QtCore.QRect(0, 85,70, 16))
        StartLable.setText(QtGui.QApplication.translate("frame_2", "Start level", None, QtGui.QApplication.UnicodeUTF8))
        
        self.frame_2.kdoublenuminput2 = KDoubleNumInput(self.frame_2, decimals=5, singleStep=0.00001)
        self.frame_2.kdoublenuminput2.setGeometry(QtCore.QRect(60, 85, 55, 21))    
        
        EndLable = QtGui.QLabel(self.frame_2)
        EndLable.setGeometry(QtCore.QRect(0, 108,70, 16))
        EndLable.setText(QtGui.QApplication.translate("frame_2", "Final level", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_2.kdoublenuminput3 = KDoubleNumInput(self.frame_2, decimals=5, singleStep=0.00001)
        self.frame_2.kdoublenuminput3.setGeometry(QtCore.QRect(60, 108, 55, 21))


        StepLable = QtGui.QLabel(self.frame_2)
        StepLable.setGeometry(QtCore.QRect(0, 132,70, 16))
        StepLable.setText(QtGui.QApplication.translate("frame_2", "Set step", None, QtGui.QApplication.UnicodeUTF8))       
        self.frame_2.kdoublenuminput4 = KDoubleNumInput(self.frame_2, decimals=5, singleStep=0.00001)
        self.frame_2.kdoublenuminput4.setGeometry(QtCore.QRect(60,132, 55, 21))
        
        IsoAnimationButton = QtGui.QPushButton(self.frame_2)
        IsoAnimationButton.setGeometry(QtCore.QRect(0, 156,121, 21)) 
        IsoAnimationButton.setText(QtGui.QApplication.translate("frame_2", "Animate ", None, QtGui.QApplication.UnicodeUTF8))
        

        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.show()
        
        QtCore.QObject.connect(pushButton,QtCore.SIGNAL('clicked()'),self.make_isosurface)
        QtCore.QObject.connect(IsoAnimationButton,QtCore.SIGNAL('clicked()'),self.make_iso_animation)
        #pushButton.clicked.connect(self.czarna_robota2(Isosurface,kdoublenuminput.value()))
     
    def make_isosurface(self, level = -1):
        if level==-1:
            level=self.frame_2.kdoublenuminput.value()
        self.czarna_robota2(Isosurface,level)
   # lipa, trzeba zrobic jakiegos namespaca dla isosurfacow i w ogole nie wyglada jak powinno :-( 
   #a powinno robic animacje, na slabym komputerze w ogole nie ma szans
    def make_iso_animation(self):
        self.args = [self.frame_2.kdoublenuminput2.value(),self.frame_2.kdoublenuminput3.value(),self.frame_2.kdoublenuminput4.value()]
        self.czarna_robota2(Isosurface,self.args[0])
        print "make iso animation" , self.args
       

        self.renderWindowInteractor = self.qvtkWidget.GetRenderWindowInteractor()
        self.renderWindowInteractor.AddObserver('TimerEvent', self.make_single_iso_for_animation)
        
        self.timerId = self.renderWindowInteractor.CreateRepeatingTimer(2000);
			
    def make_single_iso_for_animation(self,event,object):
		self.args[0] = self.args[0] + self.args[2]
		if self.args[0] < self.args[1]:
		    self.czarna_robota2(Isosurface, self.args[0])
		    self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer().ResetCamera()
		else:
			self.renderWindowInteractor.DestroyTimer(self.timerId)
			return 0
		    
   
    def layers_dots(self):
        print "layers_dots"
        data_reader=self.data_set_list[self.listWidget_2.currentRow()]
        
        #reader=self.data_set_list[self.listWidget_2.currentRow()] #do zmiennej reader przypisuje readera z data_set_list o indeksie rownym currentRow
        rendered_object=Layers_Dots(data_reader,QtGui.QFileDialog.getOpenFileName(directory ="..")) #wywoluje konstruktor reprezentacji danych przy pomocy class_to_be_rendered
        self.add_objects_to_render_scene(rendered_object) # dodaje do sceny renderowana
        self.add_to_rendered_objects_list(rendered_object) #dodaje do listy i listboxa rendere_objects_list  
        
        #self.czarna_robota(Layers_Dots,path)
        
    def mat_plot_3d(self):
        print "mat_plot_3d"
        self.frame_2.hide()
        self.frame_2.destroy()
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 340, 120, 331))
        label = QtGui.QLabel(self.frame_2)
        label.setGeometry(QtCore.QRect(0, 0, 121, 16))
        label.setText(QtGui.QApplication.translate("frame_2", "Plane property:", None, QtGui.QApplication.UnicodeUTF8))
        
        label_2 = QtGui.QLabel(self.frame_2)
        label_2.setGeometry(QtCore.QRect(0, 18, 121, 16))
        label_2.setText(QtGui.QApplication.translate("frame_2", "Origin", None, QtGui.QApplication.UnicodeUTF8))


        self.kdoublenuminput = KLineEdit(self.frame_2)
        self.kdoublenuminput.setGeometry(QtCore.QRect(0, 37, 53, 21))
        self.kdoublenuminput2 = KLineEdit(self.frame_2)
        self.kdoublenuminput2.setGeometry(QtCore.QRect(42, 37, 53, 21))
        self.kdoublenuminput3 = KLineEdit(self.frame_2)
        self.kdoublenuminput3.setGeometry(QtCore.QRect(84, 37, 50, 21))
        
        label_3 = QtGui.QLabel(self.frame_2)
        label_3.setGeometry(QtCore.QRect(0, 60, 121, 16))
        label_3.setText(QtGui.QApplication.translate("frame_2", "Normal", None, QtGui.QApplication.UnicodeUTF8))
        
        self.kdoublenuminput01 = KLineEdit(self.frame_2)
        self.kdoublenuminput01.setGeometry(QtCore.QRect(0, 80, 53, 21))
        self.kdoublenuminput02 = KLineEdit(self.frame_2)
        self.kdoublenuminput02.setGeometry(QtCore.QRect(42, 80, 53, 21))
        self.kdoublenuminput03 = KLineEdit(self.frame_2)
        self.kdoublenuminput03.setGeometry(QtCore.QRect(84,80, 50, 21))
        
        pushButton = QtGui.QPushButton(self.frame_2)
        pushButton.setGeometry(QtCore.QRect(0, 103, 121, 21))
        pushButton.setText(QtGui.QApplication.translate("frame_2", "Single XYZplot", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.show()
        
        QtCore.QObject.connect(pushButton,QtCore.SIGNAL('clicked()'),self.make_mat_plot3d)
        
    def make_mat_plot3d(self):
        print("make_mat_plot3d")
        origin=[self.kdoublenuminput.text(),self.kdoublenuminput2.text(),self.kdoublenuminput3.text()]
        normal = [self.kdoublenuminput01.text(),self.kdoublenuminput02.text(),self.kdoublenuminput03.text()]
        reader=self.data_set_list[self.listWidget_2.currentRow()] #do zmiennej reader przypisuje readera z data_set_list o indeksie rownym currentRow
        camera_normal = [0,1,0]
        a=MatPlot3d(reader,origin,normal,camera_normal)
        
    def outline(self):
        print "outline"
        self.czarna_robota(Outline)
        #Outline(selected_Data_Reader)
        
    def vector_field(self):
        print "vector_field"
        self.czarna_robota(Vector_Field)
        
    def xy_plot(self):
        print "xy_plot"
        self.frame_2.hide()
        self.frame_2.destroy()
        
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 340, 120, 331))
        label = QtGui.QLabel(self.frame_2)
        label.setGeometry(QtCore.QRect(0, 0, 121, 16))
        label.setText(QtGui.QApplication.translate("frame_2", "Line property:", None, QtGui.QApplication.UnicodeUTF8))
        
        label_2 = QtGui.QLabel(self.frame_2)
        label_2.setGeometry(QtCore.QRect(0, 18, 121, 16))
        label_2.setText(QtGui.QApplication.translate("frame_2", "First point", None, QtGui.QApplication.UnicodeUTF8))


        self.kdoublenuminput = KLineEdit(self.frame_2)
        self.kdoublenuminput.setGeometry(QtCore.QRect(0, 37, 53, 21))
        self.kdoublenuminput2 = KLineEdit(self.frame_2)
        self.kdoublenuminput2.setGeometry(QtCore.QRect(42, 37, 53, 21))
        self.kdoublenuminput3 = KLineEdit(self.frame_2)
        self.kdoublenuminput3.setGeometry(QtCore.QRect(84, 37, 50, 21))
        
        label_3 = QtGui.QLabel(self.frame_2)
        label_3.setGeometry(QtCore.QRect(0, 60, 121, 16))
        label_3.setText(QtGui.QApplication.translate("frame_2", "Second point", None, QtGui.QApplication.UnicodeUTF8))
        
        self.kdoublenuminput01 = KLineEdit(self.frame_2)
        self.kdoublenuminput01.setGeometry(QtCore.QRect(0, 80, 53, 21))
        self.kdoublenuminput02 = KLineEdit(self.frame_2)
        self.kdoublenuminput02.setGeometry(QtCore.QRect(42, 80, 53, 21))
        self.kdoublenuminput03 = KLineEdit(self.frame_2)
        self.kdoublenuminput03.setGeometry(QtCore.QRect(84,80, 50, 21))
        
        pushButton = QtGui.QPushButton(self.frame_2)
        pushButton.setGeometry(QtCore.QRect(0, 103, 121, 21))
        pushButton.setText(QtGui.QApplication.translate("frame_2", "Single XYplot", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.show()
        
        QtCore.QObject.connect(pushButton,QtCore.SIGNAL('clicked()'),self.make_xy_plot)
        
    def make_xy_plot(self):
        points=[self.kdoublenuminput.text(),self.kdoublenuminput2.text(),self.kdoublenuminput3.text(),self.kdoublenuminput01.text(),self.kdoublenuminput02.text(),self.kdoublenuminput03.text()]
        points=[float(points[0]),float(points[1]),float(points[2]),float(points[3]),float(points[4]),float(points[5])]
        main_renderer=self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer()
        main_interactor=self.qvtkWidget.GetRenderWindowInteractor()
        self.czarna_robota5(XY_Plot,main_renderer,main_interactor,points)     
        
    def xyz_plot(self):
        print "xyz_plot"
        #origin=[10,10,15]
        #normal=[0.5,0.5,0.5]

        self.frame_2.hide()
        self.frame_2.destroy()
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 340, 120, 331))
        label = QtGui.QLabel(self.frame_2)
        label.setGeometry(QtCore.QRect(0, 0, 121, 16))
        label.setText(QtGui.QApplication.translate("frame_2", "Plane property:", None, QtGui.QApplication.UnicodeUTF8))
        
        label_2 = QtGui.QLabel(self.frame_2)
        label_2.setGeometry(QtCore.QRect(0, 18, 121, 16))
        label_2.setText(QtGui.QApplication.translate("frame_2", "Origin", None, QtGui.QApplication.UnicodeUTF8))


        self.kdoublenuminput = KLineEdit(self.frame_2)
        self.kdoublenuminput.setGeometry(QtCore.QRect(0, 37, 53, 21))
        self.kdoublenuminput2 = KLineEdit(self.frame_2)
        self.kdoublenuminput2.setGeometry(QtCore.QRect(42, 37, 53, 21))
        self.kdoublenuminput3 = KLineEdit(self.frame_2)
        self.kdoublenuminput3.setGeometry(QtCore.QRect(84, 37, 50, 21))
        
        label_3 = QtGui.QLabel(self.frame_2)
        label_3.setGeometry(QtCore.QRect(0, 60, 121, 16))
        label_3.setText(QtGui.QApplication.translate("frame_2", "Normal", None, QtGui.QApplication.UnicodeUTF8))
        
        self.kdoublenuminput01 = KLineEdit(self.frame_2)
        self.kdoublenuminput01.setGeometry(QtCore.QRect(0, 80, 53, 21))
        self.kdoublenuminput02 = KLineEdit(self.frame_2)
        self.kdoublenuminput02.setGeometry(QtCore.QRect(42, 80, 53, 21))
        self.kdoublenuminput03 = KLineEdit(self.frame_2)
        self.kdoublenuminput03.setGeometry(QtCore.QRect(84,80, 50, 21))
        
        pushButton = QtGui.QPushButton(self.frame_2)
        pushButton.setGeometry(QtCore.QRect(0, 103, 121, 21))
        pushButton.setText(QtGui.QApplication.translate("frame_2", "Single XYZplot", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.show()
        
        QtCore.QObject.connect(pushButton,QtCore.SIGNAL('clicked()'),self.make_xyz_plot)
        
    def get_camera_aligment(self):
        renderer=self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer()
        camera_aligment= renderer.GetActiveCamera().GetViewUp()
        return camera_aligment
        
    def make_xyz_plot(self):
        camera_aligment=self.get_camera_aligment()
        origin=[self.kdoublenuminput.text(),self.kdoublenuminput2.text(),self.kdoublenuminput3.text()]
        normal = [self.kdoublenuminput01.text(),self.kdoublenuminput02.text(),self.kdoublenuminput03.text()]
        self.czarna_robota4(Color_Map,origin,normal,camera_aligment)
        self.czarna_robota4(Contour,origin,normal,camera_aligment)
        
    def sphere_volume(self):
        print "sphere_volume"
        self.czarna_robota(Sphere_Volume_Actor)
        
    def scalar_bar(self):
        print "scalar_bar"
        self.czarna_robota2(Scalar_Bar,self.scalar_bar_number)
        self.scalar_bar_number+=1
        
    def hello_world(self):
		print "hello_world"
        
    def open_file(self):
        print "open_file"
        self.kurlrequester.setStartDir("../input")
        url=str(self.kurlrequester.text())  #zamienia Qstring na string
        reader=Data_Reader(url)
        self.add_to_data_list(reader)
			
    def czarna_robota(self,class_to_be_rendered):
        reader=self.data_set_list[self.listWidget_2.currentRow()] #do zmiennej reader przypisuje readera z data_set_list o indeksie rownym currentRow
        rendered_object=class_to_be_rendered(reader) #wywoluje konstruktor reprezentacji danych przy pomocy class_to_be_rendered
        self.add_object_to_render_scene(rendered_object) # dodaje do sceny renderowana
        self.add_to_rendered_objects_list(rendered_object) #dodaje do listy i listboxa rendere_objects_list
		
    def czarna_robota2(self,class_to_be_rendered,argument):
        reader=self.data_set_list[self.listWidget_2.currentRow()] #do zmiennej reader przypisuje readera z data_set_list o indeksie rownym currentRow
        rendered_object=class_to_be_rendered(reader,argument) #wywoluje konstruktor reprezentacji danych przy pomocy class_to_be_rendered
        self.add_object_to_render_scene(rendered_object) # dodaje do sceny renderowana
        self.add_to_rendered_objects_list(rendered_object) #dodaje do listy i listboxa rendere_objects_list
        
    def czarna_robota3(self,class_to_be_rendered,argument,argument2):
        reader=self.data_set_list[self.listWidget_2.currentRow()] #do zmiennej reader przypisuje readera z data_set_list o indeksie rownym currentRow
        rendered_object=class_to_be_rendered(reader,argument,argument2) #wywoluje konstruktor reprezentacji danych przy pomocy class_to_be_rendered
        self.add_object_to_render_scene(rendered_object) # dodaje do sceny renderowana
        self.add_to_rendered_objects_list(rendered_object) #dodaje do listy i listboxa rendere_objects_list
        
    def czarna_robota4(self,class_to_be_rendered,argument,argument2,argument3):
        reader=self.data_set_list[self.listWidget_2.currentRow()] #do zmiennej reader przypisuje readera z data_set_list o indeksie rownym currentRow
        rendered_object=class_to_be_rendered(reader,argument,argument2,argument3) #wywoluje konstruktor reprezentacji danych przy pomocy class_to_be_rendered
        self.add_object_to_render_scene(rendered_object) # dodaje do sceny renderowana
        self.add_to_rendered_objects_list(rendered_object) #dodaje do listy i listboxa rendere_objects_list
        
    def czarna_robota5(self,class_to_be_rendered,argument,argument2,argument3):
        reader=self.data_set_list[self.listWidget_2.currentRow()] #do zmiennej reader przypisuje readera z data_set_list o indeksie rownym currentRow
        rendered_object=class_to_be_rendered(reader,argument,argument2,argument3) #wywoluje konstruktor reprezentacji danych przy pomocy class_to_be_rendered
        self.add_object_to_render_scene(rendered_object) # dodaje do sceny renderowana
        self.add_to_rendered_objects_list(rendered_object) #dodaje do listy i listboxa rendere_objects_list
		
        
    def current_reader(self):
		return self.data_set_list[self.listWidget_2.currentRow()]
        
        
		
		
		
		
		
		
		
