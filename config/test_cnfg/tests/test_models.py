import pytest 
from test_cnfg.models import Author,Book
# Тест с использованием фикстуры для автора и для книги 
# тест без фикстуры
# тест с несколькими авторами
# - параметризирование тест 
# - тест на удаление Cascade 
# тест связанных запросов ( тестируем ForgenKey)
@pytest.mark.django_db
def test_author_fixture(author):
    assert author.name == "Тестовый Автор"
    assert Author.objects.count() == 1
@pytest.mark.django_db
def test_book_fixture(book,author):
    assert book.title == "горе от ума"
    assert book.author == author
    assert Book.objects.count() == 1

@pytest.mark.django_db
def test_multiple_author(multiple_author):
    
    assert len(multiple_author) == 10
    assert Author.objects.count()==10