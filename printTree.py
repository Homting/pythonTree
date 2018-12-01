#!/usr/bin/python3
# File Name: main.py
# Author: Jin LI
# mail: jin.li@vub.be; homtingli@gmail.com
# Created Time: 2018-12-01 12:46:15
import os
import os.path
import sys, getopt

_rootDir = os.getcwd()
_level = 3
# show hidden, default value is False.
_hidden = True

def listTree(rootDir=_rootDir, level=_level, hidden=_hidden):
    for dirName, subdirList, fileList in os.walk(rootDir):
        if dirName.startswith(".") and _hidden:
            #print(dirName)
            continue
        print("Folder: %s" % dirName)
        for fname in fileList:
            if fname.startswith(".") and _hidden:
                continue
            print("\t%s" % fname)

def usage():
    print ("-------------------------------------------")
    print ("-h\t or --help: show help")
    print ("-a\t or --all:  show all hidden folders and files")
    print ("-l xx\t or --level=xx:  show n level ")
    print ("-------------------------------------------")

if __name__ == "__main__":
    # try:
    #     options, args = getopt.getopt(sys.argv[1:],"hal:",["help","all","level="])
    # except getopt.GetoptError:
    #     sys.exit()

    options, args = getopt.getopt(sys.argv[1:],"hal:",["help","all","level="])

    for parameter, value in options:
        if parameter in ("-h","--help"):
            usage()
            sys.exit()
        if parameter in ("-a","--all"):
            print("show all files including hidden files and folders")
            _hidden = False
        if parameter in ("-l","--level"):
            _level = value
    listTree(_rootDir, _level, _hidden)
