from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    requirements = []

    try:
        with open("requirements.txt", "r") as file:
            for line in file.readlines():
                requirement = line.strip()

                if requirement and requirement != "-e .":
                    requirements.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements


print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Krish Das",
    author_email="krishanudas508@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()


)
