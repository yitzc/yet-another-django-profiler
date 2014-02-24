#!/usr/bin/env python
# encoding: utf-8
"""
Sphinx configuration for documentation
"""

from sbo_sphinx.conf import *

project = 'yet-another-django-profiler'
apidoc_exclude = [
    os.path.join('docs', 'conf.py'),
    os.path.join('yet_another_django_profiler', 'tests'),
    'setup.py',
    'test_settings.py',
    'test_urls.py',
    've',
]
