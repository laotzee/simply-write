from .test_base import ModelTestCase
from django.urls import reverse, resolve
from base import views

class TestHomeUrl(ModelTestCase):
    """Test suite for home url"""

    def test_generated_url(self):
        """Test the generated url from 'home' is correct"""
        # Given a generated url for 'home'
        url = reverse('home')

        # Verify it is equal to the path defined at '/'
        self.assertEqual(url,'/')

    def test_url_resolves_to_correct_view(self):
        """Test home url resolves to the correct view"""
        # Given a generated url for 'home'
        url = reverse('home')

        # Verify the view used for that url corresponds to the desired view
        self.assertEqual(resolve(url).func, views.home)

class TestWritingUrl(ModelTestCase):
    """Test suite for writing url"""

    def test_generated_url(self):
        """Test the generated url from 'writing' is correct"""
        # Given a generated url for 'writing'
        url = reverse('writing')

        # Verify it is equal to the path defined at '/writing/'
        self.assertEqual(url,'/writing/')

    def test_url_resolves_to_correct_view(self):
        """Test writing url resolves to the correct view"""
        # Given a generated url for 'writing'
        url = reverse('writing')

        # Verify the view used for that url corresponds to the desired view
        self.assertEqual(resolve(url).func, views.writing)