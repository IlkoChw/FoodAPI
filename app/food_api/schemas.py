from ninja import Schema, ModelSchema
from food_api.models import Food, FoodCategory
from pydantic import Field


class FoodSchema(ModelSchema):
    class Config:
        model = Food
        model_exclude = ['category', 'created', 'modified']

    toppings: list

    @staticmethod
    def resolve_toppings(food: Food):
        return [topping.name for topping in food.toppings.all()]


class FoodCategorySchema(ModelSchema):

    foods: list[FoodSchema]

    class Config:
        model = FoodCategory
        model_fields = ['id', 'name']


class ToppingFilterSchema(Schema):
    name__in: list[str] = Field(None, alias="toppings")


class FoodFilterSchema(Schema):
    is_special: bool = None
    is_vegan: bool = None


