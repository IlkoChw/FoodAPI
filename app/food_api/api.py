from ninja import Router, Query
from food_api.models import Topping, Food, FoodCategory
from food_api.schemas import FoodCategorySchema, FoodFilterSchema, ToppingFilterSchema


router = Router()


@router.get("foods", response=list[FoodCategorySchema])
def list_foods(request, food_filters: FoodFilterSchema = Query(...), topping_filters: ToppingFilterSchema = Query(...)):

    topping_filters_dict = topping_filters.dict(exclude_none=True)

    food_filters_dict = food_filters.dict(exclude_none=True)
    food_filters_dict['is_publish'] = True
    if topping_filters_dict:
        toppings = Topping.objects.filter(**topping_filters_dict)

        food_filters_dict['toppings__in'] = toppings

    foods = Food.objects.filter(**food_filters_dict)

    food_ids = list(foods.values_list('pk', flat=True))

    categories = FoodCategory.objects.filter(is_publish=True)
    fields = ['id', 'name']

    result = []
    for cat in categories:
        cat_json = {}
        for attr in fields:
            cat_json[attr] = cat.__dict__[attr]

        foods_obj = list(cat.get_filtered_foods(food_ids))
        if foods_obj:
            cat_json['foods'] = foods_obj
            result.append(cat_json)

    return result
