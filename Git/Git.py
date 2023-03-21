import subprocess
import shlex
import os

class  Git:

    PIPE = subprocess.PIPE
    filesChanged = dict()

    def __init__(self, my_branch:str, repo:str = os.getcwd(), main_branch:str="main-5.5"):
        self.my_branch = my_branch
        self.main_branch = main_branch
        self.dir = os.getcwd()
        self.changecwd(repo)
        self.__fillcommits__()


    def setdirectory(self,dir:str):
        if os.getcwd() == dir:
            return
        os.chdir(dir)
        self.dir=dir


    def changecwd(self,dir:str):
        try:
            self.setdirectory(dir)
        except:
            os.chdir(self.dir)
            print("directory change failed or repository not exist")

    def __executecommand__(self, command:str)->str:
        process = subprocess.Popen(shlex.split(command), stdout=self.PIPE, stderr=self.PIPE)
        stdoutput, stderroutput = process.communicate()
        if 'fatal' in stdoutput.decode():
            raise Exception("Error occured while executing command!!!")
        else:
            return stdoutput.decode()


    def __gitlog__(self) -> str:
        command=f"git log {self.main_branch}..{self.my_branch} --grep=\"{self.my_branch.split('_')[0]}\""
        return self.__executecommand__(command)


    def __fillcommits__(self):
        commitchunks = self.__gitlog__().split("commit ")
        self.commitIds= list()
        for commit in commitchunks:
            lines= commit.split("\n")
            if len(lines)<2 or len(lines[0])<5:
                continue
            self.commitIds.append((lines[0], not lines[1].startswith("Merge")))


    def getlastcommit(self):
        return self.__gitlog__(1)
        
    def getcommits(self):
        return self.commitIds
    

    def getchangedfilesforcommit(self,commit):
        cmd=f"git show {commit} --name-only --pretty=\"\""
        return self.__executecommand__(cmd)



    def getfileschangedforbranch(self):
        cmd=f"git diff {self.main_branch}..{self.my_branch} --name-only"
        files=list()
        for filename in self.__executecommand__(cmd).split("\n"):
            if len(filename)>0:
                files.append(filename)
        return files
        