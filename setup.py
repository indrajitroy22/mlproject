## This will be responsible for building the entire ML application as a package 
## -e . i s added to requirements.txt 
# what this means is whenever we run requirements.txt automatically the setup.py should also run
##In order to remove reading this - e. some logic also needs to implemented which is implemeted in the get_requirements


from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirement]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements


setup(
    name="ML Project",
    version="0.0.1",
    author="INDRAJIT ROY",
    author_email="indrajit.roy7.official@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)