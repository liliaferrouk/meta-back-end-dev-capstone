from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create test instances of Menu
        Menu.objects.create(title='Menu 1', price=10, inventory=5)
        Menu.objects.create(title='Menu 2', price=15, inventory=10)

    def test_getall(self):
        # Retrieve all Menu objects from the url
        url = reverse('menu-list')  # 'menu-list' is the URL name for MenuItemsView
        response = self.client.get(url)

        # Serialize the retrieved data
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Compare the serialized data(that was in the database) with the response (got from the url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)