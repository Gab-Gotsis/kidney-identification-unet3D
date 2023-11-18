# COMP9444_keen_beans

Project Report
https://docs.google.com/document/d/1YHhVStM9Fy6NThUfGkWJQmnP8DKJ-oFesjtKVkwK-2o/edit?usp=sharing

## TEAM MEMBER
| Name | Uni Email Address (zid) |
| ----------- | ----------- |
| Chin Chai | z3405715@unsw.edu.au |
| Hanyang Xu | z5254111@unsw.edu.au |
| Toran Shahi | z5342008@unsw.edu.au |
| Ji Hye Kim  | z5422963@unsw.edu.au |
| Gabriel Gotsis | z5362640@unsw.edu.au |

# Kits-23 Challenge
The topic that has been selected is https://kits-challenge.org 

# Folder Structure
At Google Colab, the base_dir is set to "/content/drive/MyDrive/Colab Notebooks/" for following file. This can be changed at notebook. Due to computational requirement, works are mainly done in Google Colab.

```
./dataset
./dataset/affine_transformed
./notebook_imgs/affine_img.png
./notebook_imgs/case_00000_case_00002.png
./classes/config_class.py
./classes/dataset_utils/preprocessor.py
./classes/dataset_utils/toTorchDataset.py
./classes/models/resnet.py
./classes/models/resnet_model_generator.py
./classes/models/unet3d.py
./pretrainedModel/resnet_10_23dataset.pth
./pretrainedModel/resnet_50_23dataset.pth
./training_checkpoints/Model_resnet*
./training_checkpoints/Model_UNET*
main_notebook.ipynb
resample_dataset.ipynb
resnet_training_cuda.ipynb
Unet3D_train_vanila_model.ipynb
```

<mark>NN-UNET Folder Structure</mark>
- For NN-UNET, file and contents are located inside folder that is named 'project'.
- The folder has to be moved to '/content/drive/MyDrive/project' to be functioning. 


## Data source
- Raw data folder is to be located at ./dataset
- Raw data can be downloaded at https://kits-challenge.org/kits23/ or URL https://kits23-data.s3.us-east-2.amazonaws.com/repo-tarballs/kits23-v0.1.2.tar
- Put the tar file at dataset folder and extract it.

## Pretrained Weight
- folder /training_checkpoints/ contains our trained RESNET and UNET pretrained weight. 
- folder /pretrainedModel/ contains RESNET pretrained weight from https://github.com/Tencent/MedicalNet

### Transform Dataset
- Transform of dataset can be performed by using resample_dataset.ipynb
- Transformed dataset can be located at ./dataset/affine_tranformed.

## Classes Folder
- Contain helper classes
- Contain model generators

## Model Training
Notebook for Resnet and Unet 3D training are given below
```
resnet_training_cuda.ipynb
Unet3D_train_vanila_model.ipynb

```
# Main Notebook
Notebook below contains the development processes and findings when taking the kits23 chanllenge as the assignment project.
```
main_notebook.ipynb
```

# Setup python virtual env (Use colab instead)
It is advised that you shall setup virtual python environment if you wish to run the main project file.
If you are confident in configuring environment (such as using conda, docker etc), ensure python version is 3.10.xx, and move to 'python packages' section for packages installation.

IF you are using other python version, it is recommended to use your own python environment for your own folder. Datasource may restrain torch version that can be used.

You can ignore the github if you use cloud such as colab. Please note that there is computational cost if cloud is used. Proceed with cloud computing at your own cost. Do provide us your colab view permission.


## python version (Use colab instead)
If you are pyenv user, ensure that you are using python 3.10 version (impact of minor version is not checked):
```
pyenv versions 3.10.xx
```

## create virtual env (Use colab instead)
At the project folder, 
```
python -m venv venv
```
After that, to activate the virtual environment
```
source ./venv/bin/activate
```

## python packages (Use colab instead)
torch, numpy, scikit-learn and jupyterlab are the core packages (for now 25 Oct 2023)
If pip is used in virtual environments, package can be installed with `pip install -r requirements.txt` 
```
numpy==1.26.1
torch==2.1.0
scikit-learn==1.3.2
jupyterlab==4.0.7
```

## start jupyter lab (Use colab instead)
At terminal, go to the root directory of the project and type below
`jupyter lab`
- Unfortunately, due to high computation requirement, model training has to be done in Colab.
- Therefore, main_notebook.ipynb can only run on Colab.

## Bash/Python command tools (for Git management)
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