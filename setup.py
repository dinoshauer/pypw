#!/usr/bin/env python

from setuptools import setup

setup(name='pypw', 
	description='Generates a random password.',
	version='0.1.5', 
	author='Kasper Jacobsen',
	author_email='k@three65.org',
	url='https://github.com/Dinoshauer/PyPW',
	packages=['pypw'],
	entry_points={
		'console_scripts': [
			'pypw = pypw.pypw:main']
	},
	install_requires=[]
)