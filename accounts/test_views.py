from django.test import TestCase
from django.shortcuts import reverse


class TestViews(TestCase):
    def test_get_home_page(self):
        '''
        Tests that the index view renders the home page
        '''
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
