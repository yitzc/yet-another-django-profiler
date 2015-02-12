# encoding: utf-8
# Created by Jeremy Bowman on Fri Feb 21 14:28:40 EST 2014
# Copyright (c) 2014 Safari Books Online. All rights reserved.
"""
URL configuration for Yet Another Django Profiler tests.
"""

from django.conf.urls import patterns, url
from django.http import HttpResponse
from django.views.generic.base import View


class TestView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('This is only a test.')

urlpatterns = patterns(
    '',
    url(r'^test/', TestView.as_view(), name='test'),
)
