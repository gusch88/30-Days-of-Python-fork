from datetime import datetime
from datetime import date
import math

default_names = ["Judith", "gunnar", "Ottilia", "lorelei"]
default_birthday = ["18.01.1989", "13.08.1988", "23.04.2018", "25.01.2021"]

message = """Hi {name},
I hope you are doing very well. On the date {date} you will be {years} old!
Bye"""


def make_message(names, birthday, date_input):
    if len(default_names) == len(default_birthday):
        age = make_age(date_input, default_birthday, years=True)
        i = 0
        for name in names:
            print(message.format(name=name.capitalize(), date=date_input, years=age[i]))
            i += 1


def make_age(date_input, birthday, years=False):
    list_age = []
    if not isinstance(date_input, date):
        form_date = datetime.strptime(date_input, "%d.%m.%Y")
    else:
        form_date = date_input

    for day in birthday:
        form_birthday = datetime.strptime(day, "%d.%m.%Y")
        if form_birthday < form_date:
            age = form_birthday - form_date
            if years:
                age = age.days / 365
            else:
                age.days
            list_age.append(math.floor(abs(age)))
    return list_age


if __name__ == '__main__':
    make_message(default_names, default_birthday, "10.07.2022")
