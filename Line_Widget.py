#LINEWIDGET jest to odcinek po dla ktorego bedzie wykreslany wykres XY
import vtk
from Rendered_Object import *
class Line_Widget(Rendered_Object):
    name = "Line_Widget"
    def __init__(self,data_reader,main_renderer,main_interactor,chart,pts):

        self.widget=vtk.vtkLineWidget()
        self.widget.SetCurrentRenderer(main_renderer)
        #interactor = vtk.vtkRenderWindowInteractor()
        self.widget.SetInteractor(vtk.vtkRenderWindowInteractor())
        self.widget.SetInput(data_reader.get_data_set())
        self.widget.ClampToBoundsOff()
        self.widget.SetResolution(1000)
        self.widget.SetAlignToNone()
        
        self.point1=[pts[0],pts[1],pts[2]]
        self.point2=[pts[3],pts[4],pts[5]]
        self.widget.SetPoint1(self.point1)
        self.widget.SetPoint2(self.point2)

        self.widget.PlaceWidget()

        self.widget.AddObserver("InteractionEvent",self.PrepareProfile(chart))
        self.widget.On()
        
    def PrepareProfile(self,chart):
        self.widget.GetPolyData(chart.poly_data)

    def delete(self):
        self.widget.Off()
    #widgetu nie da sie schowac, mozna go tylko trwale wylaczyc
    def hide(self):
        return
    def show(self):
        return
