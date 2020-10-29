# Testing Functionality of Profile Form, to save billing info

from django.test import TestCase
from .forms import UserProfileForm

# Create your tests here.


class ProfilesViewsTest(TestCase):
    """
    This tests that the redirect is working properly.
    """
    def test_get_profile_page(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)


class ProfileFormTest(TestCase):
    """
    Check that validation works when a user doesn't fill in at least one field
    """
    def test_profile_form(self):
        form = UserProfileForm({
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County or State',
        })
        self.assertTrue(form.is_valid())

