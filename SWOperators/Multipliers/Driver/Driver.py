"""
Created by Karthekeyan Periasamy
Edited on July 10 12:15
"""

class Driver():

    """
    Class to identify what is driving an operator
    This class is mostly software logic, but help design the HW logic
    For instance, if the multiplicand of the multiplier is driven by a port,
    The driver will identify whether its a port or not by the name of it
    This help the HW Multiplier to configure the port object
    Additionally, also, the driver might be a weight, and this help multiplier to enable, read and write the specific weight from memory
    """

    def __init__(self):
        self.connect()    
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value
        if self._name[0] == self.portLetter:
            self.isDriverAPort = True
        elif self.__isNameAFloat() == True:
            self.isDriverAWeight = True
        elif len(self._name.split("_")) == 3:
            self.isDriverAnArithmeticNode = True
            # extract the information from the name of the driver
            driverNodeIndexInArithmeticNodeArray = self._name.split("_")[(len(self._name.split("_"))-1)]
            # the information about the driver will be used for further processing
            self.info = dict()
            self.info[self._name] =  driverNodeIndexInArithmeticNodeArray
            

    def connect(self):
        self.connectProperties()    

    def connectProperties(self):
        #property to store the number of the driver
        # the number is used same as the index of the operator
        # using this number we can differentitate the multipliers by appending the name of the Multiplier
        self.number = 0

        # property to store the name of the driver
        # it is a string
        self._name = None

        # property to store the port letter this property can be set to whether the driver is a port or not
        self.portLetter = 'v'

        #property to know whether the driver name is a port or not
        self.isDriverAPort = False

        # property to know whether a driver is a weight or not
        self.isDriverAWeight = False

        # property to know whether a drive is another arithmetic node or not
        self.isDriverAnArithmeticNode = False

        self.configurationDetailsOfDriver = None
       


    def configure(self):
        # check if the configuration details of the driver is set or not
        if self.configurationDetailsOfDriver == None:
            return

        # store the configuration details on the local variable
        configurationDetails = self.configurationDetailsOfDriver

        if "Name" in configurationDetails:
            # set the name of the configuration details
            self.name = configurationDetails["Name"]

      
        # intialise the inputDataPorts array
        self.inputDataPorts = list()

        # check the configuration details contains input data ports
        if "InputDataPorts" in configurationDetails:

            # access the ports and set the details of the port
            # the value of the key is expected to be an array
            portDetails = configurationDetails["InputDataPorts"]
            #print("LUT InputDataPorts", portDetails)
            for portDetail in portDetails:
                # access the information about the port or use the configuration details property to configure itself
                newPort = Port()
                newPort.configurationDetails = portDetail
                # configure the port
                newPort.configure()
                # process the port
                newPort.process()
                # once the port is configured, add the port to the InputDataPorts array
                self.inputDataPorts.append(newPort)

        
        
        # check the configuration details contains output port details
        if "OutputPorts" in configurationDetails:
            # access the ports and set the details of the port
            # the value of the key is expected to be an array
            portDetails = configurationDetails["OutputPorts"]
            for portDetail in portDetails:
                # access the information about the port or use the configuration details property to configure itself
                newPort = Port()
                newPort.configurationDetails = portDetail
                # configure the port
                newPort.configure()
                # process the port
                newPort.process()
                #print("Add the output port")
                # once the port is configured, add the port to the InputDataPorts array
                self.outputPorts.append(newPort)
            
        
        # check the configuration details contains clock port details
        if "InputClockPort" in configurationDetails:
            # access the ports and set the details of the port
            # the value of the key is expected to be a dict
            clockPortDetail = configurationDetails["InputClockPort"]
            # access the portDetail frequency
            # it is expected to have single frequency for the clock port
            # also, only one clock port is possible
            # access the information about the port or use the configuration details property to configure itself'
            newPort = Port()
            newPort.configurationDetails = clockPortDetail
            # configure the port
            newPort.configure()
            # process the port
            newPort.process()
            # once the port is configured, set the port
            self.clockPort = newPort
            
        
        
        # check the configuration details contains reset port or not
        if "InputResetPort" in configurationDetails:
            # access the ports and set the details of the port
            # the value of the key is expected to be a dict
            resetPortDetail = configurationDetails["InputResetPort"]
            # access the reset port detail
            # only one reset port is possible
            # access the information about the port or use the configuration details property to configure itself'
            newPort = Port()
            newPort.configurationDetails = resetPortDetail
            # configure the port
            newPort.configure()
            # process the port
            newPort.process()
            # once the port is configured, set the port
            self.resetPort = newPort
        
        # check the configuration details contains reset port or not
        if "InputDataSelect" in configurationDetails:
            # access the ports and set the details of the port
            # the value of the key is expected to be a dict
            inputDataSelectDetail = configurationDetails["InputDataSelect"]
            # access the inputDataSelect port detail
            # only one reset port is possible
            # access the information about the port or use the configuration details property to configure itself'
            newPort = Port()
            newPort.configurationDetails = inputDataSelectDetail
            # configure the port
            newPort.configure()
            # process the port
            newPort.process()
            # once the port is configured, set the port to the inputdata select port
            self.inputDataSelectPort = newPort



    
    
    
    def reset(self):
        self.resetProperties()
    
    def resetProperties(self):
        #property to store the number of the driver
        # the number is used same as the index of the operator
        # using this number we can differentitate the multipliers by appending the name of the Multiplier
        self.number = 0

        # property to store the name of the driver
        # it is a string
        self._name = None

        # property to store the port letter this property can be set to whether the driver is a port or not
        self.portLetter = 'v'

        #property to know whether the driver name is a port or not
        self.isDriverAPort = False

        # property to know whether a driver is a weight or not
        self.isDriverAWeight = False

        # property to know whether a drive is another arithmetic node or not
        self.isDriverAnArithmeticNode = False

        self.configurationDetailsOfDriver = None
        

    def process(self):
        pass

    def main(self):
        pass
        
    """
    # Start:__isNameAFloat function
    """
    def __isNameAFloat(self):
        try:
            float(self.name)
            return True
        except ValueError:
            return False
    
    """
    # End: __isNameAFloat function
    """
   
    def run(self):
        pass




