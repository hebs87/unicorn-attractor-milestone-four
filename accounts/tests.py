from django.test import TestCase


# Create your tests here.
class TestDjango(TestCase):

    def test_is_this_thing_on(self):
        '''
        Simple test to ensure test is working
        '''
        self.assertEquals(1, 1)
