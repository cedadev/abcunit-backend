#from distutils.core import setup
from setuptools import setup

setup(
    name="abcunit-backend",
    version="1.0.0",
    author="Jonathan Haigh",
    author_email="jonathan.haigh@stfc.ac.uk",
    url="https://github.com/cedadev/abcunit-backend",
    packages=["backend"],
    install_requires=["psycopg2>=2.8.0"]
)

