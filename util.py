import sys
import os
import shutil

def mkdir(path):
    if os.path.isdir(path):
        raise Exception("Invalid Path!")
    os.makedirs(path)

def mkfile(path, file):
    path = os.path.join(path, file)
    if os.path.isfile(path):
        raise Exception("Invalid Path!")
    file = open(path, 'w')
    file.close()

def cpfile(src, dst):
    if not os.path.isfile(src):
        raise Exception("No File <%s>" % (src))
    if os.path.isfile(dst):
        raise Exception("File <%s> existed" % (dst))
    shutil.copy(src, dst)
        