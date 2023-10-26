# COMP9444_keen_beans

Project Report
https://docs.google.com/document/d/1YHhVStM9Fy6NThUfGkWJQmnP8DKJ-oFesjtKVkwK-2o/edit?usp=sharing

## TEAM MEMBER
| Name | Uni Email Address (zid) |
| ----------- | ----------- |
| Chin Chai | z3405715@unsw.edu.au |
| Hanyang Xu | z5254111@unsw.edu.au |
| name | uni email |
| name | uni email |
| name | uni email |

# TOPIC HERE

# Git Folder Structure

# Setup python virtual env
It is advised that you shall setup virtual python environment if you wish to run the main project file.
If you are confident in configuring environment (such as using conda, docker etc), ensure python version is 3.9.xx, and move to 'python packages' section for packages installation.

IF you are using other python version, it is recommended to use your own python environment for your own folder. Datasource may restrain torch version that can be used.

You can ignore the github if you use cloud such as colab. Please note that there is computational cost if cloud is used. Proceed with cloud computing at your own cost. Do provide us your colab view permission.


## python version
If you are pyenv user, ensure that you are using python 3.9 version (impact of minor version is not checked):
```
pyenv versions 3.9.xx
```

## create virtual env
At the project folder, 
```
python -m venv venv
```
After that, to activate the virtual environment
```
source ./venv/bin/activate
```


## python packages
torch, numpy, scikit-learn and jupyterlab are the core packages (for now 25 Oct 2023)
If pip is used in virtual environments, package can be installed with `pip install -r requirements.txt` 
```
numpy==1.26.1
torch==2.1.0
scikit-learn==1.3.2
jupyterlab==4.0.7
```

## start jupyter lab
At terminal, go to the root directory of the project and type below
`jupyter lab`

## Bash/Python command tools
make sure you have permission to run bash file at root
```
init_folder.sh
```
and permission to run bash file at bash folder
```
create_gitignore.sh
create_skeleton_folders.sh
```

Please be edit above bash if necessary.

## Data source
### Data folder (Test and Training)
### Output Folder

## User folder

## Git Ignore


### Unit Test
### Other Tools

