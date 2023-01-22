import unittest
from django.test import Client
from food_api.models import Topping, Food, FoodCategory


class GetFoodTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.category = FoodCategory.objects.create(name='Main dishes')
        self.topping = Topping.objects.create(name='Cheese')
        self.food1 = Food.objects.create(
            name='Pizza',
            category=self.category,
            price=10,
            is_special=True,
            is_vegan=False
        )
        self.food1.toppings.add(self.topping)
        self.food2 = Food.objects.create(
            name='Salad',
            category=self.category,
            price=5,
            is_special=False,
            is_vegan=True
        )
        self.food2.toppings.add(self.topping)

    def test_get_foods_with_filters(self):
        response = self.client.get('/api/foods?is_special=true&is_vegan=false')
        self.assertEqual(response.status_code, 200)
        food1 = Food.objects.get(id=self.food1.id)
        self.assertEqual(response.json()[0]['foods'][0]['name'], food1.name)

    def test_get_foods_with_filters_no_result(self):
        response = self.client.get('/api/foods?is_special=false&is_vegan=false')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)

    def test_is_list(self):
        response = self.client.get('/api/foods')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json(), list)
