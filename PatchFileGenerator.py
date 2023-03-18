from Git import Git
import os

class PatchFileGenerator:
    '''
    This class is used to create a zip file,
      which contains the neccessary .dll and .exe as per changes in implementation.
    '''
    def __init__(self, repo:str, branch:str, comparetobranch:str ="main-5.5") -> None:
        self.git= Git(branch, repo, comparetobranch)
        self.tempfolder="C:/temp"
        self.binarypath="/bin/debug/net48"
        self.chaintobinary=dict()

    def __createfolder__(self, branchName) -> None:
        try:
            os.mkdir(branchName)
        except:
            return

    def __fillchain__(self):
        files= self.__getchangedfilenames__(self).split("\n")
        for file in files:
            names=file.split("/")
            n=0
            current=self.chaintobinary
            for name in names:
                if name in current:
                    current=current[name]
                else:
                    current[name]=dict() 


    def __getchangedfilenames__(self)->list:
        return self.git.getfileschangedforbranch()


    def __locatebinary__(self, chain, path) -> str:
        fullpath = os.path.join(path,self.binarypath)
        if os.path.isdir(fullpath):
            self.__copybinarytofolder__(fullpath)
            return

        for key,value in chain:
            self.__locatebinary__(value, os.path.join(path, key))



    def __copybinarytofolder__(self, filepath:str) -> None:
        

        pass


    def createzipfolder(self) -> str:
        pass

    
           

