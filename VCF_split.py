class VCF_split:
    def __init__(self):
        self.filename='backup.dat'
        self.fileNumber=0
    
    def split(self):
        sourceFile = open(self.filename, 'r')
        newFile = None
        
        for line in sourceFile.readlines():
            if line.strip() == '':
                continue
            
            elif line.find('BEGIN') >= 0:
                newFile = self.openFile(line)
            
            elif line.find('END') >= 0:
                self.closeFile(newFile, line)
            
            else:
                newFile.write(line)
        
    def openFile(self, line):
        newFile = open(self.fileNumber.__str__() + ".vcf", 'w')
        newFile.write(line)
        return newFile
    
    def closeFile(self, newFile, line):
        newFile.write(line)
        newFile.close()
        self.fileNumber += 1
        
if __name__ == '__main__':
    vcf = VCF_split()
    vcf.split()
    