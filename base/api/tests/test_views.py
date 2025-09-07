from django.test import TestCase
from base.tests.test_base import ModelTestCase
from base.models import Prompt
from base.api import views
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

class TestGetPrompt(ModelTestCase):

    def setUp(self):
        self.client = APIClient()

    def test_status_code_200(self):
        """Test view returns the correct status code"""
        # Given a response to a client request
        response = self.client.get(reverse('prompt'))

        # Verify the status code is 200
        self.assertEqual(response.status_code, 200)

    def test_status_code_404(self):
        """Test the view returns status code 404 if there is no records on the database"""
        # Given an empty database and a client request
        Prompt.objects.all().delete()
        response = self.client.get(reverse('prompt'))

        # Verify the status code is 404 and its status is error
        self.assertEqual(response.status_code, 404)

    def test_response_structure(self):
        """Test the successful structure of the API response """
        # Given a successful response to a client request
        response = self.client.get(reverse('prompt'))
        self.assertEqual(response.status_code, 200)
        data = response.data

        # Verify the JSON structure
        self.assertIn('status', data)
        self.assertIn('data', data)
        self.assertIn('message', data)

    def test_200_status_code_and_status(self):
        """Test 200 status code and the JSON 'success' status are congruent"""
        # Given a response to a client request
        response = self.client.get(reverse('prompt'))

        # Verify the state is congruent
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.status_code, 200)


    def test_404_status_code_and_status(self):
        """Test 404 status code and the JSON 'error' status are congruent"""
        # Given an empty database and a client request
        Prompt.objects.all().delete()
        response = self.client.get(reverse('prompt'))

        # Verify the state is congruent
        self.assertEqual(response.data['status'], 'error')
        self.assertEqual(response.status_code, 404)

