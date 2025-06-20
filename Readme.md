# Create a repository

# Create an Environment
conda create -p venv python==3.12 -y

# Connect with git

## First time
git config --global user.name "username"
git config --global user.email "email@email.com"

## Add Readme.md file
touch Readme.md

## Commit and push
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/vvithurshan/mlproject.git
git push -u origin main

## Go to the repo and create .gitignore file with your programming language and commit 

## Go to the Project Directory 
git pull

############################# Git Done #######################################

# Create files
touch setup.py # for building our application as a package
touch requirments.txt

# Edit setup.py

from setuptools import find_packages, setup
from typing import List

def get_requirments(file_path:str)->List[str]:
    '''
    this function will return the list of requirments
    '''
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n", "") for req in requirments ]
        if '-e .' in requirments:
            requirments.remove('-e .')
    return requirments

setup(
    name='mlprojct',
    versions='0.0.1',
    author='Vithurshan',
    author_email='vvithurshan@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas', 'numpy', 'seaborn', 'matplot']
    install_requires=get_requirments('requirments.txt')
)


# Edit requirments.txt

pandas
seaborn
numpy
matplotlib
scikit-learn
-e . # if you execute pip install -r requirments.txt


# Create src folder
mkdir src
touch src/__init__.py # to consider src as a package

# Install packages
pip install -r requirments.txt

## a folder called mlproject.egg-info will be created 

############################# Setup Done #######################################

# Create Some Folders and files
mkdir ./src/components
touch ./src/components/__init__.py
touch ./src/components/data_ingestion.py # about data reading
touch ./src/components/data_transformation.py # transformation: like one-hot encoding, train test split
touch ./src/components/model_trainer.py # for the training purpose 

mkdir ./src/pipeline
touch ./src/pipeline/train_pipeline.py # it will triger all the files in the components
touch ./src/pipeline/predict_pipeline.py
touch ./src/pipeline/__init__.py

touch ./src/logger.py
touch ./src/exception.py
touch ./src/utils.py

# Edit exception
import sys

def error_message_detail(error, error_detail:sys):
    _, _, exe_tb = error_detail.exc_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    error_message = "Error Occured in Python Script name \
        [{0}] line number [{1}] error message [{2}]".format(
            file_name,
            exe_tb.tb_lineno,
            str(error)
        )
    return error_message
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

############################# Logging Done #######################################


# Edit Logger
import logging
import os
from datetime import datetime

LOG_FILE = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'
logs_path = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_path, exist_ok=True)  # Only create the directory

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    logging.info('Logging has started')

############################# Exception Done #######################################
# Create Notebook Folder
mkdir notebook
touch notebook/EDA.ipynb
touch notebook/Model_trainer.ipynb

# Do the EDA and Model Traininer 


# Data Ingestion