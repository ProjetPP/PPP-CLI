#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='ppp_cli',
    version='0.1',
    description='Command-line tool for debugging PPP modules',
    url='https://github.com/ProjetPP/PPP-CLI',
    author='Valentin Lorentz',
    author_email='valentin.lorentz+ppp@ens-lyon.org',
    license='MIT',
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Development Status :: 1 - Planning',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    install_requires=[
        'ppp_datamodel>=0.6.1,<0.7',
        'ppp_datamodel_notation_parser',
    ],
    packages=[
        'ppp_cli',
    ],
)


