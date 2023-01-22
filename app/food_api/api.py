from ninja import Router, Query
from food_api.models import Topping, Food, FoodCategory
from food_api.schemas import FoodCategorySchema, FoodFilterSchema, ToppingFilterSchema
from loguru import logger

router = Router()


@router.get("foods", response=list[FoodCategorySchema])
def list_foods(request, food_filters: FoodFilterSchema = Query(...), topping_filters: ToppingFilterSchema = Query(...)):

    topping_filters_dict = topping_filters.dict(exclude_none=True)
    logger.debug(f'Topping filters: {topping_filters_dict}')
    food_filters_dict = food_filters.dict(exclude_none=True)
    food_filters_dict['is_publish'] = True
    if topping_filters_dict:
        toppings = Topping.objects.filter(**topping_filters_dict)
        food_filters_dict['toppings__in'] = toppings

    logger.debug(f'Food filters: {food_filters_dict}')

    foods = Food.objects.filter(**food_filters_dict)
    food_ids = list(foods.values_list('pk', flat=True))

    categories = FoodCategory.objects.filter(is_publish=True)

    fields = ['id', 'name']
    response = []
    for category in categories:
        category_dict = {}
        for attr in fields:
            category_dict[attr] = category.__dict__[attr]

        foods_obj = list(category.get_filtered_foods(food_ids))
        if foods_obj:
            category_dict['foods'] = foods_obj
            response.append(category_dict)

    logger.debug(f'response GET api/foods: {response}')

    return response
