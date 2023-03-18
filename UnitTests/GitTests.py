import unittest
from CodeReviewGenerator import *
from WebPage import openweb

''' tests related to Git Class'''

def testreviewgenerator():
    c = CodeReviewGenerator("D://olrep", "OLRS-3905", "main-5.5")
    c.createTable()
    openweb(c)

    
def testgit():
    g= Git( "OLRS-1938","D://olrep", "OLRS-1935")
    g.fillcommits()
    g.getcommits()
    g.fillchangedfilesforcommits()
    print(g.filesChanged)
    print(g.getfileschangedforbranch())
