"""
Edited by Karthekeyan Periasamy
Edited on October 22, 2023 13.07
"""

class PCEquationFileConfiguration():

    def __init__(self):
        self.connectProperties()


    def connectProperties(self):
        self._equation = None
        self._equationFileName = None

    def configure(self):
        self.configureFileConfiguration()

    def configureFileConfiguration(self):
        self.pcEquationFileConfiguration = PCEquationFileConfiguration()


    def process(self):
        pass

    def perform(self):
        pass

    def reset(self):
        pass

    def main(self):
        self.proces()
        self.perform()

    def run(self):
        self.main()

