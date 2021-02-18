# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in visitors_management_system/__init__.py
from visitors_management_system import __version__ as version

setup(
	name='visitors_management_system',
	version=version,
	description='visitors management system',
	author='ridwan',
	author_email='ridwan.manqala@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
