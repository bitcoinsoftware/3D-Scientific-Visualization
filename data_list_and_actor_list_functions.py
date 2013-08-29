class data_list_and_actor_list_functions:
    def add_to_data_list(self,data_reader):
        #obrobka stringu url do postaci 
        name=data_reader.get_name()
        index = self.listWidget_2.count()  #wyliczie ilosci elementow w okienku z data objectami
        self.listWidget_2.insertItem(index,name) # dodanie na koniec kolejnego elementu
        self.data_set_list.append(data_reader)    
		
    def add_to_rendered_objects_list(self,rendered_object):
		name=rendered_object.get_name()
		index=self.listWidget.count()
		self.listWidget.insertItem(index,name)
		self.rendered_objects_list.append(rendered_object)
		
    def change_name_of_row(self,row,new_name,data_reader):
        self.listWidget_2.takeItem(row)
        if row==-1:
			self.add_to_data_list(data_reader)
        else:
            self.listWidget_2.insertItem(row,new_name)
