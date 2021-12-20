import random
import json

BOOKS = "books.txt"
INPUT_FILE = "input.json"


# Декортаор проверки длины названия книги
def check_len(func):
    def wrapper():
        if len(title()) > 50:
            raise IOError("Too long book name!")
        else:
            return func()
    return wrapper


# Основная функция
@check_len
def main():
    from conf import model
    book_list = []
    for i in range(100):
        i = {"model": model,
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
        book_list.append(i)

    with open(INPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(book_list, f, indent=4, ensure_ascii=False)


# Вытаскиваем название книги из books.txt
def title():
    with open(BOOKS, "r", encoding="utf-8") as f:
        book_list = []
        for i in f:
            book_list.append(i)
        random_book = random.choice(book_list)
        book = random_book.replace("\n", "")
        return book


# Делаем ранодомный год
def year():
    some_year = random.randrange(1990, 2021, 1)
    return some_year


# Делаем ранодомную страницу
def pages():
    some_page = random.randrange(1, 500, 1)
    return some_page


# Делаем фейковый книжный номер, по стандарту isbn13
def isbn13():
    from faker import Faker
    fake = Faker()
    return fake.isbn13()


# Делаем ранодомный рейтинг
def rating():
    some_rat = random.uniform(0.0, 5.0)
    return float('%.1f' % some_rat)


# Делаем ранодомную цену
def price():
    some_price = random.uniform(1.0, 1500.0)
    return float('%.1f' % some_price)


# Делаем фейкового автора книги
def author():
    from faker import Faker
    fake = Faker(locale="ru_RU")
    return fake.name()


if __name__ == "__main__":
    main()
