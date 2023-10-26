#! /bin/bash

# check if there is exisitng gitignore in root project folder
if test -f ./.gitignore; then
    rm .gitignore
fi

touch .gitignore


# create folders or files to be ignored
gitignore_text=$(echo ".gitignore"; 
echo "*tmp/*"; 
echo "*results/*"; 
echo "*dataset/*"; 
echo "*venv/*"; 
echo "*.ipynb_checkpoints/*";)
echo "$gitignore_text" >> .gitignore