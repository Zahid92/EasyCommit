# import module
import webbrowser
from CodeReview.CodeReviewGenerator import CodeReviewGenerator
import os

def openweb(crg:CodeReviewGenerator):
    path=__createhtmlfile__(crg)
    # open html file
    webbrowser.open(path) 


def TableForWeb(crg:CodeReviewGenerator):
        table=crg.gettable()
        COMMITURL=f'https://yourprojectrepositriesaddress/{crg.git.dir.split("/")[-1]}/commits/'
        tablehtml="<table>\n\t<tr>\n\t\t<th>Commit</th>\n\t\t<th>Files Changed</th>\n\t</tr>"
        for commit, details in table.items():
            i=len(details)
            j = i//2
            tablehtml+=f'\n\t<tr>\n\t\t<td><a href="{COMMITURL}{commit}" target="_blank">{commit}</a></td>\n\t\t<td>'
            for filename in details:
                i-=1
                cm = commit if j==i else " " * len(commit)
                tablehtml+=f"{filename}</br>\n\t\t\t"
            tablehtml+="\n\t\t</td>\n\t</tr>"

        tablehtml+="\n</table>"
        return tablehtml


def __createhtmlfile__(crg: CodeReviewGenerator):
    table = TableForWeb(crg)
    style='''
    body{
    font-family: Calibri;
    font-size: 11pt;
    }
    table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    padding:8px;
    }
    table {
    max-width:70%;
    }
    th,tr{
    text-align:left;
    }
    b{
    font-weight:bold;
    padding:4px;
    margin-bottom:10px;
    height:20px;
    }
    r{
    font-style:oblique;
    }
    '''

    html='''
  <!DOCTYPE html>
    <html>
    <head>
    <style>{style}
    </style>
    </head>
    <body>
    Hi <r>recipient</r>,</br>
    </br>As per our discussion,</br>
    I have implemented the changes regarding <r>story/defect</r> <a href="https://yourjiraadress/{id}" target="_blank">{branch}</a></br>
    Could you review the changes.</br></br>
    <b>Repository: {repo}</b></br>
    <b>Branch: {branch}</b></br>
    {table}</br>
    Thanks and regards,
    </body>
    </html>
    '''
    rep=crg.git.dir.split("//")[-1].upper()
    html=html.format(style=style,table=table,id=crg.git.my_branch.split("_")[0],branch=crg.git.my_branch,repo=rep)
    with open("c:/temp/CodeReviewTable.html",'w') as fi:
        fi.write(html)
    
    return "c:/temp/CodeReviewTable.html"

