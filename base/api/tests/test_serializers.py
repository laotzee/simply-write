from base.api.serializers import PromptSerializer
from base.tests.test_base import ModelTestCase

class TestPromptSerializer(ModelTestCase):
    """Test base API serializers"""

    def test_serializer_output(self):
        """Test if all prompt related fields are rendered as expected"""

        # Given a prompt and its serialized representation
        prompt = self.prompt1
        serialized = PromptSerializer(prompt).data

        # Serializer uses date in ISO format, so
        prompt_date =  prompt.created.strftime('%Y-%m-%dT%H:%M:%S.%f') + 'Z'

        # Verify each field is rendered as expected
        self.assertEqual(prompt.id, serialized['id'])
        self.assertEqual(prompt.body, serialized['body'])
        self.assertEqual(prompt_date, serialized['created'])
        self.assertQuerySetEqual(prompt.tag.all(), serialized['tag'], ordered=False)
        self.assertQuerySetEqual(prompt.likes.all(), serialized['likes'], ordered=False)