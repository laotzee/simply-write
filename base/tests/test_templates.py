from django.template.loader import render_to_string
from .test_base import ModelTestCase

class TestHomeTemplate(ModelTestCase):
    """Test suite for home.html template"""

    def test_renders_without_errors(self):
        """Test home.html renders without throwing errors"""
        # Given a certain context
        context = {'prompt': self.prompt1}

        # Render home template
        rendered = render_to_string('base/home.html', context)

        # Verify no errors occurred
        self.assertIsNotNone(rendered)
        self.assertNotEqual(rendered.strip(), '')
        # Verify there is not server errors
        self.assertNotIn('TemplateDoesNotExist', rendered)
        self.assertNotIn('VariableDoesNotExist', rendered)
        # Verify the body of the prompt appears in the response
        self.assertIn(self.prompt1.body, rendered)
        # Verify template vars are replaced
        self.assertNotIn('{{prompt}}', rendered)

    def test_inheritance(self):
        """Test that home inherits correctly"""
        # Given a certain user response
        response = self.client.get('/')

        # Verify that correct templates were used
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'nav.html')
        # Verify that home.html template was used
        self.assertTemplateUsed(response, 'base/home.html')

    def test_variables_display(self):
        """Test context variables render correctly"""
        # Given the home template rendered with a certain context
        context = {
            'prompt': self.prompt1,
        }
        rendered = render_to_string('base/home.html', context)

        # Verify that variables appear correctly
        self.assertIn(str(self.prompt1), rendered)

class TestWritingTemplate(ModelTestCase):
    """Test suite for writing template"""

    def test_renders_without_errors(self):
        """Test writing.html renders without throwing errors"""
        # Given a render of the writing template
        rendered = render_to_string('base/writing.html')

        # Verify no errors occurred
        self.assertIsNotNone(rendered)
        self.assertNotEqual(rendered.strip(), '')
        # Verify there is not server errors
        self.assertNotIn('TemplateDoesNotExist', rendered)
        self.assertNotIn('VariableDoesNotExist', rendered)
        # Verify template vars are replaced

    def test_inheritance(self):
        """Test that writing inherits correctly"""
        # Given a certain user response
        response = self.client.get('/writing/')

        # Verify that correct templates were used
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'nav.html')
        # Verify that writing.html template was used
        self.assertTemplateUsed(response, 'base/writing.html')