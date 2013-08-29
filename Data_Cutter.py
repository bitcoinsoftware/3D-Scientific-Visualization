import vtk

class Data_Cutter:
    name = "Data Cutter"
		
    def __init__(self,data_reader,cuttings):
		
        original_bounds=data_reader.get_dimensions()  # pobieram pierwotne wymiary data_set
        print original_bounds ,"oryginalne wymiary"

        self.bounds = [0,0,0,0,0,0]    #zmieniam oryginalne wymiary, na wymiary pomnieszone o wprowadzone liczby

        
        self.bounds[0]=cuttings[0]
        self.bounds[1]=original_bounds[0]-cuttings[1]
        self.bounds[2]=cuttings[2]
        self.bounds[3]=original_bounds[1]-cuttings[3]
        self.bounds[4]=cuttings[4]
        self.bounds[5]=original_bounds[2]-cuttings[5]
                 
        self.cut_data_set(data_reader,self.bounds)  
			
    def get_cut_bounds(self):
        return self.bounds
            

    def cut_data_set(self,data_reader,bounds):
        self.cut_reader=vtk.vtkExtractVOI()
        self.cut_reader.SetInput(data_reader.get_data_set())
        self.cut_reader.SetVOI(bounds)
        self.cut_reader.Update()

    def get_vtkReader(self):
        return self.cut_reader
	

        

            	
			
    
