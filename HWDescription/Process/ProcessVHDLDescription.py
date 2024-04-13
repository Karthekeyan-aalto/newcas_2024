"""
Created by Karthekeyan Periasamy
Edited on Feb 9 21:18
"""

from HWDescription.Variables.Variable.VariableVHDLDescription import VariableVHDLDescription
from HWDescription.File.FileVHDLDescription import FileVHDLDescription
from HWDescription.Process.ProcessHWDescription import ProcessHWDescription

class ProcessVHDLDescription(ProcessHWDescription):

    def __init__(self):
        self.connect()

    def connect(self):
        super().connect()
        self.connectProperties()
        self.connectHWVHDLPackages()

    def connectProperties(self):
        super().connectProperties()
       
        self.vhdlEntityProcessDefinition = None
        self.vhdlEntityTBProcessDefinition = None
        self.vhdlProcessKeyWord = "PROCESS"
        self.vhdlTBClockProcess = None
        self.vhdlTBIOStimulusProcess = None
        self._vhdlProcessDefinitionAsyncResetStartSyntax = None
        self._vhdlProcessDefinitionAsyncResetEndSyntax = None
        self._vhdlProcessDefinitionRisingEdgeClockStartSyntax = None
        self._vhdlProcessDefinitionStartSyntax = None
        self._vhdlProcessDefinitionEndSyntax = None
        self._vhdlProcessVariables = None
        self._vhdlProcessIOStimulusFiles = None
        self._vhdlProcessIOStimulusVariables = None


    

    def connectHWVHDLPackages(self):
        self.hwProcessVariableVHDLDescription = VariableVHDLDescription()
        
    def configure(self):
        super().configure()
    
    def main(self):
        super().main()
        self.process()
        self.perform()

    def reset(self):
        self.resetProperties()

    def run(self):
        self.main()
    
    @property
    def vhdlProcessVariables(self):
        if self._vhdlProcessVariables == None:
            self._vhdlProcessVariables = list()
        return self._vhdlProcessVariables
    
    @vhdlProcessVariables.setter
    def vhdlProcessVariables(self,value):
        self._vhdlProcessVariables = value
    
    @property
    def vhdlProcessIOStimulusVariables(self):
        if self._vhdlProcessIOStimulusVariables == None:
            self._vhdlProcessIOStimulusVariables = list()
        return self._vhdlProcessIOStimulusVariables
    
    @vhdlProcessIOStimulusVariables.setter
    def vhdlProcessIOStimulusVariables(self,value):
        self._vhdlProcessIOStimulusVariables = value
    
    
    @property
    def vhdlProcessIOStimulusFiles(self):
        if self._vhdlProcessIOStimulusFiles == None:
            self._vhdlProcessIOStimulusFiles = list()
        return self._vhdlProcessIOStimulusFiles
    
    @vhdlProcessIOStimulusFiles.setter
    def vhdlProcessIOStimulusFiles(self,value):
        self._vhdlProcessIOStimulusFiles = value

    @property
    def vhdlProcessDefinitionStartSyntax(self):
        if self._vhdlProcessDefinitionStartSyntax == None:
            # check whether the sensitivity list there or not
            if self.processSensitivityList == None:
                self._vhdlProcessDefinitionStartSyntax = (self.vhdlProcessKeyWord + " " + "IS" + "\n" + "    "+"BEGIN" + " \n")
            else:
                self._vhdlProcessDefinitionStartSyntax = (self.vhdlProcessKeyWord + " " + "(" + self.processSensitivityList + ")" + " " + "IS" + "\n" + "    " + "BEGIN" + " \n")

        return self._vhdlProcessDefinitionStartSyntax
    
    @vhdlProcessDefinitionStartSyntax.setter
    def vhdlProcessDefinitionStartSyntax(self,value):
        self._vhdlProcessDefinitionStartSyntax = value
   
    
    @property
    def vhdlProcessDefinitionEndSyntax(self):
        if self._vhdlProcessDefinitionEndSyntax == None:
            self._vhdlProcessDefinitionEndSyntax = ("    "+"END" + " " + "PROCESS" + ";" + "\n")
        return self._vhdlProcessDefinitionEndSyntax
    
    @vhdlProcessDefinitionEndSyntax.setter
    def vhdlProcessDefinitionEndSyntax(self,value):
        self._vhdlProcessDefinitionEndSyntax = value
    

    @property
    def vhdlProcessDefinitionAsyncResetStartSyntax(self):
        if self._vhdlProcessDefinitionAsyncResetStartSyntax == None:
            self._vhdlProcessDefinitionAsyncResetStartSyntax = ("        " + "IF" + " " + self.pythonHWResetName + " " + "=" + " " + "'1'" + " " + "THEN" + "\n")

        return self._vhdlProcessDefinitionAsyncResetStartSyntax
    
    @vhdlProcessDefinitionAsyncResetStartSyntax.setter
    def vhdlProcessDefinitionAsyncResetStartSyntax(self,value):
        self._vhdlProcessDefinitionAsyncResetStartSyntax = value
    
    
    @property
    def vhdlProcessDefinitionAsyncResetEndSyntax(self):
        if self._vhdlProcessDefinitionAsyncResetEndSyntax == None:
            self._vhdlProcessDefinitionAsyncResetEndSyntax = ("        " + "END IF" + ";" + "\n")

        return self._vhdlProcessDefinitionAsyncResetEndSyntax
    
    @vhdlProcessDefinitionAsyncResetEndSyntax.setter
    def vhdlProcessDefinitionAsyncResetEndSyntax(self,value):
        self._vhdlProcessDefinitionAsyncResetEndSyntax = value
    
    
    @property
    def vhdlProcessDefinitionRisingEdgeClockStartSyntax(self):
        if self._vhdlProcessDefinitionRisingEdgeClockStartSyntax == None:
            print(self.pythonHWEnableName)
            print(self.pythonHWResetName)
            self._vhdlProcessDefinitionRisingEdgeClockStartSyntax = ("        " + "ELSIF" + " " + "rising_edge" + "(" + self.pythonHWClockName + ")" + " " + "and" + " " + self.pythonHWResetName + " " + "=" + " " + "'0'" + " " + "and" + " " + self.pythonHWEnableName + " " + "=" + " " + "'1'" + " " + "THEN" + "\n")

        return self._vhdlProcessDefinitionRisingEdgeClockStartSyntax
    
    @vhdlProcessDefinitionRisingEdgeClockStartSyntax.setter
    def vhdlProcessDefinitionRisingEdgeClockStartSyntax(self,value):
        self._vhdlProcessDefinitionRisingEdgeClockStartSyntax = value
    
    
    
    def process(self):
        self.processPythonHWPipelineStages()
        self.processPythonHWIOStimulusProcess()
        #pythonHWPipelineStagesProcessInfo

    
    def processPythonHWIOStimulusProcess(self):
        # access the IOStimulus info dictionary
        # configure each information using the dictionary details
        if self.pythonHWIOStimulusProcessInfo == None:
            return

        # access the variable info from the python HWIO Stimulus
        pythonHWIOStimulusProcessVariables = self.pythonHWIOStimulusProcessInfo["PythonHWProcessVariablesInfo"]
        
        # loop through the variable info
        for pythonHWIOStimulusProcessVariable in pythonHWIOStimulusProcessVariables:
            # access the information of the variable from the pythonHWIOStimulus process variable
            variableVHDLDescription = VariableVHDLDescription()
            variableVHDLDescription.configurationDetailsOfHWVariable = pythonHWIOStimulusProcessVariable
            variableVHDLDescription.configure()
            variableVHDLDescription.process()
            variableVHDLDescription.perform()

            # check the type of the variable
            if variableVHDLDescription.vhdlVariableIEEENameType == 2:
                self.vhdlProcessVariableInputBufferName = variableVHDLDescription.name
                self.vhdlProcessVariableIEEENameOutputConverter = variableVHDLDescription.vhdlVariableIEEENameOutputConverter
            elif variableVHDLDescription.vhdlVariableIEEENameType == 3:
                self.vhdlProcessVariableCommaBufferName = variableVHDLDescription.name
                self.vhdlProcessVariableIEEENameOutputConverter = variableVHDLDescription.vhdlVariableIEEENameOutputConverter

            self.vhdlProcessIOStimulusVariables.append(variableVHDLDescription)
        
        # print the length of the processIOStimulusVariables
        #print("The length of the Process IO Stimulus Variables", len(self.vhdlProcessIOStimulusVariables))
        
        # loop through the variable info
        pythonHWIOStimulusProcessFiles = self.pythonHWIOStimulusProcessInfo["PythonHWProcessFileInfo"]
        
        # loop through the process variable file info
        for pythonHWIOStimulusProcessFile in pythonHWIOStimulusProcessFiles:
            # access the information of the variable from the pythonHWIOStimulus process files
            fileVHDLDescription = FileVHDLDescription()
            fileVHDLDescription.configurationDetailsOfHWFile = pythonHWIOStimulusProcessFile
            fileVHDLDescription.configure()
            fileVHDLDescription.process()
            fileVHDLDescription.perform()

            self.vhdlProcessIOStimulusFiles.append(fileVHDLDescription)
        
        # print the length of the processIOStimulusFiles
        #print("The length of the Process IO Stimulus File", len(self.vhdlProcessIOStimulusFiles)) 

    def processPythonHWPipelineStages(self):
        if (self.pythonHWPipelineStages != None):
            if (self.pythonHWPipelineStages > 0):
                pass
    
    def perform(self):
        self.generateHWProcess()
        self.generateHWTBClockProcess()
        self.generateHWTBIOStimulusProcess()
    
    def generateHWTBClockProcess(self):
        # generate the hardware testbench clock process
        self.vhdlTBClockProcess = self.pythonHWClockProcessName + ":" + " " + self.vhdlProcessKeyWord + " " + "IS"  + "\n" \
                         "BEGIN" + "\n" \
                         "     " + self.pythonHWClockName + " " + "<=" + " " + "'0'" + ";" + "\n" \
                         "     " + "WAIT FOR" + " " + str(self.pythonHWClockProcessTime) + " " + "ns" + ";" + "\n" \
                         "     " + self.pythonHWClockName + " " + "<=" + " " + "'1'" + ";" + "\n" \
                         "     " + "WAIT FOR" + " " + str(self.pythonHWClockProcessTime) + " " + "ns" + ";" + "\n" \
                         "END PROCESS" + " " + self.pythonHWClockProcessName + " " + ";" + "\n" \

    
    def generateHWTBIOStimulusProcess(self):

        # initialise the vhldIOStimulusVariables and Files
        vhdlIOStimulusVariablesAndFiles = str()
        
        # initialise the variable to store the process file input name
        vhdlProcessFileInputName = str()
        # intialise the variable to store the process file output name
        vhdlProcessFileOutputName = str()
        # initialise the variable to store the variable input buffer name
        vhdlProcessVariableInputBufferName = str()
        # intialise the variable to store the process variable ieee name output converter
        vhdlProcessVariableIEEENameOutputConverter = str()
        # intialise the process variable comma buffer name
        vhdlProcessVariableCommaBufferName = str()
        # intialise the prcess variable name output converter
        vhdlProcessVariableIEEENameOutputConverter = str()
        
        # start processing the tb io stimulus 
        vhdlIOStimulusVariablesAndFiles = self.pythonHWIOStimulusProcessName + ":" + " " + self.vhdlProcessKeyWord + " " + "IS"  + "\n" \
                         
        # append the files and variables
        for vhdlIOStimulusVariable in self.vhdlProcessIOStimulusVariables:
            vhdlIOStimulusVariablesAndFiles = vhdlIOStimulusVariablesAndFiles + "    " + vhdlIOStimulusVariable.vhdlDescription
            
            # check the type of the variable
            if vhdlIOStimulusVariable.vhdlVariableIEEENameType == 2:
                vhdlProcessVariableInputBufferName = vhdlIOStimulusVariable.name
                vhdlProcessVariableIEEENameOutputConverter = vhdlIOStimulusVariable.vhdlVariableIEEENameOutputConverter
            elif vhdlIOStimulusVariable.vhdlVariableIEEENameType == 3:
                vhdlProcessVariableCommaBufferName = vhdlIOStimulusVariable.name
                vhdlProcessVariableIEEENameOutputConverter = vhdlIOStimulusVariable.vhdlVariableIEEENameOutputConverter
        
        #print("Length of VHDLProcess IO Stimulus Variables", len(self.vhdlProcessIOStimulusVariables))
        
        # append the files and variables
        for vhdlIOStimulusFile in self.vhdlProcessIOStimulusFiles:
            vhdlIOStimulusVariablesAndFiles = vhdlIOStimulusVariablesAndFiles + "    " + vhdlIOStimulusFile.vhdlDescription
            
            # check the mode and set the VHDL readMode and VHDL writeMode fileNames
            if vhdlIOStimulusFile.mode == 1:
                vhdlProcessFileInputName = vhdlIOStimulusFile.name
            elif vhdlIOStimulusFile.mode == 2:
                vhdlProcessFileOutputName = vhdlIOStimulusFile.name
        
        #print("Length of VHDLProcess IO Stimulus Files", len(self.vhdlProcessIOStimulusFiles))
        vhdlIOStimulusVariablesAndFiles = "\n\n" + vhdlIOStimulusVariablesAndFiles + "BEGIN" + "\n\n"

        # bein the process after the addition of the variables and files
        vhdlIOStimulusVariablesAndFiles = (vhdlIOStimulusVariablesAndFiles + "     " + "WHILE" + " " + "NOT" + " " + "endfile" + " " + "(" + vhdlProcessFileInputName + ")" \
                                          + " " + "LOOP" + "\n\n"\
                                          + "        " + "readline" + " " + "(" + vhdlProcessFileInputName + "," + "fileline" + ")" + ";" \
                                          +"\n\n")

        for inputDataPort in self.pythonHWInputPorts:
            # access the information of the inputdata port
            vhdlIOStimulusVariablesAndFiles = vhdlIOStimulusVariablesAndFiles + "        " + "read" + " " + "(" + "fileline" + "," \
                                              + vhdlProcessVariableInputBufferName + ")" + ";" + "\n" \
                                              
            # access the name of the input data port
            portName = inputDataPort.name
            
            vhdlIOStimulusVariablesAndFiles = vhdlIOStimulusVariablesAndFiles + "        " + portName + " " + "<=" + " " \
                                              +  vhdlProcessVariableInputBufferName +";" + "\n\n" \

            vhdlIOStimulusVariablesAndFiles = vhdlIOStimulusVariablesAndFiles +  "        " + "read" + " " + "(" + "fileline" + "," \
                                              + vhdlProcessVariableCommaBufferName + ")" + ";" + "\n\n" \

        
        vhdlIOStimulusVariablesAndFiles = vhdlIOStimulusVariablesAndFiles + "        " + "WAIT FOR" + " " + str(self.pythonHWClockProcessTime) + " " + "ns" + ";" + "\n\n"

        
        # use for loop to generate the output
        for outputPort in self.pythonHWOutputPorts:
            vhdlIOStimulusVariablesAndFiles = vhdlIOStimulusVariablesAndFiles + "        " + "write" + "(" + "fileline" + "," + vhdlProcessVariableIEEENameOutputConverter + "(" + outputPort.name + ")" + ")" + ";" + "\n"
            
            vhdlIOStimulusVariablesAndFiles = vhdlIOStimulusVariablesAndFiles + "        " + "writeline" + "(" + vhdlProcessFileOutputName + "," + "fileline" + ")" + ";" + "\n\n"
            
        
        vhdlIOStimulusVariablesAndFiles = vhdlIOStimulusVariablesAndFiles + "        " + "END LOOP" + ";" + "\n\n"

        
        # loop through the io stimulus files to access the file close description
        for ioStimulusFile in self.vhdlProcessIOStimulusFiles:
            vhdlIOStimulusVariablesAndFiles = vhdlIOStimulusVariablesAndFiles + "        " + ioStimulusFile.vhdlFileCloseDescription

        vhdlIOStimulusVariablesAndFiles = vhdlIOStimulusVariablesAndFiles + "        " + "WAIT" + ";" + "\n\n"
        vhdlIOStimulusVariablesAndFiles = vhdlIOStimulusVariablesAndFiles + "END PROCESS" + ";" + "\n"

        self.vhdlTBIOStimulusProcess = vhdlIOStimulusVariablesAndFiles

        # the above property needs to be updated to accomodate the ports and closing of the TB IO Stimulus process
        # print the vhdlIOStimulus Variables and Files
        #print("VHDL IO Stimulus Variables and Files Description", self.vhdlTBIOStimulusProcess)


    def generateHWProcess(self):

        if self.pythonHWProcess == None and self.pythonHWPipelineStagesInfo == None:
            self.vhdlEntityProcessDefinition = self.vhdlProcessDefinitionStartSyntax \
                + "\n" + self.vhdlProcessDefinitionEndSyntax
            return

        if self.pythonHWProcess != None:
            self.vhdlEntityProcessDefinition = self.vhdlProcessDefinitionStartSyntax \
                + "    " + self.pythonHWProcess \
                + "\n" + self.vhdlProcessDefinitionEndSyntax
                
        elif self.pythonHWPipelineStages != None:
            if self.pythonHWPipelineStages > 0:
                self.vhdlEntityProcessDefinition = self.vhdlProcessDefinitionStartSyntax \
                        + "    " + self.vhdlProcessDefinitionAsyncResetStartSyntax \
                        + "    " + self.pythonHWPipelineStagesAsyncResetProcessInfo \
                        + "    " + self.vhdlProcessDefinitionRisingEdgeClockStartSyntax   \
                        + "    " + self.pythonHWPipelineStagesProcessInfo \
                        + "    " + self.vhdlProcessDefinitionAsyncResetEndSyntax   \
                        + "\n" + self.vhdlProcessDefinitionEndSyntax
    
    
    def generateHWTBProcess(self):
        self.vhdlEntityTBProcessDefinition = self.vhdTBClockProcess + self.vhdlTBIOStimulusProcess
    
    
    def resetProperties(self):
        self.vhdlProcessKeyWord = "PROCESS"
        self._vhdlProcessDefinitionStartSyntax = None
        self._vhdlProcessDefinitionEndSyntax = None
        self._vhdlProcessDefinitionAsyncResetStartSyntax = None
        self._vhdlProcessDefinitionAsyncResetEndSyntax = None
        self._vhdlProcessDefinitionRisingEdgeClockStartSyntax = None
        self.vhdlEntityProcessDefinition = None
        self.vhdlEntityTBProcessDefinition = None
        self.vhdlTBClockProcess = None
        self._vhdlProcessIOStimulusFiles = None
        self.vhdlTBIOStimulusProcess = None
        self._vhdlProcessVariables = None
