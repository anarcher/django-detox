import os
from setuptools import setup,find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-detox",
    version = "0.1",
    url = 'http://github.com/anarcher/django-detox',
    license = 'BSD',
    description = "A mini framework/libs for Django apps.",
    long_description = read('README'),
 
    author = 'anarcher',
    author_email = 'anarcher@gmail.com',
 
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    
    install_requires = ['setuptools'],
    classifiers = []
)

