import vtk
from Rendered_Object import *

class Axes(Rendered_Object):
    name = "Axes"
    def __init__(self,data_reader,renderer):
		# Create a text property for cube axes
		self.tprop=vtk.vtkTextProperty()
		self.tprop.SetColor(1,1,1)
		self.tprop.ShadowOn()
		
		# Create a vtkCubeAxesActor2D.  Use the closest vertex to the camera to
        # determine where to draw the axes.  Add the actor to the renderer.
		self.actor=vtk.vtkCubeAxesActor2D()
		self.actor.SetInput(data_reader.get_data_set())
		self.actor.SetCamera(renderer.GetActiveCamera())
		self.actor.SetLabelFormat("%6.4g")
		self.actor.SetFlyModeToClosestTriad()
		self.actor.SetFontFactor(0.8)
		self.actor.GetProperty().SetColor(0,0,0)
		self.actor.ScalingOff()
		self.actor.SetAxisTitleTextProperty(self.tprop)
		self.actor.SetAxisLabelTextProperty(self.tprop)
