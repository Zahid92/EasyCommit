from Git.Git import *

class CodeReviewGenerator:
    '''
    This class is used to generate a table like structure,
      which is used by persi to ask for reviewing Code changes.

      *Table structure*
      _______________________________________________________
      |      CommitId          |     Files Changed          |
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |    R@nd0mC0mm1T        |    Relatedchangedfile.cs   |
      |________________________|____________________________|

    '''
    WIDTH=120

    def __init__(self, repo, branch, comparetobranch ="main-5.5") -> None:
        self.git = Git(branch, repo, comparetobranch) 
    

    def printTableOnConsole(self) -> None:
        commits= self.git.getcommits()

        if len(commits)==0:
            print("No commits found.")
            return

        for commit in commits:
            if commit[1] != True:
                continue
            details = self.git.getchangedfilesforcommit(commit[0])
            print(f"Commit: {commit[0]}")
            print(f"Changed files:\n{details}")

    def __tabledetails__(self):
        table=dict()
        for commit in self.git.getcommits():
            if not commit[1]:
                continue
            details = self.git.getchangedfilesforcommit(commit[0])
            details=details.split("\n")
            details=tuple(details[0:len(details)-1])
            table[commit[0]]=details
        return table
    
    def gettable(self):
        return self.__tabledetails__()



            

