#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='pypw', 
	description='Generates a random password.',
	version='0.1.6', 
	author='Kasper Jacobsen',
	author_email='k@three65.org',
	url='https://github.com/Dinoshauer/PyPW',
	packages=find_packages(),
	entry_points={
		'console_scripts': [
			'pypw = pypw.pypw:main']
	},
	license='MIT',
	install_requires=[]
)