from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT='-e .'

def get_requirements(filepath:str)->List[str]:
    '''this function will return the list of requirements
    by reading the file'''
    requirements =[]
    with open(filepath) as file:
        requirements = file.read().splitlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Urav',
    author_email='uravfarooqui3@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)

