from setuptools import find_packages, setup
import os
import subprocess

def requirements(infile):
    with open(infile) as f:
        packages = f.read().splitlines()
        return [pkg for pkg in packages if not pkg.startswith("#") and len(pkg.strip()) > 0]

setup(
    name='bertviz',
    version='1.0dev1+pnnl',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'bertviz': ['*.js']
    },
    zip_safe=False,
    install_requires=requirements("requirements.txt")
)
