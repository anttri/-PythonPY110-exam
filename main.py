import random
import json
from faker import Faker
from conf import model

BOOKS = "books.txt"
INPUT_FILE = "input.json"


def check_len(func):
    """ Декортаор проверки длины названия книги """
    def wrapper():
        if len(func()) > 50:
            raise ValueError("Too long book name!")
        else:
            return func()

    return wrapper


@check_len
def title():
    """ Функция вытаскивающая название книги из books.txt """
    with open(BOOKS, "r", encoding="utf-8") as f:
        book_list = []
        for b in f:
            book_list.append(b)
        random_book = random.choice(book_list)
        book = random_book.replace("\n", "")
    return book


def year():
    """ Функция создающая ранодомный год """
    some_year = random.randrange(1990, 2021, 1)
    return some_year


def pages():
    """ Функция создающая ранодомную страницу """
    some_page = random.randrange(1, 500, 1)
    return some_page


def isbn13():
    """ Функция создающая книжный номер, по стандарту isbn13 """
    fake = Faker()
    return fake.isbn13()


def rating():
    """ Функция создающая ранодомный рейтинг """
    some_rat = random.uniform(0.0, 5.0)
    return float(round(some_rat))


def price():
    """ Функция создающая ранодомную цену книги """
    some_price = random.uniform(1.0, 1500.0)
    return float(round(some_price))


def author():
    """ Функция создающая фйкового автора книга через faker """
    fake = Faker(locale="ru_RU")
    return fake.name()


def main():
    """ Функция main """
    books_list = []

    def creat_dict():
        """ Функция-генератор для создания словаря """
        book_mod = {"model": model,
                    "pk": count,
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

    count = 1

    for i in range(100):
        books_list.append(next(creat_dict()))
        count += 1

    with open(INPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(books_list, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
