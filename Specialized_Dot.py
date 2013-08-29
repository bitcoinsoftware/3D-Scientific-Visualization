from Abstract_Dot import *

class Layer(Abstract_Dot):
    name = "Layer"
    def __init__(self,cechy,data_reader):
        poczatek=float(cechy[2][0])
        grubosc=float(cechy[2][1])
        substancja=int(cechy[1][0])
        srodek=data_reader.get_center()
        srodek=[srodek[0],srodek[1],(poczatek+grubosc)/2.0]
        source = vtk.vtkCubeSource()
        #source.SetHeight(wysokosc)
        source.SetCenter(srodek)
        bounds = data_reader.get_bounds()
        print bounds
        source.SetXLength(10)
        source.SetYLength(10)
        source.SetZLength(grubosc)

        sourceMapper = vtk.vtkPolyDataMapper()
        sourceMapper.SetInput(source.GetOutput())

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(sourceMapper)
		

class tk_SF(Abstract_Dot):
#sfera lub polsfera
    name = "tk_SF"
    def __init__(self,cechy):
        srodek = (float(cechy[1][0]),float(cechy[1][1]),float(cechy[1][2]))
        substancja = float(cechy[2][0])
        promien = [float(cechy[3][0]),float(cechy[3][1]),float(cechy[3][2])]
        wysokosc_sciecia = float(cechy[3][3])
        obrot = float(cechy[5][0])
        #print self.name , srodek , substancja , podstawa , wysokosc , obrot
        #self.znajdz_srodek_i_numer_warstwy(cechy)
        #wys_sciecia_stozka=self.get_variable(cechy,"wysokosc stozka scietego")
        #podstawaXYZ=self.get_many_variables(cechy,"pods_X, Y i Z")
        source = vtk.vtkSphereSource()
        #source.SetHeight(wysokosc)
        source.SetCenter(srodek)
        source.SetRadius(promien[0])

        sourceMapper = vtk.vtkPolyDataMapper()
        sourceMapper.SetInput(source.GetOutput())

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(sourceMapper)
		
class tk_SZ(Abstract_Dot):
#szescian
	def __init__(self,typ,cechy,volume):
		print "Jestem %s",(typ)
		self.znajdz_srodek_i_numer_warstwy(cechy)
		podstawaXYZ=self.get_many_variables(cechy,"pods_X, Y i Z")
		
class tk_ST(Abstract_Dot):
#stozek
	def __init__(self,typ,cechy,volume):
		print "Jestem %s",(typ)
		self.znajdz_srodek_i_numer_warstwy(cechy)
		podstawaXYZ=self.get_many_variables(cechy,"pods_X, Y i Z")
		
class tk_SS(Abstract_Dot):
    name = "tk_SS"
#stozek sciety
    def __init__(self,cechy):
        srodek = (float(cechy[1][0]),float(cechy[1][1]),float(cechy[1][2]))
        substancja = float(cechy[2][0])
        podstawa = [float(cechy[3][0]),float(cechy[3][1]),float(cechy[3][2])]
        wysokosc = float(cechy[4][0])
        obrot = float(cechy[5][0])
        #print self.name , srodek , substancja , podstawa , wysokosc , obrot
        #self.znajdz_srodek_i_numer_warstwy(cechy)
        #wys_sciecia_stozka=self.get_variable(cechy,"wysokosc stozka scietego")
        #podstawaXYZ=self.get_many_variables(cechy,"pods_X, Y i Z")
        source = vtk.vtkConeSource()
        source.SetHeight(wysokosc)
        source.SetCenter(srodek)
        source.SetRadius(podstawa[0])
        source.SetCapping(1)
        source.SetResolution(16)

        sourceMapper = vtk.vtkPolyDataMapper()
        sourceMapper.SetInput(source.GetOutput())

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(sourceMapper)
        

	    
	    
class tk_WL(Abstract_Dot):
#walec
    name="tk_WL"
    def __init__(self,cechy):
        srodek = (float(cechy[1][0]),float(cechy[1][1]),float(cechy[1][2]))
        substancja = float(cechy[2][0])
        podstawa = float(cechy[3][0])
        wysokosc = float(cechy[3][1])
        obrot = float(cechy[4][0])
        #print self.name , srodek , substancja , podstawa , wysokosc , obrot
        #self.znajdz_srodek_i_numer_warstwy(cechy)
        #wys_sciecia_stozka=self.get_variable(cechy,"wysokosc stozka scietego")
        #podstawaXYZ=self.get_many_variables(cechy,"pods_X, Y i Z")
        source = vtk.vtkCylinderSource()
        source.SetHeight(wysokosc)
        source.SetCenter(srodek)
        source.SetRadius(podstawa)
        #source.SetCapping(1)
        source.SetResolution(16)

        sourceMapper = vtk.vtkPolyDataMapper()
        sourceMapper.SetInput(source.GetOutput())

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(sourceMapper)
        
class tk_CZ(Abstract_Dot):
#walec
    name="tk_CZ"
    def __init__(self,cechy):
        srodek = (float(cechy[1][0]),float(cechy[1][1]),float(cechy[1][2]))
        substancja = float(cechy[2][0])
        podstawa = float(cechy[3][0])
        wysokosc = float(cechy[3][1])
        obrot = float(cechy[4][0])
        #print self.name , srodek , substancja , podstawa , wysokosc , obrot
        #self.znajdz_srodek_i_numer_warstwy(cechy)
        #wys_sciecia_stozka=self.get_variable(cechy,"wysokosc stozka scietego")
        #podstawaXYZ=self.get_many_variables(cechy,"pods_X, Y i Z")
        source = vtk.vtkPlatonicSolidSource()
        #source.SetHeight(wysokosc)
        source.SetSolidTypeToTetrahedron()
        #source.SetCenter(srodek)

        sourceMapper = vtk.vtkPolyDataMapper()
        sourceMapper.SetInput(source.GetOutput())

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(sourceMapper)
        
class tk_WS(Abstract_Dot):
#walec sciety
	def __init__(self,typ,cechy,volume):
	    self.znajdz_srodek_i_numer_warstwy(cechy)
	    wysokosc=self.get_variable(cechy,"wysokosc walca")
	    cieciwa_i_wys_obciecia=self.get_variable(cechy,"cieciwa i wysokosc_obcieta  podstawy walca")
class tk_GT(Abstract_Dot):
#graniastoslup prosty o podstawie trojkata
    def __init__(self,typ,cechy,volume):
        self.znajdz_srodek_i_numer_warstwy(cechy)
        wysokosc=self.get_variable(cechy,"wysokosc walca")
		
class tk_GR(Abstract_Dot):
#graniastoslup prosty o podstawie rownolegloboku
    def __init__(self,typ,cechy,volume):
        self.znajdz_srodek_i_numer_warstwy(cechy)
        podstXY_kat_pomiedzy=self.get_many_variables(cechy,"podstawaX, podstawaY, kat miedzy bokami w stopniach")
