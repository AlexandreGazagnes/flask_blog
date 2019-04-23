#!/usr/bin/env python3
# coding: utf-8

from setuptools import setup, find_packages

install_requires = [
    'bcrypt==3.1.4',
    'blinker==1.4',
    'certifi==2016.2.28',
    'cffi==1.11.5',
    'click==6.7',
    'Flask==1.0',
    'Flask-Bcrypt==0.7.1',
    'Flask-Login==0.4.1',
    'Flask-Mail==0.9.1',
    'Flask-SQLAlchemy==2.3.2',
    'Flask-WTF==0.14.2',
    'itsdangerous==0.24',
    'Jinja2==2.10',
    'MarkupSafe==1.0',
    'Pillow==5.3.0',
    'pycparser==2.18',
    'six==1.11.0',
    'SQLAlchemy==1.2.7',
    'Werkzeug==0.14.1',
    'WTForms==2.1'
]

setup(
    name='flask_blog',
    version='0.0.1',
    python_requires='>=3.6',
    packages=find_packages(),
    author='AlexandreGazagnes',
    author_email='a_syoez@yahoo.fr',
    description='just another flask web app',
    long_description='See [here](https://github.com/AlexandreGazagnes/flask_blog) for complete user guide.',
    url='https://github.com/AlexandreGazagnes/flask_blog',
    install_requires=install_requires,
    license='GNU - GPL',
)
