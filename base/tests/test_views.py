from .test_base import ModelTestCase
from ..models import Prompt

class TestHomeView(ModelTestCase):
    """Test suit for home view"""

    def test_view_status_code(self):
        """Test home view returns the correct status code"""
        # Given a user GET request to home
        response = self.client.get('/')

        # Verify the response status code is 200
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        """Test home view is using the correct template"""
        # Given a user GET request to home with a 200 response
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # Verify the template the correct template is used
        self.assertTemplateUsed(response, 'base/home.html')

    def test_view_context_with_existing_prompt(self):
        """Test a prompt is in the context of the response"""
        # Given a user get request to home with a 200 response
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # Access the response context
        context = response.context

        # Verify 'prompt' key exist and a prompt appears in the context
        self.assertIn('prompt', context)  # Check if 'key' is in the context
        self.assertIsInstance(context['prompt'], Prompt)  # Check the value of 'key'

    def test_view_context_with_no_prompt(self):
        """Test None in the context if the database has no prompts"""
        # Given no prompts in the database
        Prompt.objects.all().delete()

        # And given a user get request to home with a 200 response
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

        # Access the response context
        context = response.context

        # Verify 'prompt' key exist and a prompt appears in the context as None
        self.assertIn('prompt', context)
        self.assertIsInstance(context['prompt'], type(None))

class TestWritingView(ModelTestCase):
    """Test suite for writing view"""

    def test_view_status_code(self):
        """Test writing view returns the correct status code"""
        # Given a user GET request to writing
        response = self.client.get('/writing/')

        # Verify the response status code is 200
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        """Test writing view is using the correct template"""
        # Given a user GET request to home
        response = self.client.get('/writing/')

        # Verify the template the correct template is used
        self.assertTemplateUsed(response, 'base/writing.html')