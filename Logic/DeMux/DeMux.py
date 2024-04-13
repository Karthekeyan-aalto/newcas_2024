"""
Created by Karthekeyan Periasamy
"""

from Logic.Port.Port import Port
from Logic.Logic import Logic
from HWSimulation.Logic.Mux.MuxVHDLSimulation import MuxVHDLSimulation
from HWDescription.Logic.Mux.MuxVHDLDescription import MuxVHDLDescription


class DeMux (Logic):

    def __init__(self):
        super().__init__()

        #property to connect the HW Description package of the Demux
        self.connectHWDescriptionPackage()

        #property to connect the HW Simulation package of the DeMux
        self.connectHWSimulationPackage()
        
        # property to store the selectSignal bits
        self._selectSignalBits = None

        #property to store the selectSignalCases
        self.selectSignalCases = None
        
        # property to store teh python definition of the Mux
        self.pythonDeMUX = None
    
    
    #property overriding
    @property
    def selectSignalBits(self):
        return  self._selectSignalBits

    @selectSignalBits.setter
    def selectSignalBits(self,value):

        self._selectSignalBits = value

        # generate the required payment
        self.selectSignalCases = [list(i) for i in itertools.product([0,1], repeat=self._selectSignalBits)]
        # print the select signal cases
        #print("Select Signal Cases", self.selectSignalCases)

        # temporary selectSignalCases property
        selectSignalCases = list()
        # loop through the select signal case
        for selectSignalCase in self.selectSignalCases:
            # join the select signal case
            selectSignalCase = ("".join(map(str,selectSignalCase)))
            selectSignalCases.append(selectSignalCase)

        #print the select signal case
        print("Select signal case", selectSignalCases)
        self.selectSignalCases = selectSignalCases

        # make the selectSignal port and update the inputDataPorts
        # access the information about the port or use the configuration details property to configure itself
        newPort = Port()
        newPort.configurationDetails = {"Name":"selectSignal","NumberOfBits":self._selectSignalBits,"PortType":"Input"}
        # configure the port
        newPort.configure()
        # process the port
        newPort.process()
        # once the port is configured, add the port to the InputDataPorts array
        self.inputDataPorts.append(newPort)



    def main(self):
        pass

      
    def connectHWDescriptionPackage(self):
        # connect the HWDescription Package
        self.hwDescription = MuxVHDLDescription()
        
    
    def connectHWSimulationPackage(self):
        # connect the HWSimulation Package
        self.hwSimulation = MuxVHDLSimulation()

    def process(self):
        # initialise the pythonMux dictionary
        self.pythonDeMUX = dict()
        # check if the length of the input data ports is 1
        if len(self.inputDataPorts != 1):
            print("Processing the configuration details for DeMux is not possible, as the number of input ports are not valid")
            return

        # for deMux  output data ports is expected to be empty when configured
        # use the select Signal bits to generate the output ports
        for selectSignalCaseIndex, selectSignalCase in  
        # print the length of the select signal cases
        #print("The SelectSignal Cases", self.selectSignalCases)
        # print the length of the input data ports
        #print(" The length of the input data ports", self.inputDataPorts)
        #loop through the cases and input ports
        # before that, check the len of the cases and the input port
        if (len(self.selectSignalCases) == (len(self.inputDataPorts) - 1)):

            for selectSignalCaseIndex, selectSignalCase in enumerate(self.selectSignalCases):
                # access the port
                port = self.inputDataPorts[selectSignalCaseIndex]
                # selectSignalCase
                # print the select signal case
                print("Select Signal Case", selectSignalCase)
                # access the signal case
                self.pythonMUX[selectSignalCase] = port.name
                
            
            self.pythonMUX["OTHERS"] = self.generateHyphenString()
            print("The python MUX",self.pythonMUX)

    def configure(self):
        """
        function to configure the details of the DeMux
        """
        
        super().configure()
        
        # check the configuration details of the select signal bits
        if "SelectSignalBits" in self.configurationDetailsOfLogic:
            self.selectSignalBits = self.configurationDetailsOfLogic["SelectSignalBits"]


    def run(self):
        pass
