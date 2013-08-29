import vtk

class Data_Reader:
  
	
    def __init__(self,url):
        #self.index=index
        self.index=0
        self.url=url
        type=self._check_file_type_by_extension(url)  #checks the type of file by extension
	    
        self._create_vtk_reader(url,type)
	    #tu musi byc funkcja dodajaca tego readera do listy
  
########################################################################	  
	  
	    
	#sprawdza rodzaj pliku	
    def _check_file_type_by_extension(self,url):
		splited_url=url.split('.')
		length=len(splited_url)
		print length
		extension=splited_url[length-1]
		if extension=='vtk':
			return 1
		if extension=='general':
			return 0
			
	#tworzy vtkDataSetReadera ze wsystkimi danymi	
    def _create_vtk_reader(self,url,type):
        if type==1:
            self.reader=vtk.vtkDataSetReader()
            self.reader.SetFileName(url)
            self.reader.Update()
            print "zrobilem vtk readera"
        if type==0:
			print "convert_dat_file_to_vtk_reader(url)"
			
			self.reader=self.convert_dat_file_to_vtk_reader(url)
			
    def get_data_set(self):
		return self.reader.GetOutput()
	
    def get_url(self):
        return self.url
        
    def get_dimensions(self):
		return self.reader.GetOutput().GetDimensions()
		
    def get_bounds(self):
		return self.reader.GetOutput().GetBounds()
		
    def set_vtkReader(self,reader):
		self.reader=reader
		
    def get_output_port(self):
		return self.reader.GetOutputPort()

    def get_scalar_range(self):
		return self.reader.GetOutput().GetScalarRange()
 
    def get_center(self):
		return self.reader.GetOutput().GetCenter()
    
    def get_name(self):
        url=self.get_url()
        splited_url=url.split('/')
        file_name=splited_url[len(splited_url)-1]
        name=file_name+str(self.get_dimensions())
        return name
        
    def convert_dat_file_to_vtk_reader(self,header_url):
        self.data=vtk.vtkImageData()
        
        self.header_file=open(header_url,'r')   #otwieram plik z zapisanymi wlasciwosciami pliku .dat
        self.make_header(header_url)
        
        self.data.SetScalarTypeToDouble()
        dim_x=int(self.dimensions[0])
        dim_y=int(self.dimensions[1])
        dim_z=int(self.dimensions[2])
        self.data.SetDimensions(dim_x,dim_y,dim_z)
        self.data.SetOrigin(self.origin)
        self.data.SetSpacing(self.spacing)
        scalars =vtk.vtkDoubleArray()
        scalars.SetNumberOfValues(dim_x*dim_y*dim_z)
        self.header_file.close()
        
        self.z=0
        file=open(self.data_file_name,'r')
        stringi=file.read()
        tablica=stringi.split()
  
        
        for self.z in range(dim_z):
            for self.y in range(dim_y):
                arr=file.readline().split(' ',dim_y-1)
                for self.x in range(dim_x):
                    id =self.z*(dim_x*dim_y)+self.y*dim_x+self.x
                    scalars.InsertValue(id,float(tablica[id]))  
                             
           
        self.data.GetPointData().SetScalars(scalars)

        file.close()
        
        return self.return_vtk_reader(self.data)
        
    def make_header(self,header_url):
        for line in self.header_file:
            if line.rfind('file')!=-1:
                end=header_url.rfind('/')
                path=header_url[0:end+1]
                print path
                self.data_file_name=path+(line.split(' = ',1)[1]).split('\n',1)[0]
                print self.data_file_name
            elif line.rfind('position')!=-1:
                temp=line.split(' = ',2)
                temp2= temp[1].split(', ',8)
                i=0
                temp_spacing=[1,1,1]
                temp_origin=[0,0,0]
                for elem in temp2:
					if i==3 or i==7 or i==5: 
						temp_origin[(i-3)/2]=float(elem)  # Poprawilem JA
					if i==6 or i==4 or i==8:
						temp_spacing[(i-4)/2]=float(elem)  #Poprawilem JA
					i+=1
                self.make_spacing(temp_spacing)
                self.make_point_quanty()
                self.make_origin(temp_spacing,temp_origin)
            elif line.rfind('grid')!=-1:
                self.dimensions=((line.split(' = ',1)[1]).split('\n',1)[0]).split(' x ',2)
				             
    def make_spacing(self,temp_sp):
        minimum = 1.0e-10  # to jest dlugosc Angstrema w m, bo w metrach czytamy plik, czyli przeliczamy na Angstremy
        print temp_sp
        self.spacing=[(temp_sp[0]/minimum),(temp_sp[1]/minimum),(temp_sp[2]/minimum)]
    
    def make_point_quanty(self):
		self.point_quanty=int(self.dimensions[0])*int(self.dimensions[1])*int(self.dimensions[2])
		
    def make_origin(self,t_spc,t_origin):            
        minimum = 1.0e-10 # przelicz na angstremy
        self.origin=[(t_origin[0]/minimum),(t_origin[1]/minimum),(t_origin[2]/minimum)] # nie musi byc calkowita ilosc angstremow
    
    def get_output(self):
		return self.data
		
    def return_vtk_reader(self,data):
        self.reader=vtk.vtkExtractVOI()
        self.reader.SetInput(data)
        #self.reader.SetVOI(data.GetBounds())
        self.reader.Update()
        return self.reader
        
    def get_spacing(self):
		return self.reader.GetOutput().GetSpacing()
		
    def get_origin(self):
        return self.reader.GetOutput().GetOrigin()
    def get_whole_extent(self):
        return self.reader.GetOutput().GetWholeExtent()
        
		

