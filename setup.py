#!/usr/bin/env python3

from setuptools import setup

setup(
    name='subordinate',
    version='0.1',
    description='Tools to manage subuid and subgid',
    long_description=open('README.rst').read(),
    author='Xavier Gendre',
    author_email='gendre.reivax@gmail.com',
    url='https://github.com/Meseira/subordinate',
    license='GPLv3',
    keywords=[
        'id',
        'linux',
        'subordinate',
        'subuid',
        'subgid',
        'system'
    ],
    install_requires=[],
    extras_require={},
    packages=['subordinate'],
    include_package_data=True,
    data_files=[],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: System',
        'Topic :: System :: Shells',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: System Shells',
        'Topic :: Utilities'
    ],
    zip_safe=False
)
