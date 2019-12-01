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
2. Ознайомився із вмістом `Dockerfile` та `Makefile` та його директивами:
    - STATES := app tests - присвоює змінній STATES розширений діапазон значень (app, tests), які перебираються при виконанні. У даному випадку оператор присвоєння має вигляд := - це означає, що значення буде присвоєно на момент декларації (об'явлення) змінної. Наприклад присвоєння через просте = присвоїть значення змінній тільки на момент виконання. В даній змінній описані назви так званих таргетів (targets) або цілей, іменя яких позначають яку ціль має виконати make.
    - REPO := ... - присвоюємо змінній назву нашого докер-хабу000i
    - .PHONY: $(STATES) - Зазвичай утиліта make вважає, шо цілі (targets) є файлами, вони використовуються щоб створювати файли з інших файлів, але прописавши таку команду, ми вказуємо утилііті make. що цілі є "несправжніми", тобто вони не являються файлами.
    - $(STATES): - прив'язує команди app та tests до певного правила, інструкції до якого прописані нижче з відступом. Виконання цього правила можна запустити шляхом вказання його назви, в даному випадку до цього правила прив'язано дві назви (app та tests);
    - @docker build -f Dockerfile.$(@) -t $(REPO):$(@) . - дана команда створює новий контейнер з контексту (файлів, що повинні використовуватися в майбутньому контейнері, в даному випадку в якості файлів використовуються всі, що знаходяться в даніій директорії (.) ) . В якості конфігураційного файлу для створ. контейнеру використовується Dockerfile.$(@). $(@) - це директива Makefile, що вказує на назву цілі (target). Так як дане правило використовується для двох різних цілей, ім'я докерфайлу буде залежати від вказаної цілі при виконанні make. Наприклад у випадку make app - файл буде мати назву Dockerfile.app. Прапорець -t вказує назву імеджу (image) контейнера та задає для нього тег (після :).
    - run - Дане правило виконує створення мережі для подальшої можливої взаємодії контейнерів між собою (docker network create --driver=bridge appnet). Далі ми запускаємо сервер-сховище (Redis) та раніше створений контейнер app. Параметр --rm - вказує на те, що контейнер буде видалено після закінчення його роботи, або по завершенню docker-процесу (daemon). --name - задає human readable (читабельне) ім'я контейнеру, що є необхідним якщо ми хочемо зробити щось з цим контейнером в майбутньому ми зможемо звернутись до нього за іменем. --net= - задає ім'я мережі, яку має використовувати контейнер, в даному випадку це раніше створена мережа appnet. Прапорець -d вказує на те, щоб контейнер запускався в бекграунді (background), тобто у фоновому режимі. Параметр -i (--interactive) та -t (--tty) створюють інтерактивний режим з прив'язкою до терміналу. В такому режимі можна взаємодіяти з контейнером та виконувати команди всередині контейнера. -p 5000:5000 - вказує що контейнер буде прив'язано до 5000 порту на машині на якій він запущений (5000:) та внутрішній порт контейнера (:5000).
    - docker-prune - Це правило описує видалення всіх раніше створених ресурсів, сховищ, контейнерів та мереж.
3. Використовуючи команду `make` створив Docker імеджі для додатку (`sudo make app`) та для тестів (`sudo make tests`). Запустив додаток:
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img4.png)
    Запустив тести.
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img5.png)  
    Перевірив роботу веб-сайту.  
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img6.png)  
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img7.png)  
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img8.png)  
4. Зупинив проект натиснувши `Ctrl+C` та почистив всі ресурси Docker за допомогою команди `sudo make docker-prune`.
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
7. Переходжу до іншого варіанту з використанням `docker-compose.yml`. Для цього створив даний файл у кореневій папці проекту та заповнив вмістом з прикладу. Майбутній проект міститиме дві мережі: `public` та `secret`.
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
11. Завантажив створені імеджі до Docker Hub репозиторію за допомого команди `sudo docker-compose push`.
12. Що на Вашу думку краще використовувати `Makefile` чи `docker-compose.yaml`?
    І перший і другий спосіб є зручними. Але використовуючи Makefile можна прописувати власні правила за бажанням та давати їм конретні назви, а потім викликати їх в будь-який момент для різних потреб. Використання yml-файлу зручніше в плані автоматизації тим, що він надає більш компактний спосіб описувати необхідні для роботи з контейнерами конфігурації.
13. Створив `docker-compose.yml` для лабораторної №4. Запустив проект: `sudo docker-compose lab4 up`
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img16.png)
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img17.png)
    ![alt text](https://github.com/yuraBukhniy/GitLabs/blob/master/lab5/img/img18.png)
    
