import vtk
from Rendered_Object import *
from Slicing_Matrix import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import *
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from VTK2Numpy import *



class MatPlot3d(Rendered_Object,Slicing_Matrix):
    def __init__(self,data_reader,origin,normal,camera_normal):
		
        self.axial=self.get_matrix(data_reader,origin,normal,camera_normal)
        print("MatPlot3d constructor")
        self.reslice = vtk.vtkImageReslice()
        self.reslice.SetInput(data_reader.get_data_set())
        #self.axial=self.get_matrix(volume,origin,normal)
        
        self.reslice.SetOutputDimensionality(2)
        self.reslice.SetResliceAxes(self.axial)
        self.reslice.SetInterpolationModeToLinear()
        
        # Create a colorscale lookup table
        self.lut=vtk.vtkLookupTable()
        self.lut.SetNumberOfColors(256)

        self.lut.SetTableRange(data_reader.get_scalar_range())
        self.lut.SetRange(data_reader.get_scalar_range())

        self.lut.SetHueRange(0,1)
        self.lut.Build()
        
        # Map the image through the lookup table
        self.color = vtk.vtkImageMapToColors()
        self.color.SetLookupTable(self.lut)
        self.color.SetInputConnection(self.reslice.GetOutputPort())
        
        filename='./temp/temp'
        self.writer=vtk.vtkDataSetWriter()
        self.writer.SetInput(self.reslice.GetOutput())
        
        self.writer.SetFileName(filename)
        self.writer.Write() 
        #self.file=open(self.filename,'r')
        
        converter=VTK2Numpy(filename)
        array=converter.get_array()
        
        self.dim_nx=0
        self.dim_ny=0  
        Z=[]
        row=[]
        i=0
        for elem in array:
            if elem.rfind('DIMENSIONS')!=-1:
                temp=elem.split(' ',4)
                self.dim_nx=(eval(temp[1]))
                self.dim_ny=(eval(temp[2]))
            elif elem.rfind('SPACING')!=-1:        #pomijaj slowa 
			    continue
            else:
                if elem!='\n':
                    i=i+1
                    row.append(eval(elem))
                if i==self.dim_nx:	
                    Z.append(row)
                    row=[]
                    i=0  
                     
        fig = plt.figure()
        ax = Axes3D(fig)
        X = np.arange(0,self.dim_nx,1)
        Y = np.arange(0,self.dim_ny,1)
        Zpl = np.abs(Z)
        X, Y = np.meshgrid(X, Y)
        surf = ax.plot_surface(X, Y, Zpl, rstride=1, cstride=1, cmap=cm.jet,linewidth=1, antialiased=True)
        ax.set_zlim3d(-1.01, 1.01)
        fig.colorbar(surf, shrink=0.5, aspect=10)
        plt.show()
        self.dim_nx=0
        self.dim_ny=0
        #self.Z=[]
        Z=[]
        Zpl=[]
        

        
        
        
        
        
