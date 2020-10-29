# Testing Functionality of Contact Form

from django.test import TestCase
from .forms import ContactForm

# Create your tests here.


class ContactViewsTest(TestCase):
    def test_get_contact_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')


class ContactFormTest(TestCase):
    """
    Check that validation works when a user doesn't fill in at
    least one field, all fields are required, tests forms.py
    """
    def test_contact_form(self):
        form = ContactForm({
            'first_name': 'test name',
            'last_name': 'test last name',
            'contact_subject': 'test subject',
            'email': 'test@example.com',
            'contact_body': 'test contact body',
        })
        self.assertTrue(form.is_valid())

    def test_contact_first_name_is_required(self):
        form = ContactForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0],
                         'This field is required.')

    def test_contact_last_name_is_required(self):
        form = ContactForm({'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0],
                         'This field is required.')

    def test_contact_email_is_required(self):
        form = ContactForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0],
                         'This field is required.')

    def test_contact_subject_is_required(self):
        form = ContactForm({'contact_subject': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('contact_subject', form.errors.keys())
        self.assertEqual(form.errors['contact_subject'][0],
                         'This field is required.')

    def test_contact_body_is_required(self):
        form = ContactForm({'contact_body': ''})
        self.assertIn('contact_body', form.errors.keys())
        self.assertEqual(form.errors['contact_body'][0],
                         'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ContactForm()
        self.assertEqual(form.Meta.fields,
                         ['first_name', 'last_name', 'contact_subject',
                          'email', 'contact_body'])

