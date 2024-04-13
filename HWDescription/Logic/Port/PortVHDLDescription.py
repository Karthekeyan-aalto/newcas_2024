"""
Created by Karthekeyan Periasamy
Edited on Jan 19, 10:42
"""

from HWDescription.Signals.SignalVHDLDescription import SignalVHDLDescription
from HWDescription.Logic.Port.PortHWDescription import PortHWDescription

class PortVHDLDescription(PortHWDescription):

    def __init__(self):
        super().__init__()
     
    
    @property
    def portType(self):
        return self._portType

    @portType.setter
    def portType(self,value):
        self._portType = value
        # check the portType
        if self._portType == 1:
            self.vhdlPortTypeName = "IN"
        elif self._portType == 2:
            self.vhdlPortTypeName = "OUT"
        elif self._portType == 3:
            self.vhdlPortTypeName = "IN"
    
   
    
    
    @property
    def vhdlPortIEEEName(self):
        if self._vhdlPortIEEEName == None:
            # if it is bus
            if self.isPortABus == True:
                # set the vhdlPortIEEE name
                self._vhdlPortIEEEName = "std_logic_vector"
            else:
                # set the vhdlPortIEEE name
                self._vhdlPortIEEEName = "std_logic"

        return self._vhdlPortIEEEName

    @vhdlPortIEEEName.setter
    def vhdlPortIEEEName(self,value):
        self._vhdlPortIEEEName = value

    @property
    def vhdlPortDeclarationClosure(self):
        if self._vhdlPortDeclarationClosure == None:
            # if it is of output port
            if self._portType == 2 :
                # set the declaration closure as just a str
                self._vhdlPortDeclarationClosure = "(" + self.vhdlHWSignalDescription.vhdlSignalNumberOfBitsGenericName + "-1" + " " + "DOWNTO" + " " + "0" + ")" + "\n"
            else:
                # check if the vhdlport is a bus or not
                if self.isPortABus == True:
                    self._vhdlPortDeclarationClosure = "(" + self.vhdlHWSignalDescription.vhdlSignalNumberOfBitsGenericName + "-1" + " " + "DOWNTO" + " " + "0" + ")" + ";" + "\n"
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
        
        # vhdlPortType name
        self.vhdlPortTypeName = None
        self.vhdlPortIEEEName = None
        # property to store the vhdl port declaration closure syntax
        # as the closure declaration syntax is not same
        # we will customise the getter and setter
        self._vhdlPortDeclarationClosure = None
        #property to store the signal
        self.vhdlPortDeclaration = None

    def connectHWVHDLPackages(self):
        # connect the hw signal packages
        self.vhdlHWSignalDescription = SignalVHDLDescription() 
    
    def configure(self):
        super().configure()
        
    def processHWGeneration(self):
        # make the information for the signal to be formed from the pythonHWInputPort that is suitable for testbench
        configurationDetails = dict()
        if self.constantSignalValue != None:
            configurationDetails = {"Name":self.name,"NumberOfBits":self.numberOfBits,"ConstantSignalValue":self.constantSignalValue}
        elif self.signalData != None:
            configurationDetails = {"Name":self.name,"NumberOfBits":self.numberOfBits,"SignalData":self.signalData}

        self.vhdlHWSignalDescription = SignalVHDLDescription()
        self.vhdlHWSignalDescription.configurationDetailsOfHWSignal = configurationDetails
        self.vhdlHWSignalDescription.configure()

    def process(self):
        self.processHWGeneration()
        self.vhdlHWSignalDescription.process()

    
    def perform(self):
        self.performHWGeneration()
    
    def performHWGeneration(self):
        self.vhdlHWSignalDescription.perform()
        #print("Hi")
        # generate port definition
        self.generatePortDeclaration()
        # generate port Signal
        self.generatePortSignal()
        # generate port TB Signal
        self.generatePortTBSignal()


    def generatePortDeclaration(self):
        # generate the port declaration
        # based on the number system
        #print("Port Name", self.name)
        #print("VHDLPort Type Name", self.vhdlPortTypeName)
        #print("VHDLPortIEEE Type Name", self.vhdlPortIEEEName)
        self.vhdlPortDeclaration = self.name + ":" + self.vhdlPortTypeName + " " + self.vhdlPortIEEEName + self.vhdlPortDeclarationClosure
        #print("Port Decleration", self.vhdlPortDeclaration)
    
    def generatePortSignal(self):
        # generate the port declaration
        # based on the number system
        self.vhdlPortSignal = self.vhdlHWSignalDescription.vhdlSignalDescription        

    def generatePortTBSignal(self):
        # generate the port TB Signal
        self.vhdlPortTBSignal = self.vhdlHWSignalDescription.vhdlSignalTBDescription

    def reset(self):
        self.resetProperties()
        self.resestHWVHDLPackages()

    def resetProperties(self):
        super().resetProperties()
         # vhdlPortType name
        self.vhdlPortTypeName = None
        self.vhdlPortIEEEName = None
        # property to store the vhdl port declaration closure syntax
        # as the closure declaration syntax is not same
        # we will customise the getter and setter
        self._vhdlPortDeclarationClosure = None
        #property to store the signal
        self.vhdlPortDeclaration = None
        self.vhdlPortSignal = None
        # property to store the vhdlPortTB Signal
        self.vhdlPortTBSignal = None

    
    def resetHWVHDLPackages(self):
        # connect the hw generic packages
        self.vhdlHWSignalDescription = SignalVHDLDescription()
    
    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()
