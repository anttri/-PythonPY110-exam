import random
import json
from faker import Faker
from conf import model

BOOKS = "books.txt"
INPUT_FILE = "input.json"

""" Функция вытаскивающая название книги из books.txt """


def title():
    with open(BOOKS, "r", encoding="utf-8") as f:
        book_list = []
        for b in f:
            book_list.append(b)
        random_book = random.choice(book_list)
        book = random_book.replace("\n", "")
    return book


""" Функция создающая ранодомный год """


def year():
    some_year = random.randrange(1990, 2021, 1)
    return some_year


""" Функция создающая ранодомную страницу """


def pages():
    some_page = random.randrange(1, 500, 1)
    return some_page


""" Функция создающая книжный номер, по стандарту isbn13 """


def isbn13():
    fake = Faker()
    return fake.isbn13()


""" Функция создающая ранодомный рейтинг """


def rating():
    some_rat = random.uniform(0.0, 5.0)
    return float(round(some_rat))


""" Функция создающая ранодомную цену книги """


def price():
    some_price = random.uniform(1.0, 1500.0)
    return float(round(some_price))


""" Функция создающая фйкового автора книга через faker """


def author():
    fake = Faker(locale="ru_RU")
    return fake.name()


""" Декортаор проверки длины названия книги """


def check_len(func):
    def wrapper():
        if len(title()) > 50:
            raise ValueError("Too long book name!")
        else:
            return func()
    return wrapper


""" Функция-генератор для создания словаря """


@check_len
def creat_dict():
    book_mod = {"model": model,
                "fields": {
                    "title": title(),
                    "year": year(),
                    "pages": pages(),
                    "isbn13": isbn13(),
                    "rating": rating(),
                    "price": price(),
                    "author": author()
                }
                }
    yield book_mod


""" Функция main """


def main():
    books_list = []

    for i in range(100):
        books_list.append(next(creat_dict()))

    with open(INPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(books_list, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
