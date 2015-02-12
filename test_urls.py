# encoding: utf-8
# Created by Jeremy Bowman on Fri Feb 21 14:28:40 EST 2014
# Copyright (c) 2014 Safari Books Online. All rights reserved.
"""
URL configuration for Yet Another Django Profiler tests.
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)
