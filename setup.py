from setuptools import find_packages, setup
from typing import List
import os

def get_requirements(file_path: str) -> List[str]:
    with open(file_path, encoding="utf-8") as file_obj:
        requirements = []
        for line in file_obj:
            line = line.strip()
            if line and not line.startswith("-e"):
                requirements.append(line)
    return requirements


here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="mlproject",
    version="0.0.1",
    author="Abhishek",
    author_email="abhishekjhaa340@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements(os.path.join(here, "requirements.txt")),
)
