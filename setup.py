__author__ = 'thomas'
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'Readme.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='wolkenatlas',

	# Versions should comply with PEP440.  For a discussion on single-sourcing
	# the version across setup.py and the project code, see
	# https://packaging.python.org/en/latest/single_source_version.html
	version='0.1.5',

	description='NLP embedding wrapper',
	long_description=long_description,

	# The project's main homepage.
	url='https://github.com/tttthomasssss/wolkenatlas',

	# Author details
	author='Thomas Kober',
	author_email='tttthomasssss@gmail.com',

	# Choose your license
	license='MIT',

	# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers=[
		# How mature is this project? Common values are
		#   3 - Alpha
		#   4 - Beta
		#   5 - Production/Stable
		'Development Status :: 3 - Alpha',

		# Indicate who your project is intended for
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering :: Artificial Intelligence',

		# Pick your license as you wish (should match "license" above)
		'License :: OSI Approved :: MIT License',

		# Specify the Python versions you support here. In particular, ensure
		# that you indicate whether you support Python 2, Python 3 or both.
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
	],

	# What does your project relate to?
	keywords='nlp research distributional-semantics word-embedding word-representation word-vector representation-learning',

	# You can just specify the packages manually here if your project is
	# simple. Or you can use find_packages().
	packages=find_packages(exclude=['contrib', 'docs', 'tests']),

	# Alternatively, if you want to distribute just a my_module.py, uncomment
	# this:
	#   py_modules=["my_module"],

	# List run-time dependencies here.  These will be installed by pip when
	# your project is installed. For an analysis of "install_requires" vs pip's
	# requirements files see:
	# https://packaging.python.org/en/latest/requirements.html
	install_requires=[
		'numpy>=1.18.2',
	],

	# List additional groups of dependencies here (e.g. development
	# dependencies). You can install these using the following syntax,
	# for example:
	# $ pip install -e .[dev,test]
	extras_require={
		'dev': ['check-manifest'],
		'test': ['coverage'],
	},

	# To provide executable scripts, use entry points in preference to the
	# "scripts" keyword. Entry points provide cross-platform support and allow
	# pip to create the appropriate form of executable for the target platform.
	entry_points={
		'console_scripts': [
			'sample=sample:main',
		],
	},
)