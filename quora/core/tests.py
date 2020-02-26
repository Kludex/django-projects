from django.test import TestCase
from .models import User


class LoginTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'demo',
            'email': 'demo@gmail.com',
            'password': 'secret',
            'first_name': 'demo',
            'last_name': 'user',
        }

    def test_register(self):
        response = self.client.post('/core/register/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_user(self):
        self.client.post('/core/register/', self.credentials, follow=True)
        user = User.objects.get(username='demo')
        self.assertEqual(user.username, 'demo')
