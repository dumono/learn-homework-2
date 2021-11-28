"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_ALL, "russian")

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    now = datetime.now()
    print(now.strftime("%d %B %Y"))
    print((now - timedelta(1)).strftime("%d.%m.%Y"))
    print((now - timedelta(30)).strftime("%Y-%m-%d %H:%M"))

    new_date = datetime.strptime("01/01/20 12:10:03.234567", "%d/%m/%y %H:%M:%S.%f")
    print(new_date)


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
