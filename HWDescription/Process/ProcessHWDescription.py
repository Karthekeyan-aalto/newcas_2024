"""
Created by Karthekeyan Periasamy
Edited on Feb 9 21:11
"""

from HWDescription.Entity.EntityHWDescription import EntityHWDescription

class ProcessHWDescription(EntityHWDescription):

    def __init__(self):
        """
        This class needs to be thought through again
        """
        self.connect()


    """
    Start: Custom Setters and Getters
    """
    @property
    def pythonHWIOStimulusProcessInfo(self):
        return self._pythonHWIOStimulusProcessInfo

    @pythonHWIOStimulusProcessInfo.setter
    def pythonHWIOStimulusProcessInfo(self,value):
        self._pythonHWIOStimulusProcessInfo = value
        # process the dictionary information
    
    
    def connect(self):
        super().connect()

    def connectProperties(self):
        super().connectProperties()
        self.sensitivityList = None
        self.processSensitivityList = None
        self.pythonHWPipelineStagesInfo = None
        self.pythonHWPipelineStagesProcessInfo = None
        self.pythonHWPipelineStagesAsyncResetProcessInfo = None
        self.pythonHWPipelineStages = None
        self.pythonHWProcess = None
        self.pythonHWResetName = None
        self.pythonHWResetInfo = None

        # the pythonHWClockProcess Info has the details that will be used to process and make pythonHWClockProcess
        self._pythonHWClockProcessInfo = None
        self.pythonHWClockProcess = None
        self.pythonHWEnableName = None
        self.pythonHWClockProcessName = None
        self.pythonHWIOStimulusProcessName = "ioStimulus"
        self.pythonHWIOStimulusProcess = None
        # the pythonHWIOStimulusProcess Info has the details that will be used to process and make the pythonHWIOStimulusProcess
        self._pythonHWIOStimulusProcessInfo = None


    def configure(self):
        super().configure()
        if self.configurationDetailsOfHW == None:
            return
       
        # set the configuration details temporary
        configurationDetails = self.configurationDetailsOfHW
        # print the configuration details
        #print("Configuration Details of the HW Process", configurationDetails)

        # check the sensitivity list array
        if "SensitivityList" in configurationDetails:
            processSensitivityListString = str()
            sensitivityListItems = configurationDetails["SensitivityList"]
            self.sensitivityList = sensitivityListItems
            for sensitivityListIndex, sensitivityListItem in enumerate(sensitivityListItems):
                if sensitivityListIndex == (len(sensitivityListItems)-1):
                    processSensitivityListString = processSensitivityListString + sensitivityListItem
                else:
                    processSensitivityListString = processSensitivityListString + sensitivityListItem + ","
                
         # set the local process sensitivity list to a global variable
        self.processSensitivityList = processSensitivityListString

        if "NumberOfPipelineStages" in configurationDetails:
            self.pythonHWPipelineStages = configurationDetails["NumberOfPipelineStages"]
           
        # access the configuration details
        if "PythonHWProcessInfo" in configurationDetails:
            if configurationDetails["PythonHWProcessInfo"] != None:
                self.pythonHWProcess = configurationDetails["PythonHWProcessInfo"]
            
        elif "PythonHWPipelineStagesInfo" in configurationDetails:
            self.pythonHWPipelineStagesInfo = conigurationDetails["PythonHWPipelineStagesInfo"]
            if "PythonHWPipelineStagesAsyncResetProcessInfo" in configurationDetails:
                self.pythonHWPipelineStagesAsyncResetProcessInfo = configurationDetails["PythonHWPipelineStagesAsyncResetProcessInfo"]
            

        if "PythonHWClockProcessInfo" in configurationDetails:
            # check if the info is None or not
            if configurationDetails["PythonHWClockProcessInfo"] != None:
                self.pythonHWClockProcessInfo = configurationDetails["PythonHWClockProcessInfo"]
                
                self.pythonHWClockName = self.pythonHWClockProcessInfo["ClockPortName"]

                # access the frequency
                self.pythonHWClockProcessFrequency = self.pythonHWClockProcessInfo["Frequency"]
       
                # access the name of the clock
                self.pythonHWClockProcessName = self.pythonHWClockProcessInfo["ClockStimulusName"]

                # process the frequency
                # change the frequency to nanoseconds
                time = 1/(int(self.pythonHWClockProcessFrequency)*1000000)
                
                self.pythonHWClockProcessTime = time * 1000000000
        
        
        if "PythonHWResetInfo" in configurationDetails:
            # check if the info is None or not
            if configurationDetails["PythonHWResetInfo"] != None:
                self.pythonHWResetInfo = configurationDetails["PythonHWResetInfo"]
                self.pythonHWResetName = self.pythonHWResetInfo["ResetPortName"]
        
        if "PythonHWEnableInfo" in configurationDetails:
            # check if the info is None or not
            if configurationDetails["PythonHWEnableInfo"] != None:
                self.pythonHWEnableInfo = configurationDetails["PythonHWEnableInfo"]
                self.pythonHWEnableName = self.pythonHWEnableInfo["EnablePortName"]
        
        if "PythonHWIOStimulusProcessInfo" in configurationDetails:
            # check if the info is none or not
            if configurationDetails["PythonHWIOStimulusProcessInfo"] != None:
                self.pythonHWIOStimulusProcessInfo = configurationDetails["PythonHWIOStimulusProcessInfo"]

            if "InputDataPorts" in configurationDetails["PythonHWIOStimulusProcessInfo"]:
                self.pythonHWInputPorts = configurationDetails["PythonHWIOStimulusProcessInfo"]["InputDataPorts"]


            if "OutputDataPorts" in configurationDetails["PythonHWIOStimulusProcessInfo"]:
                self.pythonHWOutputPorts = configurationDetails["PythonHWIOStimulusProcessInfo"]["OutputDataPorts"]

               
        

    def process(self):
        pass

    def main(self):
        pass

    def reset(self):
        self.resetProperties()

    def resetProperties(self):
        super().resetProperties()
        self.sensitivityList = None
        
        self.processSensitivityList = None
        self.pythonHWPipelineStagesInfo = None
        self.pythonHWResetInfo = None
        self.pythonHWPipelineStagesProcessInfo = None
        self.pythonHWPipelineStagesAsyncResetProcessInfo = None
        self.pythonHWPipelineStages = None
        self.pythonHWProcess = None
        self.pythonHWResetName = None

        # the pythonHWClockProcess Info has the details that will be used to process and make pythonHWClockProcess
        self._pythonHWClockProcessInfo = None
        self.pythonHWClockName = None
        self.pythonHWClockProcessFrequency = None
        self.pythonHWClockProcessName = None
        self.pythonHWClockProcessTime = None
        self.pythonHWIOStimulusProcessName = "ioStimulus"
        # the pythonHWIOStimulusProcess Info has the details that will be used to process and make the pythonHWIOStimulusProcess
        self._pythonHWIOStimulusProcessInfo = None

    def run(self):
        self.main()

