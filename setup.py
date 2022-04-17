# setup.py

import os
from setuptools import setup, find_packages

def read_file(fname):
    "Read a local file"
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='mkdocs-img2figv2-plugin',
    version='0.0.2',
    description='A MkDocs plugin that converts markdown encoded images into <figure> elements.',
	long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    keywords='mkdocs python markdown',
    url='https://github.com/jackiexiao/mkdocs-img2figv2-plugin',
    author='Antonio Cambule & jackiexiao',
	license='MIT',
	python_requires='>=3.6',
    install_requires=[
		'mkdocs'
	],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'img2figv2 = src:Image2FigurePlugin',
        ]
    }
)