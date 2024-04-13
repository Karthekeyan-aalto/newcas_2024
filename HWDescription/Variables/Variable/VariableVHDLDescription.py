"""
Created by Karthekeyan Periasamy
Created on Jan 24 14:11
"""

from HWDescription.Variables.VariableHWDescription import VariableHWDescription

class VariableVHDLDescription(VariableHWDescription):
    

    def __init__(self):
        super().__init__()   
    
    @property
    def vhdlVariableIEEEName(self):
        return self._vhdlVariableIEEEName

    @vhdlVariableIEEEName.setter
    def vhdlVariableIEEEName(self,value):
        self._vhdlVariableIEEEName = value

        if (self.vhdlVariableIEEEName == "bit_vector" or self.vhdlVariableIEEEName == "std_logic_vector"):
            self.vhdlVariableIEEENameType = 2
            self.vhdlVariableIEEENameOutputConverter = "to_bitvector"
        elif self.vhdlVariableIEEEName == "line":
            self.vhdlVariableIEEENameType = 1
            self.vhdlVariableIEEENameOutputConverter = str()
        elif self.vhdlVariableIEEEName == "character":
            self.vhdlVariableIEEENameType = 3
            self.vhdlVariableIEEENameOutputConverter = str()
    
    @property
    def vhdlVariableDeclarationClosure(self):
        if self._vhdlVariableDeclarationClosure == None:
            # check if the variable is a bus or not
            if self.isVariableABus == True:
                self._vhdlVariableDeclarationClosure = "(" + "numberOfBits-1" + " " + "DOWNTO" + " " + "0" + ")" + ";" + "\n"
            else:
                # check if the constant signal value is set or not
                # if the constant signal value is set, we do not need the closure
                # as the closure is taken care by the signal initialisation

                #print("Constant Variable Value is not None")
                if self.constantVariableValue == None:
                    self._vhdlVariableDeclarationClosure = ";" + "\n"
                else:
                    #print("Constant Signal Value is not None")
                    self._vhdlVariableDeclarationClosure = ""

        return self._vhdlVariableDeclarationClosure

    @vhdlVariableDeclarationClosure.setter
    def vhdlVariableDeclarationClosure(self,value):
        self._vhdlVariableDeclarationClosure = value

    @property
    def vhdlVariableInitialisation(self):
        if self._vhdlVariableInitialisation == None:
            if self.isVariableABus == True:
                self._vhdlVariableInitialisation = ":=" + " " + "(" + "others" + " " + "=>" + " " + str(self.constantVariableValue) + ")" + ";" + "\n"
            else:
                # set the variable initialisation
                self._vhdlVariableInitialisation = ":=" + " " + "\'0\'" + ";" + "\n"

        return self._vhdlVariableInitialisation

    
    @vhdlVariableInitialisation.setter
    def vhdlVariableInitialisation(self,value):
        self._vhdlVariableInitialisation = value
    
    
    def configure(self):
        super().configure()

        if self.configurationDetailsOfHWVariable == None:
            return

        configurationDetails = self.configurationDetailsOfHWVariable
        #print("Configuration Details of Variable", configurationDetails)

        if "Type" in configurationDetails:
            self.vhdlVariableIEEEName = configurationDetails["Type"]

    
    
    def connect(self):
        self.connectProperties()


    def connectProperties(self):
        super().connectProperties()
        self._vhdlVariableIEEEName = None
        self._vhdlVariableDeclarationClosure = None
        self._vhdlVariableInitialisation = None
        self.vhdlDescription = None
        self.vhdlVariableIEEENameOutputConverter = None
        self.vhdlVariableIEEENameType = None


    def generateVHDLVariable(self):
        #print("Variable Name",self.name)
        #print("VHDL Variable IEEEName", self.vhdlVariableIEEEName)
        
        #self.vhdlDescription = "Variable" + " " + self.name + " " + ":" + self.vhdlVariableIEEEName + self.vhdlVariableDeclarationClosure + self.vhdlVariableInitialisation
        
        self.vhdlDescription = "Variable" + " " + self.name + " " + ":" + self.vhdlVariableIEEEName + self.vhdlVariableDeclarationClosure
        #print(self.vhdlDescription)

    
    def process(self):
        pass

    def perform(self):
        # generate the signal with signal information
        self.generateVHDLVariable()
    
    def reset(self):
        self.resetProperties()


    def resetProperties(self):
        super().resetProperties()
        self.vhdlDescription = None
        self._vhdlVariableIEEEName = None
        self._vhdlVariableDeclarationClosure = None
        self._vhdlVariableInitialisation = None
        self.vhdlVariableIEEENameType = None
        self.vhdlVariableIEEENameOutputConverter = None

    def run(self):
        self.main()


