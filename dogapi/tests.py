#dogapi/tests.py

# Add these imports at the top
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.dog_data = {'name': 'Dog1'}
        self.response = self.client.post(
            reverse('create'),
            self.dog_data,
            format="json")

    def test_api_can_create_a_dog(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    # dogapi/tests.py

    def test_api_can_get_a_dog(self):
        """Test the api can get a given dog."""
        dog = Dog.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': dog.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, dog)

    def test_api_can_update_dog(self):
        """Test the api can update a given dog."""
        change_dog = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': dog.id}),
            change_dog, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_dog(self):
        """Test the api can delete a dog."""
        dog = Dog.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': dog.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
