"""
Created by Karthekeyan Periasamy
Edited on November 11 12:15
"""

class Receiver():

    """
    Class to store the details of the output port of an operator
    This class is mostly software logic, but help know information about the another operator about the receiver or the driver of the "another operator"
    The receiver will identify the arithmeticNode that is the output of the operator
    This help the HW Multiplier to configure the port object
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
            self.isReceiverAPort = True
        elif len(self._name.split("_")) == 3:
            self.isReceiverAnArithmeticNode = True
            # extract the information from the name of the receiver
            receiverNodeIndexInArithmeticNodeArray = self._name.split("_")[(len(self._name.split("_"))-1)]
            # the information about the receiver will be used for further processing
            self.info = dict()
            self.info[self._name] =  receiverNodeIndexInArithmeticNodeArray
            

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
        self.isReceiverAPort = False

        # property to know whether the receiver is a arithmetic node or not
        self.isReceiverAnArithmeticNode = False
        
        # proprety to store the information regarding the receiver
        self.info = dict()
        
        # intialise the outputPorts array
        self.outputPorts = list()


       


    def configure(self):
        # check if the configuration details of the driver is set or not
        if self.configurationDetailsOfReceiver == None:
            return

        # store the configuration details on the local variable
        configurationDetails = self.configurationDetailsOfReceiver

        if "Name" in configurationDetails:
            # set the name of the configuration details
            self.name = configurationDetails["Name"]

      
        self.outputPorts = list()

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
        self.isReceiverAPort = False

        # property to know whether the receiver is a arithmetic node or not
        self.isReceiverAnArithmeticNode = False
        
        # proprety to store the information regarding the receiver
        self.info = dict()
        
        # intialise the outputPorts array
        self.outputPorts = list()

        

    def process(self):
        pass

    def perform(self):
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




