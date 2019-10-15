import requests
import ntplib
from datetime import datetime


def get_time_if_url_not_work():
    c = ntplib.NTPClient()
    response = c.request('0.ua.pool.ntp.org', version=3)
    t = datetime.fromtimestamp(response.tx_time).time().strftime('%H:%M:%S %p')
    d = datetime.fromtimestamp(response.tx_time).date().strftime('%Y-%m-%d')
    date = {"date": d, "time": t}
    return date



def main(url=''):
    if not url:
        print("No URL passed to function")
        return False
    try:
        r = requests.get(url=url)
        d = r.json()
    except:
        d = get_time_if_url_not_work()
    if "time" in d.keys():
        print(home_work(d['time']))
        print("Time is: ", d['time'])
    try:
        print("Date is: ", d['date'])
    except KeyError:
        print("No date in response!!!")
        raise KeyError

    return True


def home_work(time):
    try:
        am_or_pm = time.split()[1]
    except:
        result = "Неправильний формат часу!"
        return result
    if am_or_pm == "AM":
        result = "Доброї ночі"
    elif am_or_pm == "PM":
        result = "Доброго дня"
    else:
        result = "Неправильний формат часу!"
    return result


if __name__ == "__main__":
    a = "="*40
    print(a + "\nРезультат без параметрів: ")
    main()
    print(a + "\nРезультат з правильною URL: ")
    main('http://date.jsontest.com/')
