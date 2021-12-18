import random
BOOKS = "books.txt"


def var_from_conf():
    from conf import model
    print(model)

def title():
    with open(BOOKS, "r", encoding="utf-8") as f:
        a = []
        for list in f:
            a.append(list)
        z = random.choice(a)
        n = z.replace("\n", "")
        print(n)

def year():
    y = random.randrange(1990, 2021, 1)
    print(y)

def pages():
    y = random.randrange(1, 500, 1)
    print(y)

def isbn13():
    from faker import Faker
    fake = Faker()
    print(fake.isbn13())

def rating():
    y = random.uniform(0.0, 5.0)
    print('%.1f' % y)

def price():
    y = random.uniform(1.0, 1500.0)
    print('%.1f' % y)

def author():
    from faker import Faker
    fake = Faker(locale="ru_RU")
    print(fake.name())

if __name__ == "__main__":
    var_from_conf()
    title()
    year()
    pages()
    isbn13()
    rating()
    price()
    author()