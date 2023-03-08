from Git import Git
import os

class EngineeringBuildGenerator:
    '''
    This class is used to create a zip file,
      which contains the neccessary .dll and .exe as per changes in implementation.
    '''
    def __init__(self, repo:str, branch:str, comparetobranch:str ="main-5.5") -> None:
        self.git= Git(branch, repo, comparetobranch)


    def __createfolder_(self, branchName) -> None:
        pass


    def __getchangedfilenames__(self)->list:
        return self.git.getfileschangedforbranch()


    def __locatebinaryfromfilename__(self,filename:str) -> str:
        pass


    def __copybinarytofolder__(self, filepath:str) -> None:
        pass


    def createzipfolder(self) -> str:
        pass

    
           

