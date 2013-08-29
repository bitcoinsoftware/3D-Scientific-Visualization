import vtk
from math import *
from Rendered_Object import *

class Slicing_Matrix:
    def get_matrix(self,data_reader,origin,normal,camera_normal):
        # do funkcji zostal dostarczony argument definiujacy polozenie kamery, 
        #oddaje ten argument w Panskie rece, bo sam nie wiem za bardzo co z nim zrobic
        #podejrzewam tylko ,ze musi on stanowic wartosc poczatkowa i trzeba go odjac lub dodac w odpowiednim przypadku
		# Calculate the center of the volume
        data_reader.get_data_set().UpdateInformation()
        (self.xMin,self.xMax,self.yMin,self.yMax,self.zMin,self.zMax) = data_reader.get_whole_extent()
        (self.xSpacing,self.ySpacing,self.zSpacing) = data_reader.get_spacing()
        (self.x0,self.y0,self.z0) = data_reader.get_origin()
        
        self.center = [self.x0 + self.xSpacing * 0.5 * (self.xMin + self.xMax),
        self.y0 + self.ySpacing * 0.5 * (self.yMin + self.yMax),
        self.z0 + self.zSpacing * 0.5 * (self.zMin + self.zMax)]
       # print self.center
        #-----------------------------
        c="c"     # TU jesli poda sie funkcji orgin postaci (c,c,c) to zrobi przeciecie przez srodek
        if origin[0]==c or origin[1]==c or origin[2]==c:
			origin=self.center
        
        origin=(float(origin[0]),float(origin[1]),float(origin[2]))

            
        self.axial = vtk.vtkMatrix4x4()
        if normal[0]=="p":   # jesli poda sie funkcji normal postaci (p,*,*) to zrobi prostopadla do tej osi
            self.axial.DeepCopy((0,0,1,origin[0],
			                     1,0,0,origin[1],
			                     0,1,0,origin[2],
			                     0,0,0,1))    
        elif normal[1]=="p":   # jesli poda sie funkcji normal postaci (*,p,*) to zrobi prostopadla do tej osi
			self.axial.DeepCopy((0,1,0,origin[0],
			                     0,0,1,origin[1],
			                     1,0,0,origin[2],
			                     0,0,0,1))
			
        elif normal[2]=="p":   # jesli poda sie funkcji normal postaci (*,*,p) to zrobi prostopadla do tej osi
			self.axial.DeepCopy((1,0,0,origin[0],
			                     0,1,0,origin[1],
			                     0,0,1,origin[2],
			                     0,0,0,1))
		
        else:  
            #zabezpieczenie przed nadmiernym liczeniem - i tak nie ma roznicy przy volumach 150x150x150 pkt , bo 150/10000 = 0 ;-) tzn. na brzegu voluma 
            #plaszczyzna i tak nie przetnie innego punktu (voxela) niz wlasciwy
            normal[0]=float(normal[0])
            normal[1]=float(normal[1])
            normal[2]=float(normal[2])
         
            e=0
            for dir in normal:
			    if dir==0:
				    normal[e]=0.0001
			    elif dir==1:
				    normal[e]=0.9999
			    e=e+1
	        #tu najprawdopodobniej jest blad w jakims minusie, albo sinus zamiast cos, moze wikipedia sie myli  
	        #http://pl.wikipedia.org/wiki/K%C4%85ty_Eulera
            self.Alfa=[acos(normal[0]),acos(normal[1]),acos(normal[2])]   # self.Alfa jest dla mnie normalna plaszczyzny ciecia wyrazona w stopniach tzn (kat_x,kat_y,kat_z) 
            self.SinAlfa=[sin(self.Alfa[0]),sin(self.Alfa[1]),sin(self.Alfa[2])] 
            self.i=[normal[0]*normal[2]-self.SinAlfa[0]*self.SinAlfa[1]*normal[1], self.SinAlfa[0]*normal[2]+normal[0]*self.SinAlfa[2]*normal[1],self.SinAlfa[2]*self.SinAlfa[1]]
            self.j=[-normal[0]*normal[2]-self.SinAlfa[0]*self.SinAlfa[1]*normal[1], -self.SinAlfa[0]*normal[2]-normal[0]*self.SinAlfa[1]*normal[1],normal[2]*self.SinAlfa[1]]
            self.k=[self.SinAlfa[1]*self.SinAlfa[1],-normal[0]*self.SinAlfa[2],normal[1]]
            #macierz obrotu - kat eulera w wikipedii
            #http://pl.wikipedia.org/wiki/K%C4%85ty_Eulera   - na dole jest macierz obrotu
            self.axial.DeepCopy((self.i[0], self.i[1], self.i[2], origin[0],
                                 self.j[0], self.j[1], self.j[2], origin[1],
                                 self.k[0], self.k[1], self.k[2], origin[2],
                                 0, 0, 0, 1))
        return self.axial
