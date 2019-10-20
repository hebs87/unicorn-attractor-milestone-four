from django.test import TestCase
from django.shortcuts import reverse


class TestViews(TestCase):
    def test_get_home_page(self):
        '''
        Tests that the index view renders the home template
        '''
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")


    def test_get_login_page(self):
        '''
        Tests that the index view renders the login template
        '''
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
