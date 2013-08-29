import vtk

class Abstract_Dot:

    def znajdz_srodek_i_kat_obrotu(self,cechy):
        self.srodek=self.get_many_variables(cechy,"srodek kropki, <MinNPR !!!")
        self.obrot =self.get_many_variables(cechy,"obrot kropki")
	    
    def get_variable(self,DotDataFile,variable_name):
        if type(DotDataFile) == file:
            DotDataFile.seek(0)
        for line in DotDataFile:
            if variable_name in line:
                variable=float(line.split('#',2)[0])
                return variable

    def get_2_variables(self,DotDataFile,variables_name):
        if type(DotDataFile) ==file:
            DotDataFile.seek(0)
            
        for line in DotDataFile:
            if variables_name in line:
                array=line.split('#',2)
                array=array[0].split()
                array=[float(array[0]),float(array[1])]
                return array
                   
    def get_3_variables(self,DotDataFile,variables_name):
        if type(DotDataFile) == file:
            DotDataFile.seek(0)
            
        for line in DotDataFile:
            if variables_name in line:
                array=line.split('#',2)
                array=array[0].split()
                array=[float(array[0]),float(array[1]),float(array[2])]
                return array
                
    def get_many_variables(self,DotDataFile,variables_name):
        if type(DotDataFile)== file:
            DotDataFile.seek(0)
            
        for line in DotDataFile:
            if variables_name in line:
                array=line.split('#',2)
                array=array[0].split()
                return array    
                
    def get_bounds_and_center(self,volume):
        self.x_min=volume.vol.GetMinXBound()
        self.x_max=volume.vol.GetMaxXBound()
        self.y_min=volume.vol.GetMinYBound()
        self.y_max=volume.vol.GetMaxYBound()
        #print volume.reader.GetOutput().GetBounds()
        self.l_x= self.x_max-self.x_min
        self.l_y= self.y_max-self.y_min
        self.center_x=(self.x_max+self.x_min)/2.0
        self.center_y=(self.y_max+self.y_min)/2.0
        
    def get_actor(self):
		return self.actor
