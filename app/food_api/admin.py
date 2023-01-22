from django.contrib import admin
from food_api.models import Topping, FoodCategory, Food


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_publish')


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'description', 'price', 'is_special', 'is_vegan', 'is_publish')
    list_editable = ('is_publish', )
    list_filter = ('is_publish', 'is_special', 'is_vegan', 'category__name', 'created', 'modified',)
    search_fields = ('name', 'category__name')
    filter_horizontal = ('toppings', )



