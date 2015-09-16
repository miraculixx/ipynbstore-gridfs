'''
Created on Sep 16, 2015

@author: Gaurav Ghimire <gaurav.ghimire@gmail.com>
'''
import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='ipynbstore_gridfs',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='commercial',  # example license
    description='An IPython Notebook Server with GridFS backend',
    long_description=README,
    url='https://github.com/gaumire/ipynbstore-gridfs',
    author='Gaurav Ghimire',
    author_email='gaurav.ghimire@gmail.com',
    maintainer='Patrick Senti',
    classifiers=[
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'License :: Commercial',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # replace these appropriately if you are using Python 3
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'pymongo==3.0.2',
        'ipython>=3'
    ],
    dependency_links=[
    ]
)
