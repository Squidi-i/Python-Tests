import unittest
from coffee import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):
    def test_get_price_existing_item(self):
        coffee = CoffeeMenu()
        price = coffee.menu['latte']
        self.assertEqual(price, 2.75)
        
    def test_get_price_non_existing_item(self):
        coffee = CoffeeMenu()
        price = coffee.menu.get('banana')
        self.assertEqual(price, None)

if __name__ == '__main__':
  unittest.main()