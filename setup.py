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
    install_requires=get_requirments('requirements.txt')
)