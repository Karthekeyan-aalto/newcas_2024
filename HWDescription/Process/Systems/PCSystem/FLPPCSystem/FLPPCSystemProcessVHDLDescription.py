"""
Created by Karthekeyan Periasamy
Edited on September 7, 2023, 10:53
"""

from HWDescription.Process.Systems.PCSystem.PCSystemProcessVHDLDescription import PCSystemProcessVHDLDescription

class FLPPCSystemProcessVHDLDescription(PCSystemProcessVHDLDescription):

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
                #print("Python HW Pipeline Stages Process Info", self.pythonHWPipelineStagesProcessInfo)
                # use the pythonHWPipelineStagesProcessInfo
                if self.pythonHWPipelineStagesProcessInfo != None:
                    #print("Python HW Pipeline Stages Process Info", self.pythonHWPipelineStagesProcessInfo)
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
                        
    
    @property
    def vhdlProcessDefinitionRisingEdgeClockStartSyntax(self):
        if self._vhdlProcessDefinitionRisingEdgeClockStartSyntax == None:
            self._vhdlProcessDefinitionRisingEdgeClockStartSyntax = ("        " + "ELSIF" + " " + "rising_edge" + "(" + self.pythonHWClockName + ")" + " " + "and" + " " + self.pythonHWResetName + " " + "=" + " " + "'0'" + " " + "and" + " " + self.pythonHWEnableName + " " + "=" + " " + "'1'" + " " + "THEN" + "\n")

        return self._vhdlProcessDefinitionRisingEdgeClockStartSyntax
    
    @vhdlProcessDefinitionRisingEdgeClockStartSyntax.setter
    def vhdlProcessDefinitionRisingEdgeClockStartSyntax(self,value):
        self._vhdlProcessDefinitionRisingEdgeClockStartSyntax = value
    
   
    
    def main(self):
        super().main()
    

    def perform(self):
        super().perform()

    def run(self):
        self.main() 
