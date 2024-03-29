from Git.Git import *
from CodeReview.CodeReviewGenerator import * 
from PatchGenerator.PatchFileGenerator import PatchFileGenerator
from BrowserView.WebPage import openweb

def main():
    print("Welcome to EasyCommit")
    cunt=True
    while cunt:
        repo= input("Enter path to your working directory : ")
        my_branch=input("Enter your branch name: ")
        main_branch= input("Enter branch with respect to run the operations: ")
        # validations to add after each input.
        while cunt:
            print("Which operation you want to perform: \n\tEngineering Build press --> 1\n\tCode Review table press --> 2\n")
            action= input()
            if action == '1':
                patchgenerator= PatchFileGenerator(repo, my_branch, main_branch)
                patchgenerator.createzipfile()

            elif action == '2':
                tab = CodeReviewGenerator(repo, my_branch, main_branch)
                tab.printTableOnConsole()
                openweb(tab)

            else:
                print("OOPS not in the menu.")

            cunt=input("Do you want to continue with same configuration(y/n): ").lower()=='y'

        cunt=input("Run again with different configuration(y/n): ").lower() == 'y'
        if not cunt:
            print("Happy coding then :)")


if __name__ == "__main__":
    main()
