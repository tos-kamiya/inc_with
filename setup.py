#!/usr/bin/env python3

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [L for L in f.read().splitlines() if not L.startswith('#')]

version = '0.1'

setup(
    name='inc_with',
    version=version,
    install_requires=requirements,
    author='Toshihiro Kamiya',
    author_email='kamiya@mgj.nifty.com',
    scripts=['inc_with'],
    url='https://github.com/tos-kamiya/inc_with/',
    license='CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    description='Run command with giving parameters incrementally',
)

