"""
Created by Karthekeyan Periasamy
Edited on January 8, 2023, 13:34
"""

from HWDescription.Process.ProcessVHDLDescription import ProcessVHDLDescription

class PositMultiplierProcessVHDLDescription(ProcessVHDLDescription):

    def __init__(self):
        super().__init__()
        
    
    def connectProperties(self):
        super().connectProperties()
        self.pythonHWPipelineStagesProcessInfoString = None


    def resetProperties(self):
        super().resetProperties()
        self.pythonHWPipelineStagesProcessInfoString = None
    
    def process(self):
        super().process()
    

    def configure(self):
        super().configure()
        # print the clock process info dictionary
        #print("HW Clock Process Info after being configured",self.pythonHWClockProcessInfo)

        if self.configurationDetailsOfHW == None:
            return


    def connectHWVHDLPackages(self):
        super().connectHWVHDLPackages()
        

    def processPythonHWPipelineStages(self):
        if (self.pythonHWPipelineStages != None):
            if (self.pythonHWPipelineStages > 0):
                # use the pythonHWPipelineStagesProcessInfo
                if self.pythonHWPipelineStagesProcessInfo != None:
                    # set the variable of the vhdl description about the python hw info
                    # though this info will only have string version pythonHWPipleStagesInfo
                    self.pythonHWPipelineStagesProcessInfoString = str()
                    # process the dictionary of the python hw pipeline stages process info
                    for level in self.pythonHWPipelineStagesProcessInfo.keys():
                        # access the array information from the pipelinstages info
                        processInfoPerLevel = self.pythonHWPipelineStagesProcessInfo[level]
                        for index,info in enumerate(processInfoPerLevel):
                            if index == len(processInfoPerLevel)-1:
                                self.pythonHWPipelineStagesProcessInfoString = self.pythonHWPipelineStagesProcessInfoString + info + "\n"
                            else:
                                self.pythonHWPipelineStagesProcessInfoString = self.pythonHWPipelineStagesProcessInfoString + info + "\n" + "            "
                        
    
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
                        + self.vhdlProcessDefinitionAsyncResetStartSyntax \
                        + self.vhdlProcessDefinitionRisingEdgeClockStartSyntax   \
                        + "            " + self.pythonHWPipelineStagesProcessInfoString \
                        + self.vhdlProcessDefinitionAsyncResetEndSyntax   \
                        + "\n" + self.vhdlProcessDefinitionEndSyntax    
        
    def main(self):
        super().main()
    

    def perform(self):
        super().perform()

    def run(self):
        self.main() 
