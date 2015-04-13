from django.test.utils import override_settings
from yet_another_django_profiler.tests.test_parameters import ParametersTest


@override_settings(YADP_PROFILER_BACKEND='yappi')
class YappiTest(ParametersTest):
    def test_calls_by_time(self):
        """Using profile=time should show a table of function calls sorted by internal time"""
        response = self._get_test_page('profile=time')
        self.assertContains(response, 'Ordered by: internal time')
