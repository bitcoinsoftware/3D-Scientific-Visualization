import vtk
from Rendered_Object import *

class Cone(Rendered_Object):
    def __init__(self):
        cone = vtk.vtkConeSource()
        cone.SetResolution(8)

        coneMapper = vtk.vtkPolyDataMapper()
        coneMapper.SetInput(cone.GetOutput())

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(coneMapper)
