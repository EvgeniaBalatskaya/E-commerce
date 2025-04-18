from unittest.mock import patch

from src.models import Category, Product


# Тесты для Product
def test_product_init():
    product = Product("Test Product", "Test description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_price_setter():
    product = Product("Test Product", "Test description", 100.0, 10)

    # Проверка, что нельзя установить отрицательную цену
    with patch("builtins.print") as mocked_print:
        product.price = -10
        mocked_print.assert_called_once_with(
            "Цена не должна быть нулевая или отрицательная"
        )

    # Проверка понижения цены
    with patch("builtins.input", return_value="y"):
        product.price = 90.0
        assert product.price == 90.0

    # Проверка повышения цены
    product.price = 120.0
    assert product.price == 120.0


# Тесты для Category
def test_category_init():
    product1 = Product("Product1", "Description1", 10.0, 5)
    product2 = Product("Product2", "Description2", 20.0, 3)
    category = Category("Category1", "Category Description", [product1, product2])

    assert category.name == "Category1"
    assert category.description == "Category Description"
    assert len(category._products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_add_product():
    # Обнуление счетчика продуктов
    Category.product_count = 0

    product1 = Product("Product1", "Description1", 10.0, 5)
    product2 = Product("Product2", "Description2", 20.0, 3)
    category = Category("Category1", "Category Description", [product1])

    category.add_product(product2)

    # Проверка, что количество продуктов в категории увеличилось
    assert len(category._products) == 2
    assert (
        Category.product_count == 2
    )  # Считаем, что на старте было 1 продукт, и добавлен второй


def test_category_products():
    product1 = Product("Product1", "Description1", 10.0, 5)
    product2 = Product("Product2", "Description2", 20.0, 3)
    category = Category("Category1", "Category Description", [product1, product2])

    expected_str = (
        "Product1, 10.0 руб. Остаток: 5 шт.\n" "Product2, 20.0 руб. Остаток: 3 шт.\n"
    )
    assert category.products == expected_str


def new_product(product_data: dict):
    return Product(
        product_data["name"],
        product_data["description"],
        product_data["price"],
        product_data["quantity"],
    )
