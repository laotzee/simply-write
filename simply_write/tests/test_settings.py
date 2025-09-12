from simply_write.settings import DEBUG
from django.test import TestCase
from unittest import skipIf



class SettingsTest(TestCase):


    # Look up how to pass a flag to say it is production of  not #!!!
    @skipIf(True, 'Not in production')
    def test_debug_is_off(self):
        """Test the server is not using debug mode for production"""
        self.assertEqual(DEBUG, False)

