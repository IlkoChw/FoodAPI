from django.test import TestCase

from food_api.models import Topping, Food, FoodCategory


class FoodTestCase(TestCase):
    def setUp(self):
        self.category = FoodCategory.objects.create(name='Main dishes')
        self.topping1 = Topping.objects.create(name='Cheese')
        self.topping2 = Topping.objects.create(name='Tomatoes')
        self.food = Food.objects.create(
            name='Pizza',
            category=self.category,
            price=10,
            is_special=True,
            is_vegan=False
        )
        self.food.toppings.add(self.topping1, self.topping2)

    def test_food_has_correct_category(self):
        self.assertEqual(self.food.category, self.category)

    def test_food_has_correct_toppings(self):
        toppings = self.food.toppings.all()
        self.assertEqual(len(toppings), 2)
        self.assertIn(self.topping1, toppings)
        self.assertIn(self.topping2, toppings)

    def test_food_has_correct_price(self):
        self.assertEqual(self.food.price, 10)

    def test_food_has_correct_special_status(self):
        self.assertTrue(self.food.is_special)

    def test_food_has_correct_vegan_status(self):
        self.assertFalse(self.food.is_vegan)


class FoodCategoryTestCase(TestCase):
    def setUp(self):
        self.category = FoodCategory.objects.create(name='Main dishes')
        self.food1 = Food.objects.create(
            name='Pizza',
            category=self.category,
            price=10,
            is_special=True,
            is_vegan=False
        )
        self.food2 = Food.objects.create(
            name='Salad',
            category=self.category,
            price=5,
            is_special=False,
            is_vegan=True
        )
        self.food3 = Food.objects.create(
            name='Soup',
            category=self.category,
            price=7,
            is_special=True,
            is_vegan=True
        )
        self.food4 = Food.objects.create(
            name='Steak',
            category=self.category,
            price=20,
            is_special=False,
            is_vegan=False
        )

    def test_get_filtered_foods(self):
        filtered_foods = self.category.get_filtered_foods([self.food1.id, self.food3.id])
        self.assertEqual(len(filtered_foods), 2)
        self.assertIn(self.food1, filtered_foods)
        self.assertIn(self.food3, filtered_foods)

    def test_get_filtered_foods_empty_list(self):
        filtered_foods = self.category.get_filtered_foods([])
        self.assertEqual(len(filtered_foods), 0)


class ToppingTestCase(TestCase):
    def setUp(self):
        self.topping = Topping.objects.create(name='Cheese')

    def test_topping_name(self):
        self.assertEqual(self.topping.name, 'Cheese')

    def test_topping_string_representation(self):
        self.assertEqual(str(self.topping), 'Cheese')
