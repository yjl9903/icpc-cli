BASE_PATH = ''
CF_PATH = 'CodeForces'

CF_USER = {
    'handle': '', 'password': ''
}

OJ_PATH = {
    'hdu': 'HDu', 'h': 'HDu', 
    'poj': 'PKu', 'pku': 'PKu', 'p': 'PKu',
    'zoj': 'ZOJ', 'z': 'ZOJ',
    'loj': 'LibreOJ'
}

CF_NUMBER = 5 
# cf contest problem number
STANDARD_NUMBER = 11
# icpc contest problem number

FOLDERS = [
    {
        'name': 'debug',
    },
    {
        'name': 'input',
        'empty_files': ['in.txt', 'out.txt']
    },
    {
        'name': 'attempt'
    },
    {
        'name': 'standard'
    },
    {
        'name': '.vscode',
        'src_files': [
            '.\\.vscode\\c_cpp_properties.json',
            '.\\.vscode\\launch.json',
            '.\\.vscode\\tasks.json',
            '.\\.vscode\\settings.json',
        ]
    }
]

FILES = [
    {
        'name': 'init.cpp',
        'src': '.\\init.cpp'
    }
]

DATA_PATH = '..\\input\\'
DEFAULT_INPUT = 'in.txt'
DEFAULT_OUTPUT = 'out.txt'
DEFAULT_OUTPUT_SIZE = 20
DEFAULT_GEN = 'init.exe'