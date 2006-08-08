#!/usr/bin/env python
# -*- coding: latin-1 -*-
#
# License: MIT (see LICENSE file provided)


"""
polib setup script.
"""

__author__   = 'David JEAN LOUIS <izimobil@gmail.com>'
__version__  = '0.1.0'

from distutils.core import setup

maintainer = 'David JEAN LOUIS'
maintainer_email = 'izimobil@gmail.com'
desc = 'A library to manipulate gettext catalogs files (.po/.mo files).'
long_desc = """polib allows you to manipulate, create, modify gettext \
.pot/.po/.mo files.  You can load existing files, iterate through it's \
entries, add, modify entries, comments or metadata, etc... or create new \
po/pot files from scratch."""

if __name__ == '__main__':
    setup(
        name='polib',
        description=desc,
        long_description=long_desc,
        version='0.1.0',
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
# vim600: fdm=marker tabstop=4 shiftwidth=4 expandtab ai
