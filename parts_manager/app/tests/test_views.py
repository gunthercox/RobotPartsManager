from django.test import TestCase
from django.core.urlresolvers import reverse


class ViewTests(TestCase):

    def test_main_page(self):
        main_url = reverse('main')
        response = self.client.get(main_url)

        self.assertEqual(response.status_code, 200)
