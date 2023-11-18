#! /bin/bash

# check if there is exisitng gitignore in root project folder
if test -f ./.gitignore; then
    rm .gitignore
fi

touch .gitignore


# folders or files to be ignored by git
gitignore_text=$(echo ".gitignore"; 
echo "*tmp/*"; 
echo "*results/*"; 
echo "*dataset/*"; 
echo "**/__pycache__/";
echo "**/.ipynb_checkpoints/";
echo "pretrainedModel/*";
echo "chin/dataset/*"; 
echo "chin/tmp/*";
echo "chin/notebook_imgs/*";
echo "project/*";
echo "training_checkpoints/*";
echo "toran/dataset/*"; 
echo "hanyang/dataset/*"; 
echo "gabriel/dataset/*"; 
echo "hayden/dataset/*";
echo "*venv/*"; 
echo "chin/.ipynb_checkpoints/*";
echo "chin/training_checkpoints/*";
echo "toran/.ipynb_checkpoints/*"; 
echo "hanyang/.ipynb_checkpoints/*"; 
echo "gabriel/.ipynb_checkpoints/*";
echo "hayden/.ipynb_checkpoints/*";
echo "bash/.ipynb_checkpoints/*";
echo ".project";
echo ".metadata/*";
echo "classes/dataset_utils/__pycache__/*";
echo "*.ipynb_checkpoints/*";)
echo "$gitignore_text" >> .gitignore
