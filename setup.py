#!/usr/bin/python3

from distutils.core import setup

from setuptools import find_packages

version = "0.1.0"

with open('README.rst', mode='r', encoding='utf-8') as f:
    long_description = f.read()

setup(name='ofxstatement-swedbank-xls',
      version=version,
      author="Karl Linderhed",
      author_email="code@karlinde.se",
      url="https://github.com/Karlinde/ofxstatement-swedbank",
      description="Swedbank xls plugin for ofxstatement",
      long_description=long_description,
      license="GPLv3",
      keywords=["ofx", "banking", "statement"],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3',
          'Natural Language :: English',
          'Topic :: Office/Business :: Financial :: Accounting',
          'Topic :: Utilities',
          'Environment :: Console',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=["ofxstatement", "ofxstatement.plugins"],
      entry_points={
          'ofxstatement': ['swedbankxls = ofxstatement.plugins.swedbankxls:SwedbankXlsPlugin']
      },
      install_requires=['ofxstatement', 'xlrd'],
      include_package_data=True,
      zip_safe=True
      )
