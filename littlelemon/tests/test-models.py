from django.test import TestCase
from restaurant.models import Menu

#this does work for some reasons that I don't know about

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = item.get_item()

        self.assertEqual(itemstr,"IceCream : 80")
