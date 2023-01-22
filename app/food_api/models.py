from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    modified = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"


class PubModel(models.Model):
    is_publish = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Topping(BaseModel):

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class FoodCategory(BaseModel, PubModel):

    class Meta:
        verbose_name = "Категория блюд"
        verbose_name_plural = "Категории блюд"

    def get_filtered_foods(self, ids: list[int]):
        return self.foods.filter(id__in=ids)


class Food(BaseModel, PubModel):
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='foods', verbose_name='Категория')
    description = models.TextField(blank=True, null=True, max_length=1024, verbose_name='Описание')
    toppings = models.ManyToManyField(Topping, blank=True, verbose_name='Ингредиенты')
    price = models.PositiveIntegerField(verbose_name='Цена')
    is_special = models.BooleanField(default=False, verbose_name='Специальное предложение')
    is_vegan = models.BooleanField(default=False, verbose_name='Вегетарианское блюдо')

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
