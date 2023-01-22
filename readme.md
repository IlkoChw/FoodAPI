<h2>Электронное меню для ресторана</h2>

<h3>Сборка и запуск контейнеров</h3>
<b>docker build -t food_api .</b>

<b>docker-compose up --build -d</b>

<h3>Загрузка фикстур</h3>
docker-compose exec web python manage.py loaddata food_api/fixtures/test_objects.json

<h3>Запуск юнит тестов</h3>
docker-compose exec web python manage.py test --verbosity 2

<h3>Food API</h3>
Панель администратора: <a href="http://localhost:8000">localhost:8000</a>

Документация и тестирование API: <a href="http://localhost:8000/api/docs">localhost:8000/api/docs</a>


<h3>TO DO</h3>
<ul>
<li> Оптимизировать GET api/foods
<li> Добавить методы для создания объектов: Topping, Food, FoodCategory
</ul>