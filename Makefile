# polib Makefile, useful for developers only.
# Make sure you have pep8 and tox python modules installed.

all: lint test clean

clean:
	@find . -name '*.pyc' |xargs rm -f
	@rm -rf MANIFEST build dist .coverage .tox .venv __pycache__ docs/_build

lint:
	@type pep8 >/dev/null 2>&1 || { echo >&2 "Please install pep8 package."; exit 1; }
	@pep8 -r polib.py && { echo >&2 "PEP8: congrats, everything is clean !"; }

test:
	@type tox >/dev/null 2>&1 && { tox; } || { ./runtests.sh; }

dist: clean
	@python setup.py sdist
