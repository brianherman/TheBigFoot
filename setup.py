#!/usr/bin/env python
# Shamelessly stolen from requests.
# Learn more: https://github.com/kennethreitz/setup.py
import os
import re
import sys

from codecs import open

from setuptools import setup
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        try:
            from multiprocessing import cpu_count
            self.pytest_args = ['-n', str(cpu_count()), '--boxed']
        except (ImportError, NotImplementedError):
            self.pytest_args = ['-n', '1', '--boxed']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    #os.system('twine upload dist/*')
    sys.exit()

packages = ['TheBigFoot']

requires = []

test_requirements = []

about = {}

exec(open(os.path.join(here, 'TheBigFoot', '__version__.py'), 'r', 'utf-8').read(), about)

readme = open('README.md', 'r', 'utf-8').read()
history = open('HISTORY.md', 'r', 'utf-8').read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], 'TheBigFoot': ['*.pem']},
    package_dir={'TheBigFoot': 'TheBigFoot'},
    include_package_data=True,
    python_requires="!=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=requires,
    license=about['__license__'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    cmdclass={'test': PyTest},
    tests_require=test_requirements,
    extras_require={},
    project_urls={
        'Documentation': 'https://thebigfoot.github.io',
        'Source': 'https://github.com/brianherman/thebigfoot',
    },
)
