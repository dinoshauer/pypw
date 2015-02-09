#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
	name='pypw', 
	description='Generates a random password.',
	version='1.0.0', 
	author='Kasper Jacobsen',
	author_email='k@mackwerk.dk',
	url='https://github.com/Dinoshauer/PyPW',
	packages=find_packages(),
	entry_points={
		'console_scripts': [
			'pypw = pypw.pypw:main',
		]
	},
	license='MIT',
	long_description=open('README.rst').read(),
)
