Related Projects
================

A lot of people have written middleware classes for Django profiling over the
years.  Here are some of the ones I directly took inspiration from:

* This `ProfileMiddleware gist <https://gist.github.com/kesor/1229681>`_
  disables itself when DEBUG is False, returns either a summary table or the
  raw profiling data file, and uses the
  `cProfile <http://docs.python.org/2/library/profile.html#module-cProfile>`_
  profiler

* This other `ProfileMiddleware <https://djangosnippets.org/snippets/2998/>`_
  got really fancy with the sorting options, but lacks a couple of the other
  features the one above has

* `geordi <https://bitbucket.org/brodie/geordi>`_ introduced using
  `Graphviz <http://www.graphviz.org>`_ and
  `Gprof2Dot <https://code.google.com/p/jrfonseca/wiki/Gprof2Dot>`_ to
  generate call graph PDFs

Honorable mentions
------------------

* `This ProfileMiddleware <https://djangosnippets.org/snippets/70/>`_ uses the
  older `hotshot <http://docs.python.org/2/library/hotshot.html#module-hotshot>`_
  profiler and writes the raw profiling data of all requests while active to
  disk

* `This other ProfileMiddleware <https://djangosnippets.org/snippets/186/>`_
  still uses the hotshot profiler, but uses a GET parameter and returns the
  profiling data summary in the browser

* And `this ProfileMiddleware <https://djangosnippets.org/snippets/605/>`_
  again uses the hotshot profiler and a GET parameter, but is a little
  fancier with the summary formatting

* This `ProfilerMiddleware <https://djangosnippets.org/snippets/727/>`_ was
  one of the first ones to use cProfile; GET parameter and in-browser data
  summary

* And this `variation <https://djangosnippets.org/snippets/1579/>`_ on the
  previous ProfilerMiddleware added the ability to sort the summary by the
  specified column

* `ProfilerMiddleware <https://github.com/omarish/django-cprofile-middleware>`_
  was packaged fairly nicely, uses cProfile, and allows sorting of the summary
  table

Dependencies
------------

Like the geordi middleware, this one uses Gprof2dot to generate call graphs.
There doesn't seem to be a current version of it nicely packaged for automatic
installation (a `rather old version <https://pypi.python.org/pypi/gprof2dot/1.0>`_
is on PyPI but doesn't appear when searching the site).  I've opened an
`issue <https://code.google.com/p/jrfonseca/issues/detail?id=91>`_ for this,
but haven't received a response yet.  In the meantime, I've bundled the script
in the yet-another-django-profiler distribution for ease of installation.

`Graphviz <http://www.graphviz.org/>`_ is the graph visualization library
used by Gprof2dot to do the graphics work.  It's a native library that needs
to be installed in a manner typical for the system it's running on, so that
needs to be done separately from the installation of this library (but isn't
strictly necessary if you just plan to use the statistics tables and not the
call graphs).

`sbo-sphinx <https://github.com/safarijv/sbo-sphinx>`_ contains some Sphinx
extensions and common configuration for the documentation of this and other
libraries being developed at Safari Books Online.  You don't need it to run
the middleware, but you'll want to install it if you use Sphinx to build the
documentation on your system.
