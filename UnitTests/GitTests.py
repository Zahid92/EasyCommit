import unittest
from CodeReviewGenerator import *
''' tests related to Git Class'''

def testreviewgenerator():
    c = CodeReviewGenerator("D://olrep", "OLRS-1938", "OLRS-1935")
    c.createTable()

    
def testgit():
    g= Git( "OLRS-1938","D://olrep", "OLRS-1935")
    g.fillcommits()
    g.getcommits()
    g.fillchangedfilesforcommits()
    print(g.filesChanged)
    print(g.getfileschangedforbranch())