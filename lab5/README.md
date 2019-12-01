1. Після ініціалізації середовища виконав команди записані нижче:
    ```bash
    pipenv --python 3.7
    pipenv install -r requirements.txt
    pipenv run python app.py
    ```
    Додаток app.py запустився, але з помилками. Для їх виправлення встановив та запустив сервер redis за допомогою команди `sudo apt-get install redis-server && sudo systemctl start redis-server.service`. Після цього у файлі hosts прописав: `127.0.0.1   redis`. Тепер сайт запускається.  
    Щоб запускалася сторінка /logs потрібно в папці `my_app` створити папку `logs`, де буде знаходитись лог-файл.  
    Перевірив роботу сайту перейшовши на кожну із сторінок.  
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img1.png)
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img2.png)
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img3.png)
2. Ознайомився із вмістом `Dockerfile` та `Makefile` та його директивами. Розпишіть у Вашому `README.md` файлі що робить кожна директива `Makefile`;

3. Використовуючи команду `make` створив Docker імеджі для додатку (`sudo make app`) та для тестів (`sudo make tests`). Запустив додаток:
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img4.png)
    Запустив тести.
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img5.png)
    Перевірив роботу веб-сайту.
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img6.png)
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img7.png)
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img8.png)
4. Зупинив проект натиснувши `Ctrl+C` та почистив всі ресурси Docker за допомогою команди `sudo make docker-prune`.
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img9.png)
5. Створив директиву в `Makefile` для завантаження створених імеджів у Docker Hub репозиторій. Завантажив імеджі до свого репозиторію;
    ```bash
    docker-push:
	@docker push $(REPO):app
	@docker push $(REPO):tests
    ```
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img10.png)
6. Також видалив створені та закачані імеджі. Створив для цього директиву в `Makefile`.
    ```bash
    docker-purge:
	@docker image prune -a --force
    ```
    Команда `docker images` виводить пусті рядки.  
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img11.png)
7. Переходжу до іншого варіанту з використанням `docker-compose.yml`. Для цього створив даний файл у кореневій папці проекту та заповнив вмістом з прикладу.
    
8. Запустив `docker-compose`;  
    ```bash
    docker-compose -p lab5 up
    ```
    Перед запуском змінив репозиторій у тегах, прописаних у `docker-compose.yml`, на власний.  
9. Веб-сайт працює:
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img12.png)
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img13.png)
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img14.png)
    Щоб відкрити сайт треба ввести інший номер порта - 80. Він прописаний у файлі `docker-compose.yml`. Хоча можна і зовсім не вводити номер порта, ввівши лише адресу `0.0.0.0`, оскільки 80 - номер порта для HTTP протоколу.
10. Зупинив проект і почистив ресурси створені компоуз `docker-compose down`;
11. Завантажив створені імеджі до Docker Hub репозиторієм за допомого команди:
    ```bash
    docker-compose push
    ```
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img15.png)
12. Що на Вашу думку краще використовувати `Makefile` чи `docker-compose.yaml`?
13. Створив `docker-compose.yml` для лабораторної №4. Запустив проект: `sudo docker-compose lab4 up`
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img16.png)
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img17.png)
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img18.png)
    
