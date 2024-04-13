"""
Created by Karthekeyan Periasamy
Edited on Jan 21 15:55
"""

from Operators.Port.Port import Port
from Operators.LUTs.LUT import LUT
from HWDescription.Operators.LUTs.FloatLUT.FloatLUTVHDLDescription import FloatLUTVHDLDescription



class FloatLUT(LUT):
    """
    This class is the extension of the normal LUT
    This LUT will have the float 1 value for a given integer 1
    """

    def __init__(self):
        super().__init__()
        
        # property to store the mantissaBits
        self.mantissaBits = None
        
        # property to store the mantissaBits
        self.exponentBits = None


    
    def generateLUT(self):
        """
        Function to generate a LUT based on the number of bits set
        The number of bits of input data ports will be mapped
        with number of bits of the output port. Here the top input port
        and top output port from the ports array will be used to generate the LUT
        
        Return: The function will return a dictionary which then can be used by the
        HWDescription package to generate appropriate HW architecture using the behaviour dictionary

        *For now, we have generation of LUT when the input is one bit (either 0 or 1) and the output LUT or dictionary can represent both 0 and posit 1
        """
        inputPort = None
        outputPort = None

        # check whether there is a top input port 
        if self.inputDataPorts[0] != None:
            # access the top input port
            port = self.inputDataPorts[0]
            # set the port to the inputPort
            inputPort = port

        outputPort = None
        # check whether there is a top output port 
        if self.outputPorts[0] != None:
            # access the top output port
            port = self.outputPorts[0]
            # set the port to the inputPort
            outputPort = port

        # access the number of bits of the inputPort
        numberOfBits = inputPort.numberOfBits

        # check if the numberOfBits is 1 or not
        if numberOfBits == 1:
            # access the output port bits
            outputPortBits = outputPort.numberOfBits
            if outputPortBits == self.numberOfBits:
                # generate zero string for the number of bits
                zeroString = self.generateZeroString()
                # update the python LUT
                self.pythonLUT["0"] = zeroString
                # update the python LUT with float 1
                # however as the floaone 
                self.pythonLUT["1"] = "floatOneSignal"
                self.pythonLUT["OTHERS"] = self.generateHyphenString()
        else:
             return
    

    def configure(self):
        super().configure()
        configurationDetails = self.configurationDetailsOfLUT
        
        # check the configuration details contains exponent bits details
        if "ExponentBits" in configurationDetails:
            self.exponentBits = configurationDetails["ExponentBits"]
            
        
        # check the configuration details contains mantissa bits details
        if "MantissaBits" in configurationDetails:
            self.mantissaBits = configurationDetails["MantissaBits"]

           
   
    def configureHWDescriptionPackage(self):
        super().configureHWDescriptionPackage()
       
        # set the luts generics of the hwDescription of LUT
        lutGenerics = dict()
        if self.numberOfBits != None:
            lutGenerics["numberOfBits"] = self.numberOfBits

        if self.mantissaBits != None:
            lutGenerics["mantissaBits"] = self.mantissaBits

        if self.exponentBits != None:
            lutGenerics["exponentBits"] = self.exponentBits
        
        # set the lut generics
        self.hwDescription.lutGenerics = lutGenerics
    
    def processHWDescriptionPackage(self):
        super().processHWDescriptionPackage()

 
    def connectHWDescriptionPackage(self):
        # connect the HWDescription Package
        self.hwDescription = FloatLUTVHDLDescription()

    def process(self):
        super().process()

    def reset(self):
        super().reset()
    
    def main(self):
        self.process()

    def run(self):
        self.main()

        


