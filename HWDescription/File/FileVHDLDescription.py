"""
Created by Karthekeyan Periasamy
Created on Sep 26 13:23
"""

from HWDescription.File.FileHWDescription import FileHWDescription

class FileVHDLDescription(FileHWDescription):
    

    def __init__(self):
        super().__init__()   
    
    
    
    @property
    def vhdlFileDeclarationClosure(self):
        if self._vhdlFileDeclarationClosure == None:
            self._vhdlFileDeclarationClosure = ";" + "\n"
 
        return self._vhdlFileDeclarationClosure

    @vhdlFileDeclarationClosure.setter
    def vhdlFileDeclarationClosure(self,value):
        self._vhdlFileDeclarationClosure = value

    @property
    def vhdlFileInitialisation(self):
        if self._vhdlFileInitialisation == None:
            self._vhdlFileInitialisation = str()
            
        return self._vhdlFileInitialisation

    
    @vhdlFileInitialisation.setter
    def vhdlFileInitialisation(self,value):
        self._vhdlFileInitialisation = value
    
    
    def configure(self):
        super().configure()

        if self.configurationDetailsOfHWFile == None:
            return

        configurationDetails = self.configurationDetailsOfHWFile
        #print("Configuration Details of File", configurationDetails)

        if "Type" in configurationDetails:
            self.vhdlFileIEEEName = configurationDetails["Type"]

        
    
    def connect(self):
        self.connectProperties()


    def connectProperties(self):
        super().connectProperties()
        self.vhdlFileIEEEName = None
        self._vhdlFileDeclarationClosure = None
        self._vhdlFileInitialisation = None
        self.vhdlDescription = None


    def generateVHDLFile(self):

        self.vhdlDescription = "File" + " " + self.name + " " + ":" + self.vhdlFileIEEEName + " " + "OPEN" + " " + self.modeName + " " + "is" + " " + "\"" + self.fileName + "." + self.fileExtension + "\"" + self.vhdlFileDeclarationClosure
        
        self.vhdlFileCloseDescription = "file_close" + " " + "(" + self.name + ")" + ";" + "\n"
    
    def process(self):
        pass

    def perform(self):
        # generate the signal with signal information
        self.generateVHDLFile()
    
    def reset(self):
        self.resetProperties()


    def resetProperties(self):
        super().resetProperties()
        self.vhdlDescription = None
        self.vhdlFileIEEEName = None
        self._vhdlFileDeclarationClosure = None
        self._vhdlFileInitialisation = None
        self.vhdlFileCloseDescription = None

    def run(self):
        self.main()


