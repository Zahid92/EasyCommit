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
       # process = subprocess.run(shlex.split(f"git log {self.main_branch}..{self.my_branch}"))
        command=f"git log {self.main_branch}..{self.my_branch} --grep=\"{self.my_branch.split('_')[0]}\""
        return self.__executecommand__(command)


    def fillcommits(self):
        commitchunks = self.__gitlog__().split("commit ")
        self.commitIds= list()
        for commit in commitchunks:
            lines= commit.split("\n")
            if len(lines)<2 or len(lines[0])<5:
                continue
            self.commitIds.append((lines[0], not lines[1].startswith("Merge")))


    def getlastcommit(self):
        return self.__gitlog__(1)
    

    def fillchangedfilesforcommits(self):
        for index in range(0,len(self.commitIds)):
            cmd=f"git show {self.commitIds[index][0]} --name-only --pretty=\"\""
            self.filesChanged[self.commitIds[index][0]] = self.__executecommand__(cmd)

        
    def getcommits(self):
        return self.commitIds
    

    def getchangedfilesforcommit(self,commit):
        if commit in self.filesChanged:
            return self.filesChanged[commit]
        else: 
            return "CommitId Not Found."


    def getfileschangedforbranch(self):
        cmd=f"git diff {self.main_branch}..{self.my_branch} --name-only"
        files=list()
        for filename in self.__executecommand__(cmd).split("\n"):
            if len(filename)>0:
                files.append(filename)
        return files
        