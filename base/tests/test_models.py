from unittest import skip
from django.db.models import QuerySet
from .test_base import BaseTestCase

class PromptTests(BaseTestCase):

    @skip
    def test_list(self):
        #!!! Users not implemented yet
        pass

    @skip
    def test_like_count(self):
        #!!! Users not implemented yet
        pass

    def test_prompt_representation(self):
        """Test the string representation of a Prompt instance equals its body """
        prompt_body = self.prompt1.body
        prompt_repr = repr(self.prompt1)

        self.assertEqual(prompt_body, prompt_repr)

    def test_tags_return_value(self):
        """Test .tags return value is a QuerySet"""
        tags =  self.prompt1.tags
        self.assertIsInstance(tags, QuerySet)

    def test_new_prompt_has_no_tags(self):
        """Test a new prompt has no tags by default"""
        tags = self.prompt1.tags

        self.assertEqual(tags.count(), 0)
        self.assertQuerySetEqual(tags, [])

    def test_prompt_returns_correct_tags(self):
        """Test .tags returns all associated tags to Prompt"""
        self.prompt1.tag.add(self.tag1, self.tag2)
        tags = self.prompt1.tags

        self.assertEqual(tags.count(), 2)
        self.assertQuerySetEqual(tags, self.list2, ordered=False)
