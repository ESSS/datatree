from os import path
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand



#===================================================================================================
# PyTest
#===================================================================================================
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        import sys
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)



with open(path.join(path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()

setup(
    name='datatree',
    version='0.1.8.1',

    packages=find_packages(),
    install_requires=[
        'six'
    ],
    tests_require=[
        'pytest',
        'PyYAML',
        'sphinx',
        'coverage',
        'tox',
    ],
    cmdclass = {
        'test': PyTest
    },

    include_package_data=True,

    # Project description
    author='Jason Webb',
    author_email='bigjasonwebb@gmail.com',
    url='https://github.com/bigjason/datatree',
    license='Creative Commons Attribution 3.0 Unported License',
    description='DSL for creating structured documents in python.',
    long_description=readme,
    classifiers=[
       'Development Status :: 4 - Beta',
       'Topic :: Text Processing :: Markup',
       'Topic :: Text Processing :: Markup :: XML',
       'Operating System :: OS Independent',
       'Intended Audience :: Developers',
       'Programming Language :: Python :: 2.6',
       'Programming Language :: Python :: 2.7',
       'License :: OSI Approved :: Apache Software License'
    ]
)
