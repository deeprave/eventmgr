from django.test import TestCase
from django.contrib.auth.models import User


class TestApi(TestCase):
    fixtures = ['test_localities.json']

    USERNAME = 'test'
    PASSWORD = 'test'

    def setup_auth(self):
        # Create a user and Log the client in
        user = User.objects.create_user(username=self.USERNAME, password=self.PASSWORD)
        self.assertTrue(self.client.login(username=self.USERNAME, password=self.PASSWORD))
        return user

    def test_country_list(self):
        response = self.client.get('/contacts/api/country/')
        # Check to make sure our auth wrapper works
        self.assertEqual(response.status_code, 403)
        self.setup_auth()
        # let's try again
        response = self.client.get('/contacts/api/country/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/contacts/api/country/?abbrev=AU')
        self.assertEqual(response.status_code, 200)
