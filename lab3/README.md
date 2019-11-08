1. Ініціалізував середовище pipenv та встановив необхідні пакети:  
```bash
pipenv --python 3.7
pipenv install django
```
2. За допомогою Django Framework створив заготовку мого проекту my_site.
```bash
pipenv run django-admin startproject my_site
```
3. Запустив Django сервер.
```bash
pipenv run python manage.py runserver
```  
   У браузері ввів ІР-адресу 127.0.0.1:8000.  
![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab3/images/django_server.png)  
   4. Створив темплейт мого додатку (main).
```bash
pipenv run python manage.py startapp main
```
5. Відредагував файли my_site/settings.py та my_site/urls.py.
6. Щоб поєднати функції з URL шляхами заповнив файл main/urls.py.
7. Запустив сервер.  
   Головна сторінка:
![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab3/images/main_page.PNG)
   Сторінка health:  
![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab3/images/health.png)
   Виконав коміт сайту.
8. Встановив бібліотеку requests.
9. Модифікував функцію health на виведення необхідних даних.  
   Додав обробку винятку, якщо сторінка буде недоступною, використавши функцію logging.error().  
   Зробив так, щоб запит виконувався раз в хвилину за допомогою функції time.sleep().  
   Додав аліас на запуск сервера та моніторингу. Для цього додав секцію scripts у Pipfile, де прописав швидкі виклики команд.
10. Запустив сервер та моніторинг.
```bash
pipenv run server
pipenv run monitoring
```
![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab3/images/health_final.png)
   Під час моніторингу створив ситуацію, при якій моя веб-сторінка стала недоступною. Повідомлення про помилку записане в файлі логів server.logs.
![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab3/images/error.png)