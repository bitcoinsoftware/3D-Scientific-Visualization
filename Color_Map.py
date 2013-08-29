import vtk
from Rendered_Object import *
from Slicing_Matrix import *

class Color_Map(Rendered_Object,Slicing_Matrix):
    name="Color_Map"
    def __init__(self,data_reader,origin,normal,camera_normal):
        self.axial=self.get_matrix(data_reader,origin,normal,camera_normal)
                             
        # Extract a slice in the desired orientation
        self.reslice = vtk.vtkImageReslice()
	
        self.reslice.SetInput(data_reader.get_data_set())
        self.reslice.SetOutputDimensionality(2)
        self.reslice.SetResliceAxes(self.axial)
        self.reslice.SetInterpolationModeToLinear()
        
        # Create a colorscale lookup table
        self.lut=vtk.vtkLookupTable()
        self.lut.SetNumberOfColors(256)

        self.lut.SetTableRange(data_reader.get_scalar_range())
        self.lut.SetRange(data_reader.get_scalar_range())

        self.lut.SetHueRange(0,1)
        self.lut.Build()
        
        # Map the image through the lookup table
        self.color = vtk.vtkImageMapToColors()
        self.color.SetLookupTable(self.lut)
        self.color.SetInputConnection(self.reslice.GetOutputPort())
        
        # Display the image
        self.actor = vtk.vtkImageActor()
        self.actor.SetInput(self.color.GetOutput())
        c="c"
        if origin[0]==c or origin[1]==c or origin[2]==c:
			origin=self.center
        
        origin=(float(origin[0]),float(origin[1]),float(origin[2]))
        self.actor.SetOrigin(origin)
        self.actor.PokeMatrix(self.axial)
        
    def write(self):
        writer=vtk.vtkDataSetWriter()
        writer.SetInput(self.reslice.GetOutput())
        
        #proboje wczytac workspace z pliku, jesli sie nie uda to otwiera folder w ktorym sie znajduje plik
        try:
            dir=ReadFile().read_variable('output_folder:')
            print dir
        except:
            dir=""
        self.filename=asksaveasfilename(initialdir=dir,filetypes=[("allfiles","*"),("VTKfiles","*.vtk")])
        writer.SetFileName(self.filename)
        writer.Write() 
