import requests
import json
import logging
import time
from requests.exceptions import HTTPError

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)

def run():
    while True:
        main("http://localhost:8000/health")
        time.sleep(60)

def main(url):
    try:
        r = requests.get(url)
        data = json.loads(r.content)
        logging.info("Сервер доступний. Час на сервері: %s", data['date'])
        logging.info("Запитувана сторінка: : %s", data['current_page'])
        logging.info("Інформація про сервер: : %s", data['server_info'])
        logging.info("Інформація про користувача: : %s", data['client_info'])
    except Exception as ex:
        logging.error("Web сторінка недоступна. Помилка: %s", ex)


if __name__ == '__main__':
    run()

