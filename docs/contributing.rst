.. _contributing:

Contributing to polib
=====================

You are very welcome to contribute to the project!
The bugtracker, wiki and mercurial repository can be found at the 
`project's page <https://github.com/izimobil/polib/>`_.

New releases are also published at the 
`"cheeseshop" (PyPI) <https://pypi.org/project/polib/>`_.

How to contribute
~~~~~~~~~~~~~~~~~

There are various possibilities to get involved, for example you can:

* `Report bugs <https://github.com/izimobil/polib/issues/new/>`_
  preferably with patches if you can
* Enhance this `documentation <https://github.com/izimobil/polib/tree/master/docs/>`_
* `Fork the code <https://github.com/izimobil/polib/>`_, implement new
  features, test and send a pull request

Running the test suite
~~~~~~~~~~~~~~~~~~~~~~

To run the tests, just type the following on a terminal::

    $ cd /path/to/polib/
    $ ./runtests.sh

You can also use tox::

    $ cd /path/to/polib/
    $ pip install tox
    $ tox

If you want to generate coverage information::

    $ pip install coverage
    $ ./runtests.sh
    $ coverage html
