import vtk
from Slicing_Matrix import *
from Rendered_Object import *


class Contour(Rendered_Object, Slicing_Matrix):
    name="Contour"	
    def __init__(self,data_reader,origin,normal,camera_normal):
        self.axial=self.get_matrix(data_reader,origin,normal,camera_normal)
        # Extract a slice in the desired orientation
        self.reslice = vtk.vtkImageReslice()
        self.reslice.SetInput(data_reader.get_data_set())
        self.reslice.SetOutputDimensionality(2)
        self.reslice.SetResliceAxes(self.axial)
        self.reslice.SetInterpolationModeToLinear()
        
        self.contour=vtk.vtkContourFilter()
        self.contour.SetInputConnection(self.reslice.GetOutputPort())

        self.contour.GenerateValues(25, data_reader.get_scalar_range())
        self.contour.ComputeScalarsOn()
        self.contour.ComputeGradientsOn()      
        self.cutmapper=vtk.vtkPolyDataMapper()
        self.cutmapper.SetInputConnection(self.contour.GetOutputPort())  
        self.actor=vtk.vtkActor()
        self.actor.SetMapper(self.cutmapper)
        self.actor.PokeMatrix(self.axial)
        c="c"
        if origin[0]==c or origin[1]==c or origin[2]==c:
			origin=self.center
        
        origin=(float(origin[0]),float(origin[1]),float(origin[2]))
        self.actor.SetOrigin(origin)		  
