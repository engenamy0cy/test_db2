import pytest 
from test_cnfg.models import Book, Author

@pytest.fixture
def author():
    return Author.objects.create(
        name="Тестовый Автор"
    )

@pytest.fixture
def book(author):
    return Book.objects.create(
        title = "горе от ума",
        author=author
    )


@pytest.fixture
def multiple_author():
    authors = []
    for i in range(10):
        author = Author.objects.create(name=f"Автор {i}")
        authors.append(author)
    return authors

@pytest.fixture
def author_this_books():
    author = Author.objects.create(name="Шухрат")
    for i in range(10):
        Book.objects.create(title=f"Книга {i}",author=author)
    return author