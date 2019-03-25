# icpc-cli

[![Build Status](https://travis-ci.org/yjl9903/icpc-cli.svg?branch=master)](https://travis-ci.org/yjl9903/icpc-cli)

Enjoy a Codeforces round!

![](https://github.com/yjl9903/icpc-cli/raw/master/1.gif)

![](https://github.com/yjl9903/icpc-cli/raw/master/2.gif)

## Installation

Make sure that you have added `code` (VS Code) command in your environment variable.

Clone the repositories

```
git clone git@github.com:yjl9903/icpc-cli.git
```

Go to icpc folder and modify `config.py`.

```
BASE_PATH = 'C:\\'
CF_PATH = 'CodeForces'

CF_USER = {
    'handle': 'abcd', 'password': 'abcd'
}
```

Input your path, and `icpc init` `icpc open` will use this base path.

Make sure that `Codeforces` folder in your base path. All the commands related to `Codeforces` will use this folder.

If you want to use `icpc submit`, input your account information in `CF_USER`.

## Usage

### Init a contest folder

Use `icpc init [Folder]` or just `init [Folder]` command to create a contest folder in your base path.

### Open a contest

Use `icpc open [Folder]` or `open [Folder]` command.

### Submit your code

Go to your contest folder.

Use `icpc submit` command to start submit mode.

Then icpc-cli will use your account to login Codeforces.

Input the contest id, and you can get it in the contest url `codeforces.com/contest/[id]`.

Now, you can just input `a`, `b`, `c`, ... to submit your code!

P.S: Make sure that your code name is `a.cpp`, `b.cpp`, `c.cpp` and so on.

## Credits

+ [idne](https://github.com/endiliey/idne)

+ [Einsturing](https://github.com/Einsturing)