"""
Created by Karthekeyan Periasamy
Created on Jan 27 09:38
"""

from HWDescription.Signals.SignalVHDLDescription import SignalVHDLDescription

class FloatSignalVHDLDescription(SignalVHDLDescription):
    

    def __init__(self):
        super().__init__()
        # property to store the signal initialisation
        self._vhdlSignalInitialisation = None
        # property to store the vhdlDescription of the signal
        self.vhdlDescription = None

    """
    Custom Getters and Setters
    """
    @property
    def vhdlSignalInitialisation(self):
        if self._vhdlSignalInitialisation == None:
            if self.isSignalABus == True:
                self._vhdlSignalInitialisation = ":=" + " " + "to_slv"+ "(" + "to_float"+ "("+ str(float(self.constantSignalValue)) + "," + "exponentBits"+","+ "mantissaBits-1"+")" + ")" + ";" + "\n"
            else:
                # set the signal initialisation
                self._vhdlSignalInitialisation = ":=" + " " + "\'0\'" + ";" + "\n"

        return self._vhdlSignalInitialisation

    @vhdlSignalInitialisation.setter
    def vhdlSignalIntialisation(self,value):
        self._vhdlSignalIntialisation = value

    
    @property
    def vhdlSignalDeclarationClosure(self):
        if self._vhdlSignalDeclarationClosure == None:
            # check if the vhdlport is a bus or not
            if self.isSignalABus == True:
                self._vhdlSignalDeclarationClosure = "(" + self.vhdlSignalNumberOfBitsGenericName + "-1" + " " + "DOWNTO" + " " + "0" + ")" + ";" + "\n"
            else:
                # check if the constant signal value is set or not
                # if the constant signal value is set, we do not need the closure
                # as the closure is taken care by the signal initialisation

                #print("Constant Signal Value is not None")
                if self.constantSignalValue == None:
                    self._vhdlSignalDeclarationClosure = ";" + "\n"
                else:
                    #print("Constant Signal Value is not None")
                    self._vhdlSignalDeclarationClosure = ""

        return self._vhdlSignalDeclarationClosure

    @vhdlSignalDeclarationClosure.setter
    def vhdlSignalDeclarationClosure(self,value):
        self._vhdlSignalDeclarationClosure = value
    
    
    
    def perform(self):
        super().perform()
    
    def main(self):
        self.process()
        self.perform()

    def configure(self):
        super().configure()

    def process(self):
        super().process()
    
    def resetProperties(self):
        super().resetProperties()

    def reset(self):
        self.resetProperties()

    def run(self):
        self.main()

