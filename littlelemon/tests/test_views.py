from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import MenuTable
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu = MenuTable.objects.create(Title = 'Dosa', Price = 50, Inventory = '2')

    def test_get_all(self):
        response = self.client.get(reverse('restaurant/menu/'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        menu_list = MenuTable.objects.all()
        serializer = MenuSerializer(menu_list,many=True)
        self.assertEquals(response.data, serializer.data)
