import vtk
from Rendered_Object import *

class Isosurface(Rendered_Object):
    name="Isosurface"
    def __init__(self,data_reader,iso_level):
        # Find the triangles that lie along the 0.5 contour.
        self.filter = vtk.vtkContourFilter()

        self.filter.SetInput(data_reader.get_data_set())
        self.filter.SetValue(0, 0.5)
        self.filter.Update()
        self.mapper=vtk.vtkPolyDataMapper()
        self.mapper.ScalarVisibilityOn()
        self.mapper.SetScalarRange(data_reader.get_scalar_range())
        iso= data_reader.get_scalar_range()[1]/2.0
        
        self.actor=vtk.vtkActor()
        self.filter.GenerateValues(1,iso_level*(1-1/255.0),iso_level)
        self.mapper.SetInputConnection(self.filter.GetOutputPort())
        self.actor.SetMapper(self.mapper)
        self.actor.GetProperty().SetOpacity(0.7)
		
