import os
from setuptools import setup

current_dir = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(current_dir, 'README.md')).read()
REQUIRES_PYTHON = ">=3.5.0"
LICENSE = open(os.path.join(current_dir, 'LICENSE')).read()

reqs = [line.strip() for line in open('requirements.txt')]
dev_reqs = [line.strip() for line in open('requirements_dev.txt')]

setup(
    name="abcunit-backend",
    version="1.0.0",
    description="Backend solution for abcunit success / failure logs",
    long_description=README,
    author="Jonathan Haigh",
    author_email="jonathan.haigh@stfc.ac.uk",
    url="https://github.com/cedadev/abcunit-backend",
    python_requires=REQUIRES_PYTHON,
    license=LICENSE,
    packages=["backend"],
    install_requires=reqs,
    extras_require={"dev": dev_reqs}
)
