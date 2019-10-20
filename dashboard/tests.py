from django.test import TestCase


# Create your tests here.
class TestViews(TestCase):
    def test_get_dashboard_page(self):
        '''
        Tests that the dashboard view renders the dashboard template
        '''
        page = self.client.get("/dashboard/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dashboard.html")
