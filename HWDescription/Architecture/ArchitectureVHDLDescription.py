"""
Created by Karthekeyan Periasamy
Edited on April 4, 2023, 10:16
"""

from HWDescription.Architecture.ArchitectureHWDescription import ArchitectureHWDescription
from HWDescription.Generics.GenericVHDLDescription import GenericVHDLDescription
from HWDescription.Signals.SignalVHDLDescription import SignalVHDLDescription
from HWDescription.Process.ProcessVHDLDescription import ProcessVHDLDescription

class ArchitectureVHDLDescription(ArchitectureHWDescription):

    def __init__(self):
        self.connect()
    
    
    """
    # Start: vhdlInputSignals getters
    """

    @property
    def vhdlInputSignals(self):
        if self._vhdlInputSignals == None:
            self._vhdlInputSignals = list()
            
        return self._vhdlInputSignals
        
    @vhdlInputSignals.setter
    def vhdlInputSignals(self, value):
        self._vhdlInputSignals = value
       
    """
    # End: vhdlInputSignals setters and getters
    """
    
    """
    # Start: vhdlOutputSignals getters
    """

    @property
    def vhdlOutputSignals(self):
        if self._vhdlOutputSignals == None:
            self._vhdlOutputSignals = list()
            
        return self._vhdlOutputSignals
        
    @vhdlOutputSignals.setter
    def vhdlOutputSignals(self, value):
        self._vhdlOutputSignals = value
       
    """
    # End: vhdlOutputSignals setters and getters
    """
    
    """
    # Start: vhdlEntityInstances getters
    """

    @property
    def vhdlEntityInstances(self):
        if self._vhdlEntityInstances == None:
            self._vhdlEntityInstances = list()
            
        return self._vhdlEntityInstances
        
    @vhdlEntityInstances.setter
    def vhdlEntityInstances(self, value):
        self._vhdlEntityInstances = value
       
    """
    # End: vhdlEntityInstances setters and getters
    """
    
    """
    # Start: vhdlSignals getters
    """

    @property
    def vhdlSignals(self):
        if self._vhdlSignals == None:
            self._vhdlSignals = list()
            
        return self._vhdlSignals
        
    @vhdlSignals.setter
    def vhdlSignals(self, value):
        self._vhdlSignals = value
       
    """
    # End: vhdlSignals setters and getters
    """

    
    """
    # Start: vhdlEntityTBIOSignals getters
    """

    @property
    def vhdlEntityTBIOSignals(self):
        if self._vhdlEntityTBIOSignals == None:
            self._vhdlEntityTBIOSignals = list()
            
        return self._vhdlEntityTBIOSignals
        
    @vhdlEntityTBIOSignals.setter
    def vhdlEntityTBIOSignals(self, value):
        self._vhdlEntityTBIOSignals = value
       
    """
    # End: vhdlEntityTBIOSignals setters and getters
    """


    
    """
    # Start: pythonHWOutputPorts getter
    """

    @property
    def pythonHWOutputPorts(self):
        if self._pythonHWOutputPorts == None:
            self._pythonHWOutputPorts = list()
            
        return self._pythonHWOutputPorts
        
    @pythonHWOutputPorts.setter
    def pythonHWOutputPorts(self, value):
        self._pythonHWOutputPorts = value
        #print("NumberOfOutput Ports",len(self.pythonHWOutputPorts))
        # access the vhdlOutputPortSignals property
        # add the signals of the output port to the vhdl signals
        for outputPort in self._pythonHWOutputPorts:
            self.vhdlOutputSignals.append(outputPort.hwDescription.vhdlPortSignal)

        #print("VHDLOutputPort Signals",len(self.vhdlOutputSignals))

       
    """
    # End: pythonHWOutputPorts setter
    """
    
    """
    # Start: pythonHWInputPorts getter
    """

    @property
    def pythonHWInputPorts(self):
        if self._pythonHWInputPorts == None:
            self._pythonHWInputPorts = list()
            
        return self._pythonHWInputPorts
        
    @pythonHWInputPorts.setter
    def pythonHWInputPorts(self, value):
        self._pythonHWInputPorts = value
        #print("NumberOfInput Ports",len(self._pythonHWInputPorts))
        # access the vhdlInputSignals property
        # add the signals of the input port to the vhdl signals
        for inputPort in self.pythonHWInputPorts:
            self.vhdlInputSignals.append(inputPort.hwDescription.vhdlHWSignalDescription.vhdlSignalDescription)

        #print("VHDLInputPort Signals",len(self.vhdlInputSignals))

       
    """
    # End: pythonHWInputPorts setter
    """


    def connect(self):
        super().connect()
        self.connectHWVHDLPackages()
        self.connectProperties()
    

    def connectHWVHDLPackages(self):
        # connect the hw generic packages
        # here the hw generic package is used to generate hw testbench constant signals
        self.vhdlGenericDescription = GenericVHDLDescription()
        # connect the hw signal packages
        self.vhdlSignalDescription = SignalVHDLDescription()
        # connect the hw process packages
        self.vhdlProcessDescription = ProcessVHDLDescription()


    
    def hwVHDLEntityArchitectureDefinitionStartSyntax(self):
        entityArchitectureDefinitionStartSyntax = ("ARCHITECTURE" + " " + "rtl" + " " + "of " + self.hwName + " " + "IS" + "\n")
        return entityArchitectureDefinitionStartSyntax

    def hwVHDLEntityArchitectureDefinitionEndSyntax(self):
        entityArchitectureTBDefinitionEndSyntax = ("END" + " " + "ARCHITECTURE" + ";" + "\n")
        return entityArchitectureTBDefinitionEndSyntax
    
    
    def hwVHDLEntityArchitectureTBDefinitionStartSyntax(self):
        entityArchitectureDefinitionStartSyntax = ("ARCHITECTURE" + " " + "rtl" + " " + "of " + self.hwName + "_" + "tb" + " " + "IS" + "\n")
        return entityArchitectureDefinitionStartSyntax

    def connectProperties(self):
        super().connectProperties()

        # property to store the vhdlSignals in total
        # this will be the final one for a HW entity that will be added to architecture
        self._vhdlSignals = None

        # property to store the vhdl architecture definition
        self.vhdlEntityArchitectureDefinition = None

        # property to store the vhdl test bench architecture definition
        self.vhdlEntityArchitectureTBDefinition = None
        
        # property to store the Input Signals
        # this contains the signals of input ports and other input signals that will be fed to the components of the top entity
        self._vhdlInputSignals = None


        #property to store the vhdlOutput signals
        # this contain the signals output port signals and component output signals
        self._vhdlOutputSignals = None

        # property to store the architecture instances
        # the instancs could be of arithmetic nodes, could of registers or some other hw instances, that are not the top entity
        self._vhdlEntityInstances = None

        # property to store the top entity architecture instance
        # this is used mainly to generate test bench of the top entity
        self._vhdlEntityInstance = None

        self._vhdlEntityTBInstance = None

        # property to store the vhdlSignals that is part of the test bench architecture
        self._vhdlEntityTBIOSignals = None



    def reset(self):
        self.resetProperties()
        self.resetHWVHDLPackages()
   
    def resetHWVHDLPackages(self):
        # reset the hw generic packages
        # here the hw generic package is used to generate hw testbench constant signals
        self.vhdlGenericDescription = None
        # reset the hw signal packages
        self.vhdlSignalDescription = None
        # reset the hw process packages
        self.vhdlProcessDescription = None


    def generateHWVHDLEntityArchitectureDefinition(self):
        entityArchitectureDefinition = self.hwVHDLEntityArchitectureDefinitionStartSyntax()

        # access the vhdlOutputPortSignals
        # append the entityArchitectureDefinition with output port syntax
        for vhdlOutputPortSignal in self.vhdlOutputSignals:
            entityArchitectureDefinition = entityArchitectureDefinition + "    " + vhdlOutputPortSignal
            

        # begin the lutVHDLEntity architecture
        entityArchitectureDefinition = (entityArchitectureDefinition + "BEGIN" + "\n" \
                + "    ")

        if self.pythonHWClockPort != None:

            # attach the process start and end description of the HW
            entityArchitectureDefinition = entityArchitectureDefinition + self.vhdlProcessDescription.vhdlEntityProcessDefinition

        else:
            # attach the python HW to the architecture
            entityArchitectureDefinition = self.pythonHW
        
        # attach the python HW to the architecture

        entityArchitectureDefinition = entityArchitectureDefinition + self.hwVHDLEntityArchitectureDefinitionEndSyntax()
        self.vhdlEntityArchitectureDefinition = entityArchitectureDefinition
        #print("Architecture Definition", self.vhdlEntityArchitectureDefinition)
    
    
    
    def generateHWVHDLEntityTBArchitectureDefinition(self):
        entityArchitectureDefinition = self.hwVHDLEntityArchitectureTBDefinitionStartSyntax()

        # access the vhdl constant signals
        # append the entityArchitectureTB Definition with the information about the constants
        for vhdlConstantSignal in self.vhdlGenericDescription.vhdlConstantSignals:
            entityArchitectureDefinition = entityArchitectureDefinition + "    " + vhdlConstantSignal

        # access the vhdlOutputPortSignals
        # append the entityArchitectureTB Definition with output port syntax
        for vhdlEntityTBIOSignal in self.vhdlEntityTBIOSignals:
            entityArchitectureDefinition = entityArchitectureDefinition + "    " + vhdlEntityTBIOSignal
            

        # begin the lutVHDLEntity architecture
        entityArchitectureDefinition = (entityArchitectureDefinition + "BEGIN" + "\n" \
                + "    ")

        # attach the vhdl instance in the test bench architecture
        entityArchitectureDefinition = entityArchitectureDefinition + "    " + self.vhdlEntityTBInstance + "\n" \
        
        # attach the entity tb process defintion
        entityArchitectureDefinition = entityArchitectureDefinition + self.vhdlProcessDescription.vhdlTBClockProcess + self.vhdlProcessDescription.vhdlTBIOStimulusProcess
        
        
        entityArchitectureDefinition = entityArchitectureDefinition + self.hwVHDLEntityArchitectureDefinitionEndSyntax()
        self.vhdlEntityArchitectureTBDefinition = entityArchitectureDefinition

    def resetProperties(self):
        super().resetProperties()
        
        self._vhdlSignals = None

        # property to store the vhdl architecture definition
        self.vhdlEntityArchitectureDefinition = None
        
        # property to store the Input Signals
        # this contains the signals of input ports and other input signals that will be fed to the components of the top entity
        self._vhdlInputSignals = None


        #property to store the vhdlOutput signals
        # this contain the signals output port signals and component output signals
        self._vhdlOutputSignals = None
        
        # property to store the architecture instances
        # the instancs could be of arithmetic nodes, could of registers or some other hw instances
        self._vhdlEntityInstances = None
        
        # property to store the entityTBIOSignal instances
        self._vhdlEntityTBIOSignals = None
        
        # property to store the vhdl test bench architecture definition
        self.vhdlEntityArchitectureTBDefinition = None
        
        # property to store the top entity architecture instance
        # this is used mainly to generate test bench of the top entity
        # this property will be set using the entity vhdl description instance definition of the top entity
        self._vhdlEntityInstance = None
        
        self._vhdlEntityTBInstance = None

    def configure(self):
        super().configure()
        configurationDetails = self.configurationDetailsOfHW
        
        # check the generics key of the HW
        # generics of the HW act as the constant signals in the architecture of the HW
        if "PythonHWGeneric" in configurationDetails:
            self.vhdlGenericDescription.configurationDetailsOfHWGenerics = configurationDetails["PythonHWGeneric"]
            self.vhdlGenericDescription.configure()

 
        if "PythonHWProcess" in configurationDetails:
            #print("ConfigurationDetails Of HW Process", configurationDetails["PythonHWProcess"])
            self.vhdlProcessDescription.configurationDetailsOfHW = configurationDetails["PythonHWProcess"]
            self.vhdlProcessDescription.configure()
    
    def process(self):
        # process the configuration information for the port signals to be used as part of the testbench
        self.processHWVHDLTBSignalConfiguration()
        self.vhdlProcessDescription.process()
    
    def processHWVHDLTBSignalConfiguration(self):
        # make a for loop to loop through the input and output ports
        for pythonHWInputPort in self.pythonHWInputPorts:
            # print the pythonHWInputPort name and the number of bits
            #print("Python HW Input Port Name", pythonHWInputPort.name)
            #print("Python HW Input Port Number Of Bits", pythonHWInputPort.numberOfBits)
            
            # make the information for the signal to be formed from the pythonHWInputPort that is suitable for testbench
            configurationDetails = dict()
            configurationDetails = {"Name":pythonHWInputPort.name,"NumberOfBits":pythonHWInputPort.numberOfBits,"ConstantSignalValue":0}
            vhdlHWSignalDescription = SignalVHDLDescription()
            vhdlHWSignalDescription.configurationDetailsOfHWSignal = configurationDetails
            vhdlHWSignalDescription.configure()
            vhdlHWSignalDescription.process()
            vhdlHWSignalDescription.perform()
            self.vhdlEntityTBIOSignals.append(vhdlHWSignalDescription.vhdlSignalTBDescription)

        # make a for loop to loop through the outuput ports
        for pythonHWOutputPort in self.pythonHWOutputPorts:
            # print the python hw output port
            #print("Python HW Output Port", pythonHWOutputPort.name)
            #print("Python HW Output Port", pythonHWOutputPort.numberOfBits)
            
            # make the information for the signal to be formed from the pythonHWInputPort that is suitable for testbench
            configurationDetails = dict()
            configurationDetails = {"Name":pythonHWOutputPort.name,"NumberOfBits":pythonHWOutputPort.numberOfBits,"ConstantSignalValue":0}
            vhdlHWSignalDescription = SignalVHDLDescription()
            vhdlHWSignalDescription.configurationDetailsOfHWSignal = configurationDetails
            vhdlHWSignalDescription.configure()
            vhdlHWSignalDescription.process()
            vhdlHWSignalDescription.perform()
            self.vhdlEntityTBIOSignals.append(vhdlHWSignalDescription.vhdlSignalTBDescription)

        # add the reset port and clock port to the signal description
        
        # make the information for the signal to be formed from the pythonHWInputPort that is suitable for testbench
        configurationDetails = dict()
        configurationDetails = {"Name":self.pythonHWClockPort.name,"NumberOfBits":self.pythonHWClockPort.numberOfBits,"ConstantSignalValue":0}
        vhdlHWSignalDescription = SignalVHDLDescription()
        vhdlHWSignalDescription.configurationDetailsOfHWSignal = configurationDetails
        vhdlHWSignalDescription.configure()
        vhdlHWSignalDescription.process()
        vhdlHWSignalDescription.perform()
        self.vhdlEntityTBIOSignals.append(vhdlHWSignalDescription.vhdlSignalTBDescription)
        
        # make the information for the signal to be formed from the pythonHWInputPort that is suitable for testbench
        configurationDetails = dict()
        configurationDetails = {"Name":self.pythonHWResetPort.name,"NumberOfBits":self.pythonHWResetPort.numberOfBits,"ConstantSignalValue":0}
        vhdlHWSignalDescription = SignalVHDLDescription()
        vhdlHWSignalDescription.configurationDetailsOfHWSignal = configurationDetails
        vhdlHWSignalDescription.configure()
        vhdlHWSignalDescription.process()
        vhdlHWSignalDescription.perform()
        self.vhdlEntityTBIOSignals.append(vhdlHWSignalDescription.vhdlSignalTBDescription)
        
        if self.pythonHWEnablePort != None:
            # make the information for the signal to be formed from the pythonHWInputPort that is suitable for testbench
            configurationDetails = dict()
            configurationDetails = {"Name":self.pythonHWEnablePort.name,"NumberOfBits":self.pythonHWEnablePort.numberOfBits,"ConstantSignalValue":1}
            vhdlHWSignalDescription = SignalVHDLDescription()
            vhdlHWSignalDescription.configurationDetailsOfHWSignal = configurationDetails
            vhdlHWSignalDescription.configure()
            vhdlHWSignalDescription.process()
            vhdlHWSignalDescription.perform()
            self.vhdlEntityTBIOSignals.append(vhdlHWSignalDescription.vhdlSignalTBDescription)


    def perform(self):
        self.vhdlProcessDescription.perform()
        self.generateHWVHDLEntityArchitectureDefinition()
        self.generateHWVHDLEntityTBArchitectureDefinition()

    def main(self):
        self.process()
        self.perform()

    def run(self):
        self.main()

