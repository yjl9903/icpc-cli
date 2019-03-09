import sys
import os
import shutil

def mkdir(*args, **kwargs):
    path = os.path.join(*args)
    if os.path.isdir(path):
        raise Exception("Invalid Path!")
    os.makedirs(path)
    if 'no-print' not in kwargs:
        print('making directory => %s' % (path))

def mkfile(*args, **kwargs):
    if 'file' not in kwargs:
        raise Exception('Lose destination file name')
    path = os.path.join(*args, kwargs['file'])
    if os.path.isfile(path):
        raise Exception("Invalid Path!")
    file = open(path, 'w')
    file.close()
    if 'no-print' not in kwargs:
        print('making file => %s' % (path))

def cpfile(*args, **kwargs):
    dst = os.path.join(*args)
    if 'src' not in kwargs:
        raise Exception('Lose source file name')
    src = kwargs['src']
    if not os.path.isfile(src):
        raise Exception("No File <%s>" % (src))
    if os.path.isfile(dst):
        raise Exception("File <%s> existed" % (dst))
    shutil.copy(src, dst)
    if 'no-print' not in kwargs:
        print('copying file from %s => %s' % (src, dst))
        