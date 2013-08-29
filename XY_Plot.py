import vtk
from New_Render_Widget import *
#from Tkinter import *
#from Rendered_Object import *
from Line_Widget import *
import vtkTkRenderWidget
#klasa odpowiedzialna za rysowanie wykresu 1D
class XY_Plot(Rendered_Object):
    name = "XY_Plot"
    def __init__(self,data_reader,main_renderer,main_interactor,chart_points):
        
        self.poly_data=vtk.vtkPolyData()
        self.lw=Line_Widget(data_reader,main_renderer,main_interactor,self,chart_points)
        
        self.probe_filter=vtk.vtkProbeFilter()
        self.probe_filter.SetInput(self.poly_data)
        
        self.probe_filter.SetSource(data_reader.get_data_set())
        self.actor=vtk.vtkXYPlotActor()
        self.actor.AddInput(self.probe_filter.GetOutput())
        self.actor.GetPositionCoordinate().SetValue(0.05,0.05,0)
        self.actor.GetPosition2Coordinate().SetValue(0.95,0.95,0)

        self.actor.SetYRange(data_reader.get_scalar_range())
        self.actor.SetXValuesToArcLength()
        self.actor.SetNumberOfXLabels(6)
        self.actor.SetTitle("Data")
        self.actor.SetXTitle("s")
        self.actor.SetYTitle("f(s)")
        self.actor.GetProperty().SetColor(0,0,0)
        self.actor.GetProperty().SetLineWidth(2)
        self.actor.SetLabelFormat("%g")
        self.actor.GetTitleTextProperty().SetFontFamilyToArial()
        #main_renderer.AddActor2D(self.actor)
         
        #main_renderer.Render()
        # tu wystartuje nowy watek z wykresem w nowym oknie
        newwin = New_Render_Widget_Package(self.actor)
        #newwin.widget.add_actor(actor)
        newwin.start()
        
        
        
    def write(self):
        writer=vtk.vtkPolyDataWriter()
        writer.SetInput(self.probe_filter.GetOutput())
        
        #proboje wczytac workspace z pliku, jesli sie nie uda to otwiera folder w ktorym sie znajduje kod
        try:
            dir=ReadFile().read_variable('output_folder:')
        except:
            dir=""
        self.filename=asksaveasfilename(initialdir=dir,filetypes=[("allfiles","*"),("VTKfiles","*.vtk")])
        writer.SetFileName(self.filename)
        writer.Write()
        
        #pu=vtk2normal_plot(self.filename)
        #pu.write_to_file(self.filename,pu.plot_data)
     
