import vtk
from Rendered_Object import *
#from Abstract_Dot import *
from Specialized_Dot import *
class Layers_Dots(Rendered_Object, Abstract_Dot):
    
    typy="tk_SF tk_PS tk_CZ tk_SZ tk_ST tk_SS tk_WL tk_PW tk_WS tk_GR"
    warstwy="Warstwy2d Warstwy2D Warstwa2d Warstwa2D"
    numer_linii=0
    name="Layers_Dots"
    
    def __init__(self,data_reader,source_file):
        #self.WhoAmI="QuantumDot "+volume.introduction()
        self.DotDataFile=source_file
        self.DotData=open(self.DotDataFile,'r')
        #znajdz ilosc warstw
        self.ilosc_warstw=int(self.get_variable(self.DotData,'ilosc warstw'))
        self.lista_skladowych_struktury=[]
        self.okresl_kropki_i_warstwy(data_reader)
			
			
    def znajdz_koniec_opisu_kropki(self,DaneKropki):
		zestaw_typow=self.typy.split()
		for line in DaneKropki:
			line_words=(line.split()[0]).split()
			if zestaw_typow.intersection(line_words):
				return 1
	        
    def okresl_kropki_i_warstwy(self,data_reader):
        self.list_of_component_actors=[]
        i=0
        self.DotData.seek(0)      # czytam od zera dane, by nie okazalo sie ,ze dane kropki byly nad danymi warstw
        for line in self.DotData:             #przechodze do lini w ktorej ostatniowykrylem kropke, jesli wczsniej nie wykrylem to szukam od linii nr 0
			if i== self.numer_linii:
				break 
			i=+1
        print 'rozpoczalem czytanie odlinii  ' ,i
                                                  #funkcja czyta linia po linii plik i  szuka frazy okreslajcej
        zestaw_typow=set(self.typy.split())           #rodzaj kropki , gdy znajdzie ,zaczyna wczytywac linie w ktorych zapisane sa cechy  
                                             #kropki , gdy znajdzie deklaracje kolejnej kropki lub warstwy , pusta linie, EOF 
        for line in self.DotData:                  #to konczy dzialanie
            if set(self.warstwy.split()).intersection(line.split()):
                print "znalazlem napis Warstwy2d"
                for line in self.DotData:   #wczytuje liczbe warstw
                    self.liczba_warstw=int(line.split("#")[0])
                    break
                print "ilosc warstw to " ,self.liczba_warstw
                # jesli wystepuja jakies warstwy to wczytuje ich parametry
                if self.liczba_warstw>0:
                    for k in range(self.liczba_warstw):
						self.list_of_component_actors.append(Layer(self.wczytaj_linie(3,self.DotData),data_reader))
            i=+1
            word=(line.split('#')[0]).split()
            #teraz szuka czy wystepuja jakies kropki
            if zestaw_typow.intersection(word):
                self.typ_obiektu = word[0]        # znajduje rodzaj kropki
                #tu teraz bedzie wielki if , bo dla roznych kropek, rozna ilosc linii musi byc czytana
                if self.typ_obiektu=="tk_SF" or self.typ_obiektu=="tk_PS":
                    self.list_of_component_actors.append(tk_SF(self.wczytaj_linie(5, self.DotData)))
                    print "znalazalem %s", self.typ_obiektu
                if self.typ_obiektu=="tk_CZ":
					#self.list_of_component_actors.append(tk_CZ(self.wczytaj_linie(6,self.DotData)))
                    print "znalazalem %s", self.typ_obiektu
                if self.typ_obiektu=="tk_SZ" or self.typ_obiektu=="tk_ST":
				    self.wczytaj_linie(5,self.DotData)
                if self.typ_obiektu=="tk_SS":
			        self.list_of_component_actors.append(tk_SS(self.wczytaj_linie(6,self.DotData))) 
                if self.typ_obiektu=="tk_WL":
                    print "znalazalem %s", self.typ_obiektu
                    self.list_of_component_actors.append(tk_WL(self.wczytaj_linie(5,self.DotData)))
                    
                if self.typ_obiektu=="tk_PW":
                    self.wczytaj_linie(5,self.DotData)
                if self.typ_obiektu=="tk_WS" or self.typ_obiektu=="tk_GT":
                    self.wczytaj_linie(6,self.DotData)
                if self.typ_obiektu=="tk_GR":
                    self.wczytaj_linie(6,self.DotData)
			        

    def wczytaj_linie(self,n,DotData):
		# wczytaj 3 linie - dla kazdej kropki i wyluskaj dane
        tryb_srodek_numer=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        j=0
        for line in DotData:                   
            line_words=(line.split('#')[0]).split()  #dzieli linie na czlon danych i komentarza i przypisuje podzielone dane zmiennej 
            dane_w_linii=line.split('#')[0] # przypisuje zmiennej stringa zawierajacego dane w linii

            dane=dane_w_linii.split()
            #print "dane w linii    " ,dane_w_linii , "   dane    ",dane 
            if len(dane)>=1:
                tryb_srodek_numer[j][0]=dane[0]
            if len(dane)>=2:
                tryb_srodek_numer[j][1]=dane[1]
            if len(dane)>=3:
                tryb_srodek_numer[j][2]=dane[2]
            j=j+1
            if j==n:
                break
        #print j," linie ",tryb_srodek_numer
        return tryb_srodek_numer
        
    def get_list_of_component_actors(self):
		return self.list_of_component_actors
