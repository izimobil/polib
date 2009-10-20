#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT (see LICENSE file provided)
# vim600: fdm=marker tabstop=4 shiftwidth=4 expandtab ai

"""
polib setup script.
"""

__author__   = 'David JEAN LOUIS <izimobil@gmail.com>'
__version__  = '0.4.3'

from distutils.core import setup

author_data = __author__.split(' ')
readme_file = open('README', 'r')

maintainer = ' '.join(author_data[0:-1])
maintainer_email = author_data[-1]
desc = 'A library to manipulate gettext files (po and mo files).'
long_desc = '''polib provides a simple and pythonic API to manipulate, create,
modify gettext files (pot, po and mo files).
You can load existing files, iterate through it's entries, add, modify entries,
comments or metadata, etc... or create new files from scratch.'''

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

