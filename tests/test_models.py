import pytest

from src.models import Category, Product


def test_product_init():
    product = Product("Test", "Test desc", 100.0, 3)
    assert product.name == "Test"
    assert product.description == "Test desc"
    assert product.price == 100.0
    assert product.quantity == 3


def test_category_init():
    product1 = Product("A", "B", 10.0, 1)
    product2 = Product("C", "D", 20.0, 2)
    category = Category("Phones", "Desc", [product1, product2])
    assert category.name == "Phones"
    assert category.description == "Desc"
    assert category.products == [product1, product2]


def test_category_counters():
    # Обнуление счётчиков
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("P1", "D1", 100, 5)
    p2 = Product("P2", "D2", 200, 2)
    c1 = Category("Cat1", "Desc1", [p1])
    c2 = Category("Cat2", "Desc2", [p2])

    assert Category.category_count == 2
    assert Category.product_count == 2
