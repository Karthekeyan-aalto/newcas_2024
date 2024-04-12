# class made by Karthek
# Sep 26 09:22

class PCSystemConfiguration():
    """
    This class handles the configuration of a PCSystem
    Why use this module: Given PCSystem Configuration package details as a dictionary
    this class will set the respective properties, which then can be used by other modules or packages.

    """

    def __init__(self):
        # property to store the details of the PCSystem as a dictionary
        # information in this dictionary include number of bits, system type, number system and etc.
        self._pcSystemConfiguration = None
        # store the number of bits of the pcSystem
        self._pcSystemNumberOfBits = None
        # store the exponent bits
        self._pcSystemExponentBits = None
        # total number of configuration
        self._totalNumberOfConfigurations = None
        # totalConfigurations
        self.configurations = None
        # store the configuration details
        self._configurationDetailsOfSystemPackage = None
    
    """
    Properties of PCSystem Configuration
    """
    @property
    def configurationDetailsOfSystemPackage(self):
        return self._configurationDetailsOfSystemPackage
    
    @configurationDetailsOfSystemPackage.setter
    def configurationDetailsOfSystemPackage(self,value):
        self._configurationDetailsOfSystemPackage = value
        # access the configuration details of the PCSystem
        configurationDetails = self._configurationDetailsOfSystemPackage["PCSystemInfo"]
        print("The set configuration details", configurationDetails)
        # number of bits for the PCSystem
        # the variable will be set afer execution of PCMinOperation object and analysis processPCEquationed by PCAnalysis object
        # the exponentBits of the PCSystem, this will be used when the numberSystem is 2
        # the manitssaBits of the PCSystem, this will be used in the future to represent the numberSystem 2, that is Float
        # the esBits of the PCSystem, this will be used to represent the numberSystem 3, that is POSIT
        # numberSystem of the PCSystem
        # systemType 0) AC 1) SPN
        # error analysis type 0) relative error 1) absolute error
        # the variable will have custom setter to update the analysis object
        
        # property to store the information about the PCSystem in the form of a dictionary
        self.info = dict()
        # initialise the totalConfigurations object
        self.configurations = list()
        
        if "SystemType" in configurationDetails:
            self.pcSystemType = configurationDetails["SystemType"]
        
        # check whether the key Model is present
        if "Model" in configurationDetails:
            # set the model name
            self.pcSystemModel = configurationDetails["Model"]


        pcSystemNumberSystem = None
        # check whether the key NumberSystem is present
        if "NumberSystem" in configurationDetails:
            # set the system number system
            self.pcSystemNumberSystem = configurationDetails["NumberSystem"]
            # check the number system
            if pcSystemNumberSystem == "Fixed":
                # check array length of the number of bits key in the dictionary
                # check whether the key NumberOfBits is present or not
                if "NumberOfBits" in configurationDetails:
                    # access the length of the number of bits and set it to total number of configurations
                    totalFixedNumberSystemConfiguration = configurationDetails["NumberOfBits"]
                    self.totalNumberOfConfigurations = len(totalFixedNumberSystemConfiguration)
                    print("Total Number of Fixed Configurations", self.totalNumberOfConfigurations)
                   
                    # loop through the total number of configurations
                    for numberOfBits in totalFixedNumberSystemConfiguration:
                        # access each number of bit and form a configuration object
                        configuration = PCSystemConfiguration()
                        # set the number system
                        configuration.pcSystemNumberSystem = self.pcSystemNumberSystem
                        configuration.pcSystemType =self.pcSystemType
                        configuration.pcSystemModel = self.pcSystemModel
                        configuration.pcSystemNumberOfBits = int(numberOfBits)
                        # add the configuration object to the configurations array
                        self.configurations.append(configuration)
                        
                    print("Fixed Configurations", self.configurations)
                                 
            elif pcSystemNumberSystem == "Float":
                 # look for the configuration of float number system
                 # check whether the key ExponentBits is present or not
                 pcSystemExponentBits = None
                 if "ExponentBits" in configurationDetails:
                     # set the exponent bits
                     pcSystemExponentBits= configurationDetails["ExponentBits"]
                     
                 # check whether the key MantissaBits is present
                 if "MantissaBits" in configurationDetails:
                     # set the exponent bits
                     self.pcSystemMantissaBits = configurationDetails["MantissaBits"]
                     # access the length of the number of bits and set it to total number of configurations
                     totalFloatNumberSystemConfiguration = configurationDetails["MantissaBits"]
                     self.totalNumberOfConfigurations = len(totalFloatNumberSystemConfiguration)
                     # check whether the key SystemType is present
                     # loop through the total number of configurations
                     for mantissaBits in totalFloatNumberSystemConfiguration:
                         # access each number of bit and form a configuration object
                         configuration = PCSystemConfiguration()
                         # set the number system
                         configuration.pcSystemNumberSystem = pcSystemNumberSystem
                         configuration.pcSystemType = pcSystemType
                         configuration.pcSystemModel = pcSystemModel
                         configuration.pcSystemExponentBits = pcSystemExponentBits
                         configuration.pcSystemMantissaBits = int(mantissaBits)
                         configuration.pcSystemNumberOfBits = str(int(pcSystemExponentBits) + int(mantissaBits))
                         # add the configuration object to the configurations array
                         self.configurations.append(configuration)
                         
                     
                     print("Float Configurations", self.configurations)

            elif pcSystemNumberSystem == "Posit":
                #print("ConfigurationDetails",configurationDetails)
                # check whether the key EsBits is present
                pcSystemEsBits = None
                if "EsBits" in configurationDetails:
                    # set the esBits 
                    pcSystemEsBits = configurationDetails["EsBits"]

                # check whether the key NumberOfBits is present or not
                if "NumberOfBits" in configurationDetails:
                    # set the number of bits
                    pcSystemNumberOfBits = configurationDetails["NumberOfBits"]
                    # access the length of the number of bits and set it to total number of configurations
                    totalPositNumberSystemConfiguration = configurationDetails["MantissaBits"]
                    self.totalNumberOfConfigurations = len(totalPositNumberSystemConfiguration)
                    # check whether the key SystemType is present
                    # loop through the total number of configurations
                    for mantissaBits in totalPositNumberSystemConfiguration:
                        # access each number of bit and form a configuration object
                        configuration = PCSystemConfiguration()
                        # set the number system
                        configuration.pcSystemNumberSystem = pcSystemNumberSystem
                        configuration.pcSystemType = pcSystemType
                        configuration.pcSystemModel = pcSystemModel
                        configuration.pcSystemEsBits = pcSystemEsBits
                        configuration.pcSystemNumberOfBits = pcSystemNumberOfBits
                        # add the configuration object to the configurations array
                        self.configurations.append(configuration)

        
        

    
    @property
    def totalNumberOfConfigurations(self):
        return self._totalNumberOfConfigurations
    
    @totalNumberOfConfigurations.setter
    def totalNumberOfConfigurations(self,value):
        self._totalNumberOfConfigurations = value


    @property
    def pcSystemNumberOfBits(self):
        return self._pcSystemNumberOfBits
    
    @pcSystemNumberOfBits.setter
    def pcSystemNumberOfBits(self,value):
        self._pcSystemNumberOfBits = value
    
    
    @property
    def pcSystemExponentBits(self):
        return self._pcSystemExponentBits
    
    @pcSystemExponentBits.setter
    def pcSystemExponentBits(self,value):
        self._pcSystemExponentBits = value
   

    @property
    def pcSystemMantissaBits(self):
        return self._pcSystemMantissaBits
    
    @pcSystemMantissaBits.setter
    def pcSystemMantissaBits(self,value):
        self._pcSystemMantissaBits = value
    
    @property
    def pcSystemEsBits(self):
        return self._pcSystemEsBits
    
    @pcSystemEsBits.setter
    def pcSystemEsBits(self,value):
        self._pcSystemEsBits = value

    @property
    def pcSystemModel(self):
        return self._pcSystemModel
    
    @pcSystemModel.setter
    def pcSystemModel(self,value):
        self._pcSystemModel = value
       
    @property
    def pcSystemNumberSystem(self):
        return self._pcSystemNumberSystem
    
    @pcSystemNumberSystem.setter
    def pcSystemNumberSystem(self,value):
        self._pcSystemNumberSystem = None
        if value == "Fixed":
            self._pcSystemNumberSystem = 0
        elif value == "Float":
            self._pcSystemNumberSystem = 1
        elif value == "Posit":
            self._pcSystemNumberSystem = 2

        
    @property
    def pcSystemType(self):
        return self._pcSystemType

    @pcSystemType.setter
    def pcSystemType(self,value):
        # set the value of the systemType
        self._pcSystemType = value
        # set  the category number name map
        # set the fileSystem systemType
        if value == "AC":
            self._pcSystemType = 0
        elif value == "SPN":
            self._pcSystemType = 1

    def main(self):
        pass

    def run(self):
        pass
