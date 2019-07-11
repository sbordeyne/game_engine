import sys
import os

def get_root():
    cwd = os.getcwd()
    path = os.path.split(cwd)[0]
    return os.path.split(path)[0]


sys.path.append(get_root())
