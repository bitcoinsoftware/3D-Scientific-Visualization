import vtk
from Rendered_Object import *

class Scalar_Bar(Rendered_Object):
    name="Scalar_Bar"
    def __init__(self,data_reader,scalar_bar_number):
        # Create a colorscale lookup table
        self.lut=vtk.vtkLookupTable()
        self.lut.SetNumberOfColors(256)
        self.lut.SetTableRange(data_reader.get_scalar_range())
        self.lut.SetHueRange(0,1)
        self.lut.SetRange(data_reader.get_scalar_range())
        self.lut.Build()
        self.actor= vtk.vtkScalarBarActor()
        self.actor.SetOrientationToVertical()
        self.actor.SetPosition( 0.9, 0.77-0.25*scalar_bar_number)
        self.actor.SetPosition2( 0.09, 0.24 )
        self.propT = vtk.vtkTextProperty()
        self.propL = vtk.vtkTextProperty()
        self.propT.SetFontFamilyToArial()
        self.propT.SetColor(0.5,0.5,0.5)
        self.propT.ItalicOff()
        self.propT.BoldOn()
        self.propL.BoldOff()
        self.actor.SetLookupTable(self.lut)
