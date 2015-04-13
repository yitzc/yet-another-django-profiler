# encoding: utf-8
# Created by Jeremy Bowman on Fri Feb 21 12:15:29 EST 2014
# Copyright (c) 2014, 2015 Safari Books Online. All rights reserved.
#
# This software may be modified and distributed under the terms
# of the 3-clause BSD license.  See the LICENSE file for details.
"""
Tests for Yet Another Django Profiler
"""
from django.core.urlresolvers import reverse
from django.test.utils import override_settings
from django.test import TestCase


@override_settings(YADP_ENABLED=True)
class PageTest(TestCase):
    def _get_test_page(self, params=''):
        url = reverse('test')
        if params:
            url += '?' + params
        return self.client.get(url)