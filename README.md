# EasyCommit
Project to easify CodeReview and engineering testing for internal use

## Project is used to auto-generate mail format to be send for internal code reviews
## And to generate a zip folder containing neccesary binaries to manually test the changes on BUilds of different branch (usually mainbranch)

Its a first version is a Console App for windows and it is pretty easy to use.

setup:
1. You need to have python installed on your machine.
2. Clone the repository.
3. Goto config.py and update your repository links.

run:
1. open cmd(Administrator Mode preferred) in EasyCommit repository.
2. run command "python run.py"

use:
1. You can enter your branch name and target branch name.
2. On the basis of entered Information you can create a html page.
3. Html page consists of issue info and a table with commits and files changed on those commits.

