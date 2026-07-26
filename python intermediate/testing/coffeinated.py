# Instructions
# Who ordered the latte? Probably me. ☕️

# Coffee shops are wonderful places to work and study. Like any small business, coffee shops require management to manage inventory, order processing, sales, and menus. Let's use what our knowledge of Python testing to make sure a coffee menu is up to date.

# First, set up testing:

# Create and save the coffee_menu.py file.
# Next, set up a CoffeeMenu class:

# In the class set up coffee menu items. It should look like this:
# class CoffeeMenu:
#   def __init__(self):
#     self.menu = {
#       'espresso': 2.50,
#       'latte': 2.75,
#       'cappuccino': 3.20,
#       'americano': 2.70
#     }

# Then, let's define a test class and write some tests:

# Create and save the test_coffee_menu.py file with the TestCoffeeMenu class.
# Write descriptive unit test using assertions (ex. test_get_price_existing_item(), test_get_price_non_existing_item(), test_add_item())
# After running the tests, observe the output to see if all tests pass successfully.

# What results did you get? Feel free to share on Twitter!

# And once again, happy testing! 🧪

import unittest

class CoffeeMenu:
    def __init__(self):
        self.menu = {
            'espresso': 2.50,
            'latte': 2.75,
            'cappuccino': 3.20,
            'americano': 2.70
        }

    # 获取饮品价格
    def get_price(self, name):
        return self.menu[name]

    # 添加新饮品
    def add_item(self, name, price):
        self.menu[name] = price


class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        # 每次测试前初始化实例
        self.coffee_menu = CoffeeMenu()

    # 测试存在饮品价格
    def test_get_price_existing_item(self):
        self.assertEqual(self.coffee_menu.get_price('latte'), 2.75)

    # 测试不存在饮品抛出KeyError
    def test_get_price_non_existing_item(self):
        with self.assertRaises(KeyError):
            self.coffee_menu.get_price('mocha')

    # 测试新增饮品功能
    def test_add_item(self):
        self.coffee_menu.add_item('mocha', 3.00)
        self.assertEqual(self.coffee_menu.get_price('mocha'), 3.00)


if __name__ == '__main__':
    unittest.main()
