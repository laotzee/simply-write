from django.test import TestCase
from base.models import Prompt, User, Tag

class ModelTestCase(TestCase):
    """Sets up environment for testing base models"""
    @classmethod
    def  setUpClass(cls):
        super().setUpClass()

        cls.tag1 = Tag.objects.create(name='Love', click_count=50)
        cls.tag2 = Tag.objects.create(name='Greed')

        cls.prompt1 = Prompt.objects.create(body='“No. We can’t… we are too toxic for each other.”')
        cls.prompt2 = Prompt.objects.create(body='“No one touches what’s mine. Not even the gods.”')

        cls.list1 = [cls.tag1]
        cls.list2 = cls.list1.copy() + [cls.tag2]