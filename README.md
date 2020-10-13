git-cloner
============================================================

Table of Contents
=================

- [About](#About)
- [Installing](#installing)
- [Usage](#Usage)

About
=====

git-cloner is a command line tool to batch clone git projects from GitLab server.

Installing
==========

- **Windows**

1. Install [Python 2.7 or 3.4+](https://www.python.org/):

    When installing, option **`Add python.exe to Path`** must be selected and enabled. Or after installation, manually add the Python installation directory and its Scripts subdirectory to your PATH. Depending on your Python version, the defaults would be C:\Python27 and C:\Python27\Scripts respectively.

1. Install `git-cloner` via pip

    ```
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ git-cloner
    ```

1. Reboot the system

- **Linux**

1. Install [Python 2.7 or 3.4+](https://www.python.org/)

1. Install `git-cloner` via pip

    ```
    pip install -i https://mirrors.aliyun.com/pypi/simple/ git-cloner
    ```

- **MacOSX**

1. Install [Python 2.7 or 3.4+](https://www.python.org/)

1. Install `git-cloner` via pip

    ```
    pip install -i https://pypi.douban.com/simple/ git-cloner
    ```

Usage
=====

- **General command help**

    ```
    git-cloner --help
    usage: git-cloner [-h] -s <url> -u <user> -p <pass> [-g <group> [<group> ...]] [-o <path>]
    
    optional arguments:
      -h, --help            show this help message and exit
      -s <url>, --server <url>
                            The GitLab server url
      -u <user>, --user <user>
                            The GitLab login username
      -p <pass>, --pass <pass>
                            The GitLab login password
      -g <group> [<group> ...], --group <group> [<group> ...]
                            Only clone the projects in this group(s)
      -o <path>, --output <path>
                            Clone projects to output directory
    ```
