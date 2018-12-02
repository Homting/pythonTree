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

def isHidden(f):
    if f.split("\\")[-1].startswith("."):
        return True
    return False


def dfs_showdir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")

    if depth >= _level:
        return

    for item in os.listdir(path):
        if item.startswith(".") and _hidden:
            continue
        print("|      " * depth + "+--" + item)

        newitem = path +'/'+ item
        if os.path.isdir(newitem):
            dfs_showdir(newitem, depth +1)

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
            _level = int(value)
    #listTree(_rootDir, _level, _hidden)
    dfs_showdir(_rootDir,0)