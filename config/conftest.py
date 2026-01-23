import pytest 
from myapp.models import Product

@pytest.fixture 
def sample_product():
    return Product.objects.create(
        name = "Test Product",
        price = 100.00,
        in_stock = True
    )

@pytest.fixture
def create_product():
    def create_product(name = "create Product", price = 50):
        return Product.objects.create(name=name,price=price)
    return create_product