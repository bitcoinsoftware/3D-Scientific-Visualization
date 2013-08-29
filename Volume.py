import vtk
from Rendered_Object import *
from Color_Function import *

class Volume(Rendered_Object,Color_Function):
    name="Volume"
    def __init__(self,data_reader):
        #if vtk_structured_points_data!=None:
         #   ukosniki=vtk_structured_points_data.count("/")
          #  etykieta=vtk_structured_points_data.split("/",ukosniki)
           # self.WhoAmI=self.WhoAmI+" "+ etykieta[ukosniki]

    #def make_name(self,name):
     #   if name!=None:
      #      ukosniki=name.count("/")
       #     etykieta=name.split("/",ukosniki)
        #    self.WhoAmI=self.WhoAmI+" "+ etykieta[ukosniki]

        self.make_color_function(data_reader.get_data_set().GetScalarRange())
        # The property describes how the data will look
        self.volumeProperty= vtk.vtkVolumeProperty()
        self.volumeProperty.SetColor(self.colorTransferFunction)
        self.volumeProperty.SetScalarOpacity(self.opacityTransferFunction)
        self.volumeProperty.SetGradientOpacity(self.gradientTransferFunction)
        # The mapper / ray cast function know how to render the data
        self.compositeFunction=vtk.vtkVolumeRayCastCompositeFunction()
  
        self.cast=vtk.vtkImageCast()
        self.cast.SetInput(data_reader.get_data_set())
        self.cast.SetOutputScalarTypeToUnsignedShort()

        self.cast.ClampOverflowOff()   
        self.mapper=vtk.vtkVolumeRayCastMapper()
        self.mapper.SetVolumeRayCastFunction(self.compositeFunction)
        self.mapper.SetInputConnection(self.cast.GetOutputPort())
        
        self.actor=vtk.vtkVolume()
        self.actor.SetMapper(self.mapper)
        self.actor.SetProperty(self.volumeProperty)
