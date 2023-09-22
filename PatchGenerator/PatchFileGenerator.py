from Git.Git import Git
import os
import shutil

class PatchFileGenerator:
    '''
    This class is used to create a zip file,
      which contains the neccessary binaries as per changes in implementation.
    '''
    def __init__(self, repo:str, branch:str, comparetobranch:str ="main-5.5") -> None:
        self.git= Git(branch, repo, comparetobranch)
        self.tempfolder="C:/temp"
        self.binarypath="bin\\debug\\net48"
        self.chaintobinary=dict()

    def __createfolder__(self) -> None:
        try:
            self.dest=os.path.join(self.tempfolder,self.git.my_branch)
            if os.path.isdir(self.dest):
                shutil.rmtree(self.dest)
            os.mkdir(self.dest)
        except:
            print("Folder is not deleted,")
            print(f"ensure to delete folder {self.dest} then try again.")

    def __fillchain__(self):
        files= self.__getchangedfilenames__()
        for file in files:
            names=file.split("/")
            n=0
            current=self.chaintobinary
            for name in names:
                if name not in current.keys():
                    current[name]=dict() 
                current=current[name]


    def __getchangedfilenames__(self)->list:
        return self.git.getfileschangedforbranch()


    def __locatebinary__(self, chain: dict, path:str) -> None:
        #path= path.split(":")[-1]
        fullpath = os.path.join(path, self.binarypath)
        if os.path.isdir(fullpath):
            self.__copyfiletofolder__(fullpath)
            return

        for key,value in chain.items():
            self.__locatebinary__(value, os.path.join(path, key))



    def __copyfiletofolder__(self, dir_name:str) -> None:
        # Get list of all files only in the given directory
        list_of_files = filter( lambda x: os.path.isfile(os.path.join(dir_name, x)) and (x.endswith(".dll") or x.endswith(".exe")), os.listdir(dir_name) )
        # Sort list of files based on last modification time in decending order
        list_of_files = sorted( list_of_files, key = lambda x: os.path.getmtime(os.path.join(dir_name, x)), reverse=True)

        shutil.copy(os.path.join(dir_name, list_of_files[0]), self.dest)


    def createzipfile(self) -> None:
        self.__fillchain__()
        self.__createfolder__()
        self.__locatebinary__(self.chaintobinary, self.git.dir)
        shutil.make_archive(self.dest, 'zip', self.dest)
        print(f"Zip file created at \"{self.dest}\".")

    
           

