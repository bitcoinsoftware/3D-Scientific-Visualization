import vtk
class Color_Function:
    def make_color_function(self,scalar_range):
        max_scalar=scalar_range[1]
        min_scalar=scalar_range[0]
        # Create transfer mapping scalar value to opacity
        self.opacityTransferFunction=vtk.vtkPiecewiseFunction()     
        self.opacityTransferFunction.AddPoint(max_scalar/5.0,0.03)
        self.opacityTransferFunction.AddPoint(max_scalar*0.7,1)
        self.opacityTransferFunction.AddPoint(max_scalar,1)
        # Create transfer mapping scalar value to color
        self.colorTransferFunction=vtk.vtkColorTransferFunction()
        self.colorTransferFunction.AdjustRange(scalar_range)     
        self.colorTransferFunction.SetScale(100)

        self.colorTransferFunction.AddRGBPoint(min_scalar,0.0,0.0,1.0)
        self.colorTransferFunction.AddRGBPoint(max_scalar,1.0,0.0,0.0)
        self.colorTransferFunction.SetColorSpaceToRGB()
        self.colorTransferFunction.SetScaleToLinear()
        # Create transfer mapping scalar value to opacity based on gradient magnitude
        self.gradientTransferFunction=vtk.vtkPiecewiseFunction()
        self.gradientTransferFunction.AddPoint(min_scalar,0.01)
        self.gradientTransferFunction.AddPoint(max_scalar*0.7,1.0)
