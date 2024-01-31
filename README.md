# COOKS BOOK

## О проекте
Этот проект создавался как тестовое задание на вакансию "Python developer" в компанию ```Мир Говорит```.

### Подготовка к запуску

Для запуска проекта нужно создать в директории проекта виртуальное окружение.
```bash
python3 -m venv /путь/к/проекту
```

Затем необходимо запустить виртуальное окружение
```bash
source venv/bin/activate
```

Далее установить необходимые библиотеки и фреймворк django
```bash
pip3 install django
pip3 install mysqlclient
```
### Важно
Проект работает с базой данных mysql. Необходимо иметь на компьютере Mysql базу данных с названием cooks.
Либо изменить настройки и подключиться к своей СУБД.
### Запуск и работа проекта

После установки зависимостей, необходимо запустить проект командой
```bash
./manage.py runserver
```
### URL-адреса
add_product_to_recipe - добавляет к указанному рецепту указанный продукт с указанным весом. Если в рецепте уже есть такой продукт, то функция меняет его вес в этом рецепте на указанный.
```bash
add_product_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight> 
```
cook_recipe - увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт.
```bash
cook_recipe/<int:recipe_id>/
```
show_recipes_without_product - возвращает HTML страницу, на которой размещена таблица. В таблице отображены id и названия всех рецептов, в которых указанный продукт отсутствует, или присутствует в количестве меньше 10 грамм.
```bash
show_recipes_without_product/<int:product_id>
```

### АДМИНКА

Cоздать суперпользователя можно командой 
```bash
./manage.py createsuperuser
```
Для перехода в админ-панель необходимо перейти по адресу
```bash
http://127.0.0.1:8000/admin/
```