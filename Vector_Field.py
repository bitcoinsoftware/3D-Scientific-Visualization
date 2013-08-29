from Rendered_Object import *
import vtk

class Vector_Field(Rendered_Object):
    name ="Vector Field"
    def __init__(self,data_reader):
        self.lut=vtk.vtkLookupTable()
        self.lut.SetNumberOfColors(256)

        self.lut.SetTableRange(data_reader.get_scalar_range())
        self.lut.SetHueRange(0,1)
        self.lut.SetRange(data_reader.get_scalar_range())
        self.lut.SetRange(data_reader.get_scalar_range())
        self.lut.Build()

        self.arrow=vtk.vtkArrowSource()
        self.arrow.SetTipResolution(6)
        self.arrow.SetTipRadius(0.1)
        self.arrow.SetTipLength(0.35)
        self.arrow.SetShaftResolution(6)
        self.arrow.SetShaftRadius(0.03)
        
        self.glyph=vtk.vtkGlyph3D()

        self.glyph.SetInput(data_reader.get_data_set())
        self.glyph.SetSource(self.arrow.GetOutput())
        self.glyph.SetVectorModeToUseVector()
        self.glyph.SetColorModeToColorByScalar()
        self.glyph.SetScaleModeToScaleByVector()
        self.glyph.OrientOn()
        self.glyph.SetScaleFactor(0.002)
		
        mapper=vtk.vtkPolyDataMapper()
        mapper.SetInput(self.glyph.GetOutput())
        mapper.SetLookupTable(self.lut)
        mapper.ScalarVisibilityOn()
        mapper.SetScalarRange(data_reader.get_scalar_range())
        self.actor=vtk.vtkActor()
        self.actor.SetMapper(mapper)	
