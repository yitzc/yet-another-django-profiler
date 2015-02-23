yet-another-django-profiler Changelog
=====================================

0.3.0 (2015-02-23)
------------------
* Added "profile" management command for profiling other management commands
* Attempt to resolve absolute paths of Python modules to fully-qualified module
  names for more readable results, and added 2 new settings to customize this
* Upgraded gprof2dot.py (still bundled despite a recent version now being
  available on PyPI because it is slightly modified to use the new module name
  derivation code)
* Work around bug in Python >= 2.7.4 that doesn't recognize "file" as a valid
  sorting option (even though every other initial substring of "filename" is)

0.2.0 (2015-02-12)
------------------
Don't require particular Django versions (so pip won't try to auto-adjust it).

0.1.0 (2014-02-27)
------------------
Initial release
