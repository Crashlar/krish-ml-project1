from setuptools import find_packages , setup
from typing import List

HYPEN_E_DOT = "-e ."


from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of dependencies.

    Parameters
    ----------
    file_path : str
        The path to the requirements file (e.g., 'requirements.txt').

    Returns
    -------
    List[str]
        A list of requirement strings, with newline characters removed.
    
    Notes
    -----
    - Each line in the file is treated as one requirement.
    - Newline characters at the end of each line are stripped.
    """
    
    requirements = []
    
    # Open the file in read mode
    with open(file_path) as file_obj:
        # Read all lines from the file
        requirements = file_obj.readlines()
        
        # Remove newline characters from each line
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name = "Mukesh K",
    description= "This is a simple practice project where I understand workflow , pipelines that all are required to create a best project to users and developer",
    version="0.0.1",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
    # customize according to project
)
