#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT (see LICENSE file provided)
# vim600: fdm=marker tabstop=4 shiftwidth=4 expandtab ai

"""
polib setup script.
"""

__author__   = 'David Jean Louis <izimobil@gmail.com>'
__version__  = '0.5.0'

from distutils.core import setup

author_data = __author__.split(' ')
maintainer = ' '.join(author_data[0:-1])
maintainer_email = author_data[-1]
desc = 'A library to manipulate gettext files (po and mo files).'
long_desc = '''
.. contents:: Table of Contents

%s

%s

========
METADATA
========
''' % (open('README').read(), open('CHANGELOG').read())

if __name__ == '__main__':
    setup(
        name='polib',
        description=desc,
        long_description=long_desc,
        version=__version__,
        author=maintainer,
        author_email=maintainer_email,
        maintainer=maintainer,
        maintainer_email=maintainer_email,
        url='http://code.google.com/p/polib/',
        download_url='http://polib.googlecode.com/files/polib-%s.tar.gz' % __version__,
        license='MIT',
        platforms=['posix'],
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: System Administrators',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: French',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Internationalization',
            'Topic :: Software Development :: Localization',
            'Topic :: Text Processing :: Linguistic'
        ],
        py_modules=['polib']
    )

