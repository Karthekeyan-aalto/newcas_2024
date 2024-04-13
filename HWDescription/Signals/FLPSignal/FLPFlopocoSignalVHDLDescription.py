"""
Created by Karthekeyan Periasamy
Created on Jan 27 09:38
"""

from HWDescription.Signals.SignalVHDLDescription import SignalVHDLDescription

class FLPFlopocoSignalVHDLDescription(SignalVHDLDescription):
    

    def __init__(self):
        super().__init__()


    def connect(self):
        self.connectProperties()

    def connectProperties(self):
        super().connectProperties()
        self._vhdlSignalFlopocoBitsGenericName = None
        self._vhdlSignalFlopocoBitsGenericName = None
    
    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        super().resetProperties()
        self._vhdlSignalFlopocoBitsGenericName = None
        self._vhdlSignalFlopocoBitsGenericName = None


    """
    Custom Getters and Setters
    """
    @property
    def vhdlSignalInitialisation(self):
        if self._vhdlSignalInitialisation == None:
            if self.signalData != None:
                if self.isSignalABus == True:
                    self._vhdlSignalInitialisation = ":=" + " " + "to_slv"+ "(" + "to_float"+ "("+ str(float(self.signalData)) + "," + "exponentBits"+","+ "mantissaBits-1"+")" + ")" + ";" + "\n"
                else:
                    # set the signal initialisation
                    self._vhdlSignalInitialisation = ":=" + " " + "'" + str(self.signalData) + "'" + ";" + "\n"
                
            else:
                # set the signal initialisation
                self._vhdlSignalInitialisation = ""

        return self._vhdlSignalInitialisation
            

    @vhdlSignalInitialisation.setter
    def vhdlSignalIntialisation(self,value):
        self._vhdlSignalIntialisation = value

    @property
    def vhdlSignaFlopocoBitsGenericName(self):
        if self._vhdlSignalFlopocoBitsGenericName == None:
            self._vhdlSignalFlopocoBitsGenericName = "FlopocoBits"

        return self._vhdlSignalFlopocoBitsGenericName

    
    @vhdlSignaFlopocoBitsGenericName.setter
    def vhdlSignaFlopocoBitsGenericName(self,value):
        self._vhdlSignalFlopocoBitsGenericName = value

    @property
    def vhdlSignalDeclarationClosure(self):
        if self._vhdlSignalDeclarationClosure == None:
            if self.signalData != None:
                # check if the vhdlport is a bus or not
                if self.isSignalABus == True:
                    #self._vhdlSignalDeclarationClosure = self._vhdlSignalDeclarationClosure = "(" + "(" + self.vhdlSignalFlopocoBitsGenericName + "+" + "(" +  self.vhdlSignalMantissaBitsGenericName + "-1"+ ")"+  "+" + "(" + self.vhdlSignalExponentBitsGenericName + ")" + " " + "DOWNTO" + " " + "0" + ")" + ")" + ";" + "\n"
                    self._vhdlSignalDeclarationClosure = "(" + self.vhdlSignalNumberOfBitsGenericName + "-1" + " " + "DOWNTO" + " " + "0" + ")"
                else:
                    # check if the constant signal value is set or not
                    # if the constant signal value is set, we do not need the closure
                    # as the closure is taken care by the signal initialisation
                    
                    #print("Constant Signal Value is not None")
                    #if self.constantSignalValue == None:
                    self._vhdlSignalDeclarationClosure = ";" + "\n"
                    #else:
                        #print("Constant Signal Value is not None")
                        #self._vhdlSignalDeclarationClosure = ""
                        
            else:
                # check if the vhdlport is a bus or not
                if self.isSignalABus == True:
                    self._vhdlSignalDeclarationClosure = self._vhdlSignalDeclarationClosure = "(" + self.vhdlSignalFlopocoBitsGenericName + "+" + "(" +  self.vhdlSignalMantissaBitsGenericName + "-1"+ ")"+  "+" + "(" + self.vhdlSignalExponentBitsGenericName + ")" + " " + "DOWNTO" + " " + "0" + ")" + ";" + "\n"       
                else:
                    # set the signal initialisation
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




