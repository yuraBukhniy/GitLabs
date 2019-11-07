1. ����������� ���������� pipenv �� ��������� �������� ������:  
```bash
pipenv --python 3.7
pipenv install django
```
2. �� ��������� Django Framework ������� ��������� ���� ������� my_site.
```bash
pipenv run django-admin startproject my_site
```
3. �������� Django ������.
```bash
pipenv run python manage.py runserver
```
   � ������� ��� ��-������ 127.0.0.1:8000.  
![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab3/images/django_server.png)
4. ������� �������� ���� ������� (main).
```bash
pipenv run python manage.py startapp main
```
5. ³���������� ����� my_site/settings.py �� my_site/urls.py.
6. ��� ������� ������� � URL ������� �������� ���� main/urls.py.
7. �������� ������.
   ������� �������:  
![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab3/images/main_page.png)
   ������� health:  
![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab3/images/health.png)
   ������� ���� �����.