from django.test import TestCase
from django.urls import reverse, resolve
from .. import views


class TestSinglePrompt(TestCase):
    """Test suite for single random API prompt"""
    
    def test_generated_url(self):
        """Test the generated url from 'home' is correct"""
        # Given a generated url for 'home'
        url = reverse('prompt')

        # Verify it is equal to the path defined at '/'
        self.assertEqual(url,'/api/v1/prompt/')

    def test_url_resolves_to_correct_view(self):
        """Test home url resolves to the correct view"""
        # Given a generated url for 'home'
        url = reverse('prompt')

        # Verify the view used for that url corresponds to the desired view
        self.assertEqual(resolve(url).func, views.get_prompt)