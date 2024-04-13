"""
Created by Karthekeyan Periasamy
Edited on Jan 30 20:39
"""

class Library(self):

    def __init__(self):
        # property to store the name of the library where the associated files will be compiled
        self.name = None
        # property to store the configuraiton details of the library
        # configuration details will have the libraries and their respective files in the form of 
        # a key value pair, where the key will be the library name and the value will be the array of file names
        self.configurationDetails = None
        # property to store the files of the library
        # the files is an array of string with file path
        self.files = None

    
    def configure(self):
        if self.configurationDetails = None:
            return

        configurationDetails = self.configurationDetails

        # check the name of the library is there or not
        if "Name" in configurationDetails:
            self.name = configurationDetails["Name"]

        # check the files key of the library 
        if "Files" in configurationDetails:
            self.files = configurationDetails["Files"]


    def main(self):
        pass

    def run(self):
        pass
