# polib Makefile, useful for developers only.
# Make sure you have pep8 and tox python modules installed.

.PHONY: clean lint test dist

all: lint test clean

clean:
	@find . -name '*.pyc' |xargs rm -f
	@find . -name '*.pyo' |xargs rm -f
	@find . -name '*.orig' |xargs rm -f
	@rm -rf MANIFEST build dist .coverage .tox __pycache__ docs/_build *.egg-info

lint:
	@type pycodestyle >/dev/null 2>&1 || { echo >&2 "Please install pycodestyle package."; exit 1; }
	@pycodestyle -r polib.py && { echo >&2 "PEP8: congrats, everything is clean !"; }

test:
	@type tox >/dev/null 2>&1 && { tox; } || { ./runtests.sh; }

dist: clean
	@python setup.py register
	@python setup.py sdist upload
	@python setup.py bdist_wheel upload
