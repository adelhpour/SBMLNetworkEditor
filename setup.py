from setuptools import setup
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
with open("VERSION.txt", "r") as f:
    version = f.read().rstrip()
    
with open("requirements.txt", "r") as f:
    requirements = f.readlines()
setup(
    name="sbmlnetworkeditor",
    version=version,
    author="Adel Heydarabadipour",
    author_email="adelhp@uw.edu",
    description="A python api to work with libsbmlnetworkeditor library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adelhpour/SBMLNetworkEditor",
    project_urls={
        "Bug Tracker": "https://github.com/adelhpour/SBMLNetworkEditor/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9"
)
