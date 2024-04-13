"""
Created by Karthekeyan Periasamy
Edited on June 16 11:04 AM
"""


class HWSystemCompilation():
    """
    This class represents the base properties for the LUT HW Description. It will also be the sub class of the operators hw description
    For now, only we have LUTs, in the future we will implement blocks or operators 
    that will be used by the OPerations entity to implement complex systems
    """

    def __init__(self):
        self.connect()
  
        
    """
    # Start: hwDesignLibraryCreateCommand getters
    """

    @property
    def hwDesignLibraryCreateCommand(self):
        if self._hwDesignLibraryCreateCommand == None:
            self._hwDesignLibraryCreateCommand = "vlib"

        return self._hwDesignLibraryCreateCommand

    @hwDesignLibraryCreateCommand.setter
    def hwDesignLibraryCreateCommand(self,value):
        self._hwDesignLibraryCreateCommand = value       
    
    """
    # End: hwDesignLibraryCreateCommand setters and getters
    """
    
    

    def connect(self):
        self.connectProperties()

    def connectProperties(self):
        # design libraries properties
        self.hwDesignLibraries = None
        self._hwDesignLibraryCreateCommand = None
        self.hwName = None
        self.hwLocationInFileSystem = None
        self.configurationDetails = None

    def main(self):
        pass
    
    def configure(self):
        if self.configurationDetails == None:
            return

        configurationDetails = self.configurationDetails

        if "HWName" in configurationDetails:
            self.hwName = configurationDetails["HWName"]

        if "HWDesignLibraries" in configurationDetails:
            self.hwDesignLibraries = configurationDetails["HWDesignLibraries"]



    def process(self):
        pass

    def reset(self):
        self.resetProperties()

    def resetProperties(self):
         # design libraries properties
        self.hwDesignLibraries = None
        self._hwDesignLibraryCreateCommand = None
        self.hwFileName = None
        self.hwFileLocation = None
        self.configurationDetails = None


    def run(self):
        pass
