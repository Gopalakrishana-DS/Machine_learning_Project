from setuptools import find_packages,setup
from typing import List

hypone_dot_e = "-e ."

def get_requirements(filepath:str)->List[str]:
    """
    this function will return the list of requiremnets
    """
    requirements=[]
    with open(filepath) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if hypone_dot_e in requirements:
            requirements.remove(hypone_dot_e)
    return requirements

setup(
    name="Machine_learning_Project",
    version="0.0.1",
    author="Gopalakrishnan-DS",
    author_email="gopalmuruganandam1999@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)