from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.

# ######## register test cases #########
# ######## start #########
class UserRegistrationTests(APITestCase):
    def test_register_success(self):
        url = reverse('register')
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpass"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('message', response.data)

        # assert again to check database
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_register_fail_missing_username(self):
        url = reverse('register')
        data = {
            "email": "test@example.com",
            "password": "testpass"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
# ######### end ##########

# ######### login test cases ##########
# ######### start ##########
# class UserLoginTests(APITestCase):
#     def setUp(self):


# ######### end ##########