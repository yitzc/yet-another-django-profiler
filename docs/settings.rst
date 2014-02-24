Django settings for profiling
=============================

In order to get simple and meaningful profiling data, a few changes to your
Django settings may be in order:

* The `cached template loader <https://docs.djangoproject.com/en/1.6/ref/templates/api/#django.template.loaders.cached.Loader>`_
  should be used if you want to see data representative of performance after
  the templates used in the view have been loaded and cached.  The first URL
  visit after starting the server may still indicate a lot of time spent
  parsing the necessary templates, but later visits will show simpler data
  more representative of a typical visitor in production (assuming you've
  configured your production site correctly).

* ``TEMPLATE_DEBUG`` should be False to avoid spending more time processing
  templates than normal for the production site.

* If you're using ``django-debug-toolbar``, you should probably remove it from
  ``INSTALLED_APPS`` and ``MIDDLEWARE_CLASSES`` when profiling (otherwise the
  time spent preparing the toolbar can dwarf the time spent doing the main
  work of the view).

* Custom django-debug-toolbar panels (like
  `django-haystack-panel <https://github.com/streeter/django-haystack-panel>`_
  and the `template timings panel <https://github.com/orf/django-debug-toolbar-template-timings>`_
  should also be removed from ``INSTALLED_APPS`` if present.

I recommend using a separate settings file for use when profiling, which
imports your usual settings and then modifies them as appropriate to get
better profiling statistics.  Something like this can work::

    from .settings import *

    DEBUG = True
    TEMPLATE_DEBUG = False

    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
            'django.template.loaders.eggs.Loader',
        )),
    )

    INSTALLED_APPS = list(INSTALLED_APPS)
    if 'debug_toolbar' in INSTALLED_APPS:
        INSTALLED_APPS.remove('debug_toolbar')
    if 'haystack_panel' in INSTALLED_APPS:
        INSTALLED_APPS.remove('haystack_panel')
    if 'template_timings_panel' in INSTALLED_APPS:
        INSTALLED_APPS.remove('template_timings_panel')
    INSTALLED_APPS = tuple(INSTALLED_APPS)

    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
    if 'debug_toolbar.middleware.DebugToolbarMiddleware' in MIDDLEWARE_CLASSES:
        MIDDLEWARE_CLASSES.remove('debug_toolbar.middleware.DebugToolbarMiddleware')
    MIDDLEWARE_CLASSES.append('yet_another_django_profiler.ProfilerMiddleware')
    MIDDLEWARE_CLASSES = tuple(MIDDLEWARE_CLASSES)
