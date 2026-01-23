import pytest 
from myapp.models import Product

# тест 1 проверяем создание продукта 
@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(
        name = "Book",
        price = 100.00,
        in_stock = True
    )
    assert product.name == "Book"
    assert product.price == 100.00
    assert product.in_stock == True
    
#Тест  2 проверяем строковое представление
@pytest.mark.django_db
def test_product_str():
    product = Product.objects.create(
        name = "IPhone",
        price = 100
    )
    assert str(product) == 'IPhone'

# тест 3 Использование фикстуры
@pytest.mark.django_db
def test_with_fixture(create_product):
    product = create_product(
        name = "Fixture Product",
        price = 899
    )
    assert product.name == "Fixture Product"
    assert product.price == 899

# тест 4 запросы и фильтрация 
@pytest.mark.django_db
def test_filter_by_price():
    Product.objects.create(name="Банан",price = 69)
    Product.objects.create(name="Картошка",price = 101)
    Product.objects.create(name="Киви",price = 5000)
    #фильтруем дороогие товары
    expansive = Product.objects.filter(price__gt = 100)
    assert expansive.count() == 2

    #фильтруем дешевые товары
    cheap = Product.objects.filter(price__lt = 100)
    assert cheap.count() == 1

# Тест 5 обновление и сохранение записи
@pytest.mark.django_db
def test_update_product():
    product = Product.objects.create(
        name = 'Апельсины',
        price = 1200
    )
    product.name = "Голд апельсины"
    assert product.name == "Голд апельсины"

#тест 6 на удаление данных
@pytest.mark.django_db
def test_delete_product():
    product = Product.objects.create(
        name = "Чизбургер",
        price = 92
    )
    product_id = product.id
    product.delete()

    #проверяем что запись удалена

    assert Product.objects.filter(id=product_id).count() == 0