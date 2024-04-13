"""
Created by Karthekeyan Periasamy
Created on Jan 24 14:11
"""

from HWDescription.Signals.SignalHWDescription import SignalHWDescription

class SignalVHDLDescription(SignalHWDescription):
    

    def __init__(self):
        super().__init__()
    
    def connect(self):
        self.connectProperties()
        self.connectHWVHDLPackages()
  
    """
    Custom Getters and Setters
    """
    
    @property
    def vhdlSignalNumberOfBitsGenericName(self):
        if self._vhdlSignalNumberOfBitsGenericName == None:
            self._vhdlSignalNumberOfBitsGenericName = "NumberOfBits"

        return self._vhdlSignalNumberOfBitsGenericName

    
    @vhdlSignalNumberOfBitsGenericName.setter
    def vhdlSignalNumberOfBitsGenericName(self,value):
        self._vhdlSignalNumberOfBitsGenericName = value
    
    @property
    def vhdlSignalMantissaBitsGenericName(self):
        if self._vhdlSignalMantissaBitsGenericName == None:
            self._vhdlSignalMantissaBitsGenericName = "MantissaBits"

        return self._vhdlSignalMantissaBitsGenericName

    
    @vhdlSignalMantissaBitsGenericName.setter
    def vhdlSignalMantissaBitsGenericName(self,value):
        self._vhdlSignalMantissaBitsGenericName = value
    
    @property
    def vhdlSignalExponentBitsGenericName(self):
        if self._vhdlSignalExponentBitsGenericName == None:
            self._vhdlSignalExponentBitsGenericName = "ExponentBits"

        return self._vhdlSignalExponentBitsGenericName

    
    @vhdlSignalExponentBitsGenericName.setter
    def vhdlSignalExponentBitsGenericName(self,value):
        self._vhdlSignalExponentBitsGenericName = value
        
    
    @property
    def vhdlSignalIEEEName(self):
        if self._vhdlSignalIEEEName == None:
            # check if signal is a bus
            if self.isSignalABus == True:
                # set the vhdl signal IEEE name
                self._vhdlSignalIEEEName = "std_logic_vector"
            else:
                # set the vhdl signal IEEE name
                self._vhdlSignalIEEEName = "std_logic"

        return self._vhdlSignalIEEEName

    
    @vhdlSignalIEEEName.setter
    def vhdlSignalIEEEName(self,value):
        self._vhdlSignalIEEEName = value

    @property
    def vhdlSignalDeclarationClosure(self):
        if self._vhdlSignalDeclarationClosure == None:
            if self.signalData != None:
                # check if the vhdlport is a bus or not
                if self.isSignalABus == True:
                    self._vhdlSignalDeclarationClosure = "(" + self.vhdlSignalNumberOfBitsGenericName + "-1" + " " + "DOWNTO" + " " + "0" + ")" + ";" + "\n"
                else:
                    # check if the constant signal value is set or not
                    # if the constant signal value is set, we do not need the closure
                    # as the closure is taken care by the signal initialisation
                    self._vhdlSignalDeclarationClosure = ";" + "\n"
            else:
                # check if the vhdlport is a bus or not
                if self.isSignalABus == True:
                    self._vhdlSignalDeclarationClosure = "(" + self.vhdlSignalNumberOfBitsGenericName + "-1" + " " + "DOWNTO" + " " + "0" + ")" + ";" + "\n"
                else:
                    # set the signal initialisation
                    self._vhdlSignalDeclarationClosure = "" + "\n"

        return self._vhdlSignalDeclarationClosure

    @vhdlSignalDeclarationClosure.setter
    def vhdlSignalDeclarationClosure(self,value):
        self._vhdlSignalDeclarationClosure = value
    
    
  
    @property
    def vhdlSignalInitialisation(self):
        if self._vhdlSignalInitialisation == None:
            if self.signalData != None:
                if self.isSignalABus == True:
                    self._vhdlSignalInitialisation = ":=" + " " + "(" + "others" + " " + "=>" + " " + "'" + str(self.signalData) + "'" + ")" + ";" + "\n"
                else:
                    # set the signal initialisation
                    self._vhdlSignalInitialisation = ":=" + " " + "'" + str(self.signalData) + "'" + ";" + "\n"
                
            else:
                #set the signal initialisation
                self._vhdlSignalInitialisation = "" + "\n"

        return self._vhdlSignalInitialisation

    @vhdlSignalInitialisation.setter
    def vhdlSignalIntialisation(self,value):
        self._vhdlSignalIntialisation = value

    @property
    def vhdlSignalTBInitialisation(self):
        if self._vhdlSignalTBIntialisation == None:
            if self.signalData != None:
                if self.isSignalABus == True:
                    self._vhdlSignalTBIntialisation = ":=" + " " + "(" + "others" + " " + "=>" + " " + "'" + str(self.constantSignalValue) + "'" + ")" + ";" + "\n"
                else:
                    # set the signal initialisation
                    self._vhdlSignalTBIntialisation = ":=" + " " + "'" + str(self.constantSignalValue) + "'" + ";" + "\n"
                
            else:
                # set the signal initialisation
                self._vhdlSignalTBIntialisation = "" + "\n"

        return self._vhdlSignalTBIntialisation

    @vhdlSignalTBInitialisation.setter
    def vhdlSignalTBIntialisation(self,value):
        self._vhdlSignalTBIntialisation = value

    def generateVHDLSignal(self):
        #print("VHDL Signal Name", self.name)
        self.vhdlSignalDescription = "SIGNAL" + " " + self.name + " " + ":" + self.vhdlSignalIEEEName + self.vhdlSignalDeclarationClosure + self.vhdlSignalInitialisation
        #print("VHDL Signal Description", self.name, self.vhdlSignalDescription)

    def generateVHDLTBSignal(self):
        # generate the port TB Signal
        self.vhdlSignalTBDescription = "SIGNAL" + " " + self.name + " " + ":" +  self.vhdlSignalIEEEName + self.vhdlSignalDeclarationClosure + self.vhdlSignalTBInitialisation


    def main(self):
        self.process()
        self.perform()

   
    def connectHWVHDLPackages(self):
        pass
    
    def connectProperties(self):
        super().connectProperties()
        # property to store the VHDL signal IEEE name
        self._vhdlSignalIEEEName = None
        # property to store the signal declaration closure
        self._vhdlSignalDeclarationClosure = None
        # proeprty to store the vhdl signal closure
        self._vhdlSignalClosure = None
        # property to store the signal initialisation
        self._vhdlSignalInitialisation = None
        self._vhdlSignalTBIntialisation = None
        self._vhdlSignalNumberOfBitsGenericName = None
        self._vhdlSignalMantissaBitsGenericName = None
        self._vhdlSignalExponentBitsGenericName = None
        self.vhdlSignalDescription = None
        self.vhdlSignalTBDescription = None


    def configure(self):
        super().configure()
        if self.configurationDetailsOfHWSignal == None:
            return

        configurationDetails = self.configurationDetailsOfHWSignal
        if "NumberOfBits" in configurationDetails:
            self.vhdlSignalNumberOfBitsGenericName = "NumberOfBits"

        if "MantissaBits" in configurationDetails:
            self.vhdlSignalMantissaBitsGenericName = "MantissaBits"
        
        if "ExponentBits" in configurationDetails:
            self.vhdlSignalExponentBitsGenericName = "ExponentBits"

        if "FlopocoBits" in configurationDetails:
            self.vhdlSignalFlopocoBitsGenericName = "FlopocoBits"
 
    def process(self):
        pass

    def perform(self):
        # generate the signal with signal information
        self.generateVHDLSignal()
        self.generateVHDLTBSignal()
    
    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        super().resetProperties()
        # property to store the VHDL signal IEEE name
        self._vhdlSignalIEEEName = None
        # property to store the signal declaration closure
        self._vhdlSignalDeclarationClosure = None
        # proeprty to store the vhdl signal closure
        self._vhdlSignalClosure = None
        # property to store the signal initialisation
        self._vhdlSignalInitialisation = None
        self._vhdlSignalTBIntialisation = None
        # property to store the vhdlDescription of the signal
        self.vhdlDescription = None
        self._vhdlSignalNumberOfBitsGenericName = None
        self._vhdlSignalMantissaBitsGenericName = None
        self._vhdlSignalExponentBitsGenericName = None
        self._vhdlSignalFlopocoBitsGenericName = None
        # property to store the vhdlDescription of the signal
        self.vhdlSignalDescription = None
        self.vhdlSignalTBDescription = None



    def run(self):
        self.main()


