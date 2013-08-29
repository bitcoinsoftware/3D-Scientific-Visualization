import vtk
from PyQt4 import QtGui
class rendering_scene_functions:
    def add_object_to_render_scene(self,object):
        print "add_object_to_render_scene"
        renderer=self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer()
        render_window=self.qvtkWidget.GetRenderWindow()
        try:
            renderer.AddActor(object.get_actor())
        except: 
            renderer.AddVolume(object.get_actor())
        renderer.ResetCamera()
        renderer.GetActiveCamera().SetViewUp(0,0.999,0)
        self.qvtkWidget.show()
        
        
    def add_objects_to_render_scene(self,object):
        renderer=self.qvtkWidget.GetRenderWindow().GetRenderers().GetFirstRenderer()
        render_window=self.qvtkWidget.GetRenderWindow()
        
        component_object_list = object.get_list_of_component_actors()
        for component_object in component_object_list:
            try:
                renderer.AddActor(component_object.get_actor())
            except: 
                renderer.AddVolume(component_object.get_actor())
        renderer.ResetCamera()
        renderer.GetActiveCamera().SetViewUp(0,0.999,0)
        self.qvtkWidget.show()
        print component_object_list
	


