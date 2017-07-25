# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ScanLogAnalysis',
    version='0.0.1',
    description='A tool for analyzing the log produced by wallet',
    long_description=readme,
    author='leilei.yll',
    author_email='leilei.yll@alibaba-inc.com',
    url='https://github.com/kennethreitz/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

