Installation
============

[![Python package](https://github.com/chdemko/pandoc-beamer-arrow/workflows/Python%20package/badge.svg?branch=develop)](https://github.com/chdemko/pandoc-beamer-arrow/actions/workflows/python-package.yml)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-beamer-arrow/develop.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-beamer-arrow?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-beamer-arrow.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-beamer-arrow/)
[![Code Climate](https://codeclimate.com/github/chdemko/pandoc-beamer-arrow/badges/gpa.svg)](https://codeclimate.com/github/chdemko/pandoc-beamer-arrow/)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/chdemko/pandoc-beamer-arrow/develop.svg?logo=codefactor)](https://www.codefactor.io/repository/github/chdemko/pandoc-beamer-arrow)
[![Codacy](https://img.shields.io/codacy/grade/5e04e80fe4124ea18911026086fdafe9.svg?logo=codacy)](https://app.codacy.com/gh/chdemko/pandoc-beamer-arrow/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-beamer-arrow.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-beamer-arrow/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-beamer-arrow.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-beamer-arrow/)
[![License](https://img.shields.io/pypi/l/pandoc-beamer-arrow.svg?logo=pypi&logoColor=white)](https://raw.githubusercontent.com/chdemko/pandoc-beamer-arrow/develop/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-beamer-arrow?logo=pypi&logoColor=white)](https://pepy.tech/project/pandoc-beamer-arrow)
[![Development Status](https://img.shields.io/pypi/status/pandoc-beamer-arrow.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-beamer-arrow/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-beamer-arrow.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-beamer-arrow/)
[![Pandoc version](https://img.shields.io/badge/pandoc-2.11%20|%202.12%20|%202.13%20|%202.14%20|%202.15%20|%202.16%20|%202.17%20|%202.18%20|%202.19%20|%203.0%20|%203.1%20|%203.2%20|%203.3%20|%203.4%20|%203.5-blue.svg?logo=markdown)](https://pandoc.org/)
[![Latest release](https://img.shields.io/github/release-date/chdemko/pandoc-beamer-arrow.svg?logo=github)](https://github.com/chdemko/pandoc-beamer-arrow/releases)
[![Last commit](https://img.shields.io/github/last-commit/chdemko/pandoc-beamer-arrow/develop?logo=github)](https://github.com/chdemko/pandoc-beamer-arrow/commit/develop/)
[![Repo Size](https://img.shields.io/github/repo-size/chdemko/pandoc-beamer-arrow.svg?logo=github)](http://pandoc-beamer-arrow.readthedocs.io/en/latest/)
[![Code Size](https://img.shields.io/github/languages/code-size/chdemko/pandoc-beamer-arrow.svg?logo=github)](http://pandoc-beamer-arrow.readthedocs.io/en/latest/)
[![Source Rank](https://img.shields.io/librariesio/sourcerank/pypi/pandoc-beamer-arrow.svg?logo=libraries.io&logoColor=white)](https://libraries.io/pypi/pandoc-beamer-arrow)
[![Docs](https://img.shields.io/readthedocs/pandoc-beamer-arrow.svg?logo=read-the-docs&logoColor=white)](http://pandoc-beamer-arrow.readthedocs.io/en/latest/)

*pandoc-beamer-arrow* is a [pandoc] filter for creating arrows between text
elements for beamer presentation.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-beamer-arrow* requires [python], a programming language that comes
pre-installed on linux and Mac OS X, and which is easily installed
[on Windows].

Install *pandoc-beamer-arrow* using the bash command

~~~shell-session
$ pipx install pandoc-beamer-arrow
~~~

To upgrade to the most recent release, use

~~~shell-session
$ pipx upgrade pandoc-beamer-arrow
~~~

`pipx` is a script to install and run python applications in isolated
environments from the Python Package Index, [PyPI]. It can be installed
using instructions given [here](https://pipx.pypa.io/stable/).

Make sure you have the

* *xcolor*

LaTeX packages. On linux you have to install some extra libraries **before**
*pandoc-beamer-arrow*. On a Debian-based system (including Ubuntu), you can
install it as root using

~~~shell-session
$ sudo apt-get texlive-latex-extra
~~~

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with pandoc-beamer-arrow, please feel welcome to
[file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-beamer-arrow/issues

Contribute
==========

Instructions
------------

Install `hatch`, then run

~~~shell-session
$ hatch run pip install pre-commit
$ hatch run pre-commit install
~~~

to install `pre-commit` before working on your changes.

Tests
-----

When your changes are ready, run

~~~shell-session
$ hatch test
$ hatch fmt --check
$ hatch run lint:check
$ hatch run docs:build
$ hatch build -t wheel
~~~

for running the tests, checking the style, building the documentation
and building the wheel.
