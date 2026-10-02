from setuptools import setup, find_packages
from typing import List
def get_requirements()->List[str]:
    """
    This function will return the list of requirements
    """
    requirement_lst:List[str] = []

    try: 
        with open('requirements.txt','r') as file:
            #read lines from the file 
            lines= file.readlines()
            #process each lines 
            for line in lines: 
                requirement = line.strip()
                #ignore empty lines and -e . 
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")


    return requirement_lst

print(get_requirements())

setup(
    name='networksecurity',
    version='0.0.1',
    author="Deep Shah",     
    author_email="deep.shah.study100@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()  # this make sure that all the libraries mentioned in requirements.txt are installed when this package is installed
)

