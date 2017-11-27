#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT (see LICENSE file provided)
# vim600: fdm=marker tabstop=4 shiftwidth=4 expandtab ai

"""
polib setup script.
"""

__author__ = 'David Jean Louis <izimobil@gmail.com>'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import codecs
import polib

author_data = __author__.split(' ')
maintainer = ' '.join(author_data[0:-1])
maintainer_email = author_data[-1][1:-1]
desc = 'A library to manipulate gettext files (po and mo files).'

if polib.PY3:
    enc = {'encoding': 'UTF-8'}
else:
    enc = {}

long_desc = r'''
%s

%s

''' % (open('README.rst', **enc).read(), open('CHANGELOG', **enc).read())

if __name__ == '__main__':
    setup(
        name='polib',
        description=desc,
        long_description=long_desc,
        version=polib.__version__,
        author=maintainer,
        author_email=maintainer_email,
        maintainer=maintainer,
        maintainer_email=maintainer_email,
        url='http://bitbucket.org/izi/polib/',
        download_url='https://pypi.python.org/packages/source/p/polib/polib-%s.tar.gz' % polib.__version__,
        license='MIT',
        platforms=['posix'],
        classifiers = [
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.5',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.0',
            'Programming Language :: Python :: 3.1',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Internationalization',
            'Topic :: Software Development :: Localization',
            'Topic :: Text Processing :: Linguistic'
        ],
        py_modules=['polib']
    )

