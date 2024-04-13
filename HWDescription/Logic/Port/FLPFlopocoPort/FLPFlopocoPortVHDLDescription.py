"""
Created by Karthekeyan Periasamy
Edited on December 08, 08:51
"""

from HWDescription.Signals.FLPSignal.FLPFlopocoSignalVHDLDescription import FLPFlopocoSignalVHDLDescription
from HWDescription.Logic.Port.PortVHDLDescription import PortVHDLDescription

class FLPFlopocoPortVHDLDescription(PortVHDLDescription):

    def __init__(self):
        super().__init__()
    
    
    @property
    def vhdlPortDeclarationClosure(self):
        if self._vhdlPortDeclarationClosure == None:
            # if it is of output port
            if self._portType == 2 :
                # set the declaration closure as just a str
                self._vhdlPortDeclarationClosure = "(" + "(" + self.vhdlHWSignalDescription.vhdlSignalFlopocoBitsGenericName + "+" + "(" +  self.vhdlHWSignalDescription.vhdlSignalMantissaBitsGenericName + "-1"+ ")"+  "+" + "(" + self.vhdlHWSignalDescription.vhdlSignalExponentBitsGenericName + ")" + " " + "DOWNTO" + " " + "0" + ")" + ")" + "\n"

            else:
                # check if the vhdlport is a bus or not
                if self.isPortABus == True:
                    self._vhdlPortDeclarationClosure = "(" + "(" + self.vhdlHWSignalDescription.vhdlSignalFlopocoBitsGenericName + "+" + "(" + self.vhdlHWSignalDescription.vhdlSignalMantissaBitsGenericName + "-1"+ ")"+  "+" + "(" + self.vhdlHWSignalDescription.vhdlSignalExponentBitsGenericName + ")" + " " + "DOWNTO" + " " + "0" + ")" + ")" + "\n"
                else:
                    self._vhdlPortDeclarationClosure = ";" + "\n"

        return self._vhdlPortDeclarationClosure

    @vhdlPortDeclarationClosure.setter
    def vhdlPortDeclarationClosure(self,value):
        self._portVHDLDeclarationClosure = value
       
    
    def connect(self):
        self.connectProperties()
        self.connectHWVHDLPackages()
    
    def connectProperties(self):
        super().connectProperties()
        
        # property to store the vhdl port declaration closure syntax
        # as the closure declaration syntax is not same
        # we will customise the getter and setter
        self._vhdlPortDeclarationClosure = None
        #property to store the signal
        self.vhdlPortDeclaration = None

    def connectHWVHDLPackages(self):
        # connect the hw signal packages
        self.vhdlHWSignalDescription = FLPFlopocoSignalVHDLDescription() 
    
    def configure(self):
        super().configure()
        
    def processHWGeneration(self):
        # make the information for the signal to be formed from the pythonHWInputPort that is suitable for testbench
        configurationDetails = dict()
        if self.constantSignalValue != None:
            configurationDetails = {"Name":self.name,"NumberOfBits":self.numberOfBits,"MantissaBits":self.mantissaBits, "ExponentBits":self.exponentBits,"FlopocoBits":self.numberOfBits,"ConstantSignalValue":self.constantSignalValue}
        elif self.signalData != None:
            configurationDetails = {"Name":self.name,"NumberOfBits":self.numberOfBits,"MantissaBits":self.mantissaBits, "ExponentBits":self.exponentBits,"FlopocoBits":self.numberOfBits,"SignalData":self.signalData}

        #print("Configuration Details of Port Signal", configurationDetails)
        self.vhdlHWSignalDescription = FLPFlopocoSignalVHDLDescription()
        self.vhdlHWSignalDescription.configurationDetailsOfHWSignal = configurationDetails
        self.vhdlHWSignalDescription.configure()

    def process(self):
        self.processHWGeneration()
        self.vhdlHWSignalDescription.process()

    
    def perform(self):
        self.performHWGeneration()
    
    def performHWGeneration(self):
        super().performHWGeneration()

   
    def reset(self):
        self.resetProperties()
        self.resestHWVHDLPackages()

    def resetProperties(self):
        super().resetProperties()

    
    def resetHWVHDLPackages(self):
        # connect the hw generic packages
        self.vhdlHWSignalDescription = FLPFlopocoSignalVHDLDescription()
    
    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()
