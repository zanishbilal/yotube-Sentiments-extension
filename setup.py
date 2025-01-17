from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirments(filepath: str) -> List[str]:
    '''
    This function returns a list of requirements from the specified file.
    '''
    requirements = []

    with open(filepath) as file_obj:  # Correctly using the parameter 'filepath'
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Remove newline characters
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)  # Remove "-e ." if present

    return requirements

setup(
    name="sentiment_ml_project",
    version='0.0.1',
    author='Zanish',
    author_email='zanishbilal72@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')  # Ensure 'requirements.txt' exists in the directory
)
