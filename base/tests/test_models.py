from unittest import skip
from django.db.models import QuerySet
from .test_base import ModelTestCase

class PromptTests(ModelTestCase):
    """Test suite for Prompt model methods and behaviours"""

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
        # Given an initial state
        prompt_body = self.prompt1.body
        prompt_repr = repr(self.prompt1)

        # Verify both variables have the same value
        self.assertEqual(prompt_body, prompt_repr)

    def test_tags_return_value(self):
        """Test .tags return value is a QuerySet"""
        # Given an initial state
        tags =  self.prompt1.tags

        # Verify tags return value is of type QuerySet
        self.assertIsInstance(tags, QuerySet)

    def test_new_prompt_has_no_tags(self):
        """Test a new prompt has no tags by default"""
        # Given an initial state
        tags = self.prompt1.tags

        self.assertQuerySetEqual(tags, [])

    def test_prompt_returns_correct_tags(self):
        """Test .tags returns all associated tags to Prompt"""
        # Given an initial state
        self.assertQuerySetEqual(self.prompt1.tags, [])

        # When Tags are added the prompt
        self.prompt1.tag.add(self.tag1, self.tag2)
        tags = self.prompt1.tags

        # Verify prompt tags are updated
        self.assertQuerySetEqual(tags, self.list2, ordered=False)

class TagTests(ModelTestCase):
    """Test suite for Tag model"""

    def test_count(self):
        """Test count method of a tag"""
        # Given two tags of initial value 50 and 0 respectively
        tag1 = self.tag1
        tag2 = self.tag2

        # Verify count method return value is congruent with initial state
        self.assertEqual(self.tag1.count(), 50)
        self.assertEqual(self.tag2.count(), 0)

    def test_increase_count_function(self):
        """Test increase_count behaviour"""
        # Given an initial state
        self.assertEqual(self.tag1.count(),50)
        self.assertEqual(self.tag2.count(),0)

        # When incrementing both tags
        self.tag1.increase_count()
        self.tag2.increase_count()

        # Verify increase
        self.assertEqual(self.tag1.count(), 51)
        self.assertEqual(self.tag2.count(), 1)

    def test_increase_count_is_chainable(self):
        """Test increase_count chain behaviour"""
        # Given an tag
        tag = self.tag1

        # Get its return value from increase_count method
        returned_obj = tag.increase_count()

        # Verify return value is equal to instance itself
        self.assertEqual(returned_obj, self.tag1)

    def test_get_prompts_return_value(self):
        """Test get_prompts method return value is a QuerySet"""
        # Given an initial state
        prompts = self.tag1.get_prompts()

        # Verify prompts return value is of type QuerySet
        self.assertIsInstance(prompts, QuerySet)

    def test_get_prompts_with_no_return(self):
        """Test the return value of get_prompts when there are no prompts with such tag"""
        # Given a tag that has not being assigned to any prompt
        unassigned_tag = self.tag1

        # Get return value from its get_prompt method
        return_val = unassigned_tag.get_prompts()

        # Verify the tag is empty
        self.assertQuerySetEqual(return_val, [])

    def test_get_prompts_with_return(self):
        """Test the return value of get_prompts when there are prompts with such tag"""
        # Given an initial state
        self.assertQuerySetEqual(self.tag1.get_prompts(), [])
        self.assertQuerySetEqual(self.tag2.get_prompts(), [])

        # Add two tags to prompt
        self.prompt1.tag.add(self.tag1, self.tag2)

        # Prompt can be accessed through both tags
        self.assertQuerySetEqual(self.tag1.get_prompts(), [self.prompt1], ordered=False)
        self.assertQuerySetEqual(self.tag2.get_prompts(), [self.prompt1], ordered=False)

    def test_tag_representation(self):
        """Test tag representation equals its name"""
        # Given an initial state
        tag_name = self.tag1.name
        tag_repr = repr(self.tag1)

        # Verify both variables have the same value
        self.assertEqual(tag_repr, tag_name)