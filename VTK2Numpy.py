class VTK2Numpy:

    def __init__(self,file_url):
        self.plot_data =[]
        self.file=open(file_url,'r')
        print("VTK2Numpy")		
		
    def get_array(self):

        for line in self.file:
            if line.rfind('DIMENSIONS')!=-1:
                self.plot_data.append(line)
            if line.rfind('SPACING')!=-1:
				self.plot_data.append(line)
            if line.rfind('COLOR_SCALARS scalars 1')!=-1:
                for line in self.file:
                    arr=line.split(' ',3)
                    if arr[0]=='\n':   #jezeli linia jest pusta to nic nie rob
                        break
                    for elem in arr:       #wpisuj elementy po kolei do tablicy, jesli element to '\n' to nie wpisuj
                        if elem!='\n':
                            self.plot_data.append(elem)

        #print self.plot_data
        self.file.close()
        return self.plot_data
        
        
					

    def write_to_file(self,output_file,data):
        self.outf=open(output_file,'w')
        self.outf.seek(0)
        self.ii=0
        for elem in data:
            self.ii+=1
            self.outf.write(elem)
            self.outf.write('\n')
        self.outf.close()
