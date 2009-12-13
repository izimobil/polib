=====
polib
=====

Introduction
------------

polib allows you to manipulate, create, modify gettext files (pot, po and mo
files). You can load existing files, iterate through it's entries, add, modify
entries, comments or metadata, etc... or create new po files from scratch.

polib is pretty stable now and is used by many `opensource projects <http://code.google.com/p/polib/wiki/ProjectsUsingPolib>`_.


Installation
------------

Note: chances are that polib is already packaged for your linux/bsd system, if
so, we recommend you use your OS package system, if not then choose a method below:

Installing latest polib version with setuptools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

$ easy_install polib

Installing latest polib version with pip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

$ pip install polib

Installing latest polib version from source tarball
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Download latest version <http://code.google.com/p/polib/downloads/list>`_

::

$ tar xzfv polib-x.y.z.tar.gz
$ cd polib-x.y.z
$ python setup build
$ sudo python setup.py install

Installing the polib development version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note: this is **not recommended** in a production environment.

::

$ hg clone https://polib.googlecode.com/hg/ polib  
$ cd polib
$ python setup build
$ sudo python setup.py install

Basic usage example
-------------------

::

>>> import polib
>>> # load an existing po file
>>> po = polib.pofile('tests/test_utf8.po')
>>> for entry in po: print entry.msgid, entry.msgstr
>>> # add an entry
>>> entry = polib.POEntry(msgid='Welcome', msgstr='Bienvenue')
>>> entry.occurences = [('welcome.py', '12'), ('anotherfile.py', '34')]
>>> po.append(entry)
>>> # save our modified po file
>>> po.save()
>>> # compile mo file
>>> po.save_as_mofile('tests/test_utf8.mo')

Documentation
-------------

`A tutorial <http://code.google.com/p/polib/wiki/Tutorial>`_ is available and
you can also browse the `complete api documentation <http://www.izimobil.org/polib/api/>`_.

Development
-----------

Bugtracker, wiki and mercurial repository can be found at the `project's page
<http://code.google.com/p/polib/>`_.
New releases are also published at the `cheeseshop <http://cheeseshop.python.org/pypi/polib/>`_.


Credits
-------

**Author:** `David Jean Louis <izimobil@gmail.com>`_.

References
----------

* `Gettext Manual <http://www.gnu.org/software/gettext/manual/>`_
* `PO file format <http://www.gnu.org/software/gettext/manual/html_node/gettext_9.html>`_
* `MO file format <http://www.gnu.org/software/gettext/manual/html_node/gettext_136.html>`_

