"""
Created by Karthekeyan Periasamy
Edited on Sep 26 13:13
"""

class FileHWDescription():

    def __init__(self):
        self.connect()
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        # check if the signal value is none or not
        self._name = value
    
    @property
    def modeName(self):
        return self._modeName

    @modeName.setter
    def modeName(self,value):
        self._modeName = value

        if self._modeName == "read_mode":
            self.mode = 1
        elif self._modeName == "write_mode":
            self.mode = 2

    
    def connect(self):
        self.connectProperties()

    def connectProperties(self):
        # property to store the name of the variable
        self.name = None
        # property to store the file name
        self.fileName = None
        # property to store the mode of the file
        # here mode is an integer can be either 1 or 0
        # 1 means write mode
        # 0 means read mode
        self._modeName = None
        # property to store the mode in terms of the number
        self.mode = None

    
    def configure(self):
        # check if the configuration details are there or not
        if self.configurationDetailsOfHWFile == None:
            return
        
        # store the configuraiton details to a local variable
        configurationDetails = self.configurationDetailsOfHWFile
        
        # check if the name key is available in the configuration details
        if "Name" in configurationDetails:
            self.name = configurationDetails["Name"]

        # check if the file name key exist or not
        if "FileName" in configurationDetails:
            self.fileName = configurationDetails["FileName"]
        
        # check if the mode exists or not
        if "Mode" in configurationDetails:
            self.modeName = configurationDetails["Mode"]
        
        if "FileExtension" in configurationDetails:
            self.fileExtension = configurationDetails["FileExtension"]
    
    
    def perform(self):
        pass

    def process(self):
        pass

    def main(self):
        self.process()
        self.perform()

    def reset(self):
        self.resetProperties()


    def resetProperties(self):
        # property to store the name of the variable
        self.name = None
        # property to store the file name
        self.fileName = None
        # property to store the mode of the file
        # here mode is an integer can be either 1 or 0
        # 1 means write mode
        # 0 means read mode
        self._modeName = None
        # property to store the mode in terms of the number
        self.mode = None

    def run(self):
        self.main()

