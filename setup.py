from setuptools import setup
from setuptools import find_packages

MAJOR = 0
MINOR = 0
MICRO = 9

version = f'{MAJOR}.{MINOR}.{MICRO}'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

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
    install_requires=["libsbmlnetworkeditor", "networkinfotranslator"],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8"
)
