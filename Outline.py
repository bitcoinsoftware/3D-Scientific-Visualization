import vtk
from Rendered_Object import *

class Outline(Rendered_Object):
    name="Outline"
    def __init__(self,reader):
		self.outline=vtk.vtkOutlineFilter()
		self.outline.SetInput(reader.get_data_set())
		self.outlinemapper=vtk.vtkPolyDataMapper()
		self.outlinemapper.SetInput(self.outline.GetOutput())
		self.actor=vtk.vtkActor()
		self.actor.SetMapper(self.outlinemapper)
		self.actor.GetProperty().SetColor(0,0,0)
