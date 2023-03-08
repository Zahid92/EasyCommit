from Git import *

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
    def __init__(self, repo, branch, comparetobranch ="main-5.5") -> None:
        self.git = Git(branch, repo, comparetobranch) 
        self.git.fillcommits()
        self.git.fillchangedfilesforcommits()
    

    def createTable(self) -> None:
        commits= self.git.getcommits()

        if len(commits)==0:
            print("No commits found.")
            return
        print("_"*100)
        print(f"\n| CommitId{' '*(len(commits[0][0])-8)} | FilesChanged           ")

        for commit in commits:
            if commit[1] != True:
                continue
            details = self.git.getchangedfilesforcommit(commit[0])
            print("_"*100)
            details=details.split("\n")
            details=details[0:len(details)-1]
            i=len(details)
            j = i//2
            for filename in details:
                i-=1
                cm = commit[0] if j==i else " " * len(commit[0])
                print(f"\n| {cm} | {filename}")
        print("_"*100)
            

