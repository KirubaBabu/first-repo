from django.test import TestCase
from restaurant.models import MenuTable
class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuTable.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEquals(item, "IceCream : 80")