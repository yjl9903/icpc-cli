import sys
import os
import shutil
import time
import requests
from threading import Thread

ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

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
    if not os.path.isabs(src):
        src = os.path.join(ASSETS_PATH, os.path.normpath(src))

    if not os.path.isfile(src):
        raise Exception("No File <%s>" % (src))
    if os.path.isfile(dst):
        raise Exception("File <%s> existed" % (dst))
        
    shutil.copy(src, dst)

    if 'no-print' not in kwargs:
        print('copying file => %s' % os.path.join(dst, os.path.split(src)[1]))

def setTimeLimit(maxTime):
    def wrapper(func):
        def _wrapper(*args, **kw):
            class LimitTime(Thread):
                def __init__(self):
                    Thread.__init__(self)
                def run(self):
                    func(*args, **kw)
                def stop(self):
                    if self.is_alive():
                        Thread._Thread__stop(self)
            t = LimitTime()
            start = time.time()
            t.start()
            t.join(timeout=maxTime)
            end = time.time()
            last = 1000 * (end - start)
            if t.is_alive():
                t.stop()
            return last
        return _wrapper
    return wrapper

def execTest(problem, input, time):
    if not time:
        if input:
            return os.popen('%s <%s' % (problem, input)).read().strip(), 0
        else:
            return os.popen('%s' % problem).read().strip(), 0
        
    output = ['']

    @setTimeLimit(20 * 1000)
    def fun():
        if input:
            output[0] = os.popen('%s <%s' % (problem, input)).read().strip()
        else:
            output[0] = os.popen('%s' % problem).read().strip()
        
    used = fun()
    return output[0], used

def getLatestVerdict(user):
    r = requests.get('http://codeforces.com/api/user.status?' + 'handle=%s&from=1&count=1' % user)
    js = r.json()
    if 'status' not in js or js['status'] != 'OK':
        raise ConnectionError('Cannot connect to codeforces!')
    try:
        result = js['result'][0]
        id_ = result['id']
        verdict_ = '' if 'verdict' not in result else result['verdict'] 
        time_ = result['timeConsumedMillis']
        memory_ = result['memoryConsumedBytes'] / 1000
        passedTestCount_ = result['passedTestCount']
    except Exception as e:
        raise ConnectionError('Cannot get latest submission!')
    return id_, verdict_, time_, memory_, passedTestCount_