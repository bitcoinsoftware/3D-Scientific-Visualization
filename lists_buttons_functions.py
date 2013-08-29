from Data_Cutter import *
from New_Render_Widget import *
from PyQt4 import QtCore, QtGui



class lists_buttons_functions():
    # data set buttons
    def delete_data_object(self):
        print "delete_data_object" 
        if self.listWidget_2.count()>0 and self.listWidget_2.currentRow()>-1:  #gdy w listboxie jest wicej niz 0 elementow i jest jakis zaznaczony 
            self.data_set_list.pop(self.listWidget_2.currentRow())
            self.listWidget_2.takeItem(self.listWidget_2.currentRow())
        else:
			print "there are no elements left in the listbox"
			
    def cut_data_set(self):
        print "cut"
        cut_value=[self.kintnuminput.value(),self.kintnuminput_2.value(),self.kintnuminput_4.value(),self.kintnuminput_5.value(),self.kintnuminput_7.value(),self.kintnuminput_8.value()]
        row=self.listWidget_2.currentRow()
        data_reader = self.data_set_list[row]
        cutter=Data_Cutter(data_reader,cut_value)
        data_reader.set_vtkReader(cutter.get_vtkReader())
        #change dimmensions in name in listwidget
        self.change_name_of_row(row,data_reader.get_name(),data_reader)
        print self.data_set_list[row].get_data_set().GetDimensions()
        
    def new_window(self):
        print "new_window"
        if self.listWidget.count()>0:
            object=self.rendered_objects_list[self.listWidget.currentRow()]
            actor=object.get_actor() 
            newwin = New_Render_Widget_Package(actor)
            #newwin.widget.add_actor(actor)
            newwin.start()
    
        else:
			print "there are no elements left in the listbox"  
        
        
    def hide(self):
        print "hide"
        renderer=self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer()
    def show(self):
        print "show"
    def delete_all_rendered_objects(self):
        print "delete_all_rendered_objects"
        objs_numb=len(self.rendered_objects_list)
        for obj_num in range(objs_numb):
            print(obj_num)
            object=self.rendered_objects_list.pop(objs_numb-obj_num-1) # zwraca obiekt z listy i wywoluje jego destruktora
            try:
                self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer().RemoveActor(object.get_actor())
            except:
                self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer().RemoveVolume(object.get_actor())
            object.delete()
            self.listWidget.takeItem(objs_numb-obj_num -1) #wyjmuje obiekt z listy nazw obiektow
			
        
    def delete_rendered_object(self):
        if self.listWidget.count()>0:
            object=self.rendered_objects_list.pop(self.listWidget.currentRow())
            try:
                self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer().RemoveActor(object.get_actor())
            except:
				self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer().RemoveVolume(object.get_actor())
            object.delete()
            self.listWidget.takeItem(self.listWidget.currentRow())
        else:
			print "there are no elements left in the listbox"      
			

		
