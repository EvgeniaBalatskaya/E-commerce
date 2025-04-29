import pytest

from src.models import (BaseProduct, Category, LawnGrass, LogMixin, Product,
                        Smartphone, ZeroQuantityError)


def test_product_str():
    product = Product("Test", "Desc", 100.0, 2)
    assert str(product) == "Test, 100.0 руб. Остаток: 2 шт."


def test_product_add():
    p1 = Product("P1", "D", 100.0, 2)
    p2 = Product("P2", "D", 50.0, 4)
    assert p1 + p2 == 100.0 * 2 + 50.0 * 4


def test_product_add_invalid_type():
    p1 = Product("P1", "D", 100.0, 2)
    with pytest.raises(TypeError):
        _ = p1 + "string"


def test_product_price_setter():
    p = Product("Test", "D", 100.0, 1)
    p.price = 200.0
    assert p.price == 200.0


def test_product_price_negative(capsys):
    p = Product("Test", "D", 100.0, 1)
    p.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_category_add_product():
    p = Product("P", "D", 100.0, 1)
    c = Category("C", "Desc", [])
    c.add_product(p)
    assert p in c._products


def test_category_str():
    p = Product("P", "D", 100.0, 2)
    c = Category("Cat", "Description", [p])
    assert str(c) == "Cat, Description. Количество продуктов: 2 шт."


def test_category_add_invalid():
    c = Category("Cat", "Desc", [])
    with pytest.raises(TypeError):
        c.add_product("not product")


def test_smartphone_inheritance():
    s = Smartphone("Phone", "Desc", 100.0, 2, 95.5, "Model X", 128, "Black")
    assert isinstance(s, Product)
    assert s.model == "Model X"
    assert s.memory == 128


def test_lawngrass_inheritance():
    g = LawnGrass("Grass", "Desc", 50.0, 10, "Россия", "7 дней", "Зеленый")
    assert isinstance(g, Product)
    assert g.country == "Россия"
    assert g.color == "Зеленый"


def test_product_add_different_classes():
    s = Smartphone("Phone", "Desc", 100.0, 1, 90.0, "X", 128, "Black")
    g = LawnGrass("Grass", "Desc", 50.0, 1, "Россия", "7 дней", "Зелёный")
    with pytest.raises(TypeError):
        _ = s + g


def test_smartphone_str():
    s = Smartphone("Phone", "Desc", 100.0, 1, 90.0, "X", 128, "Black")
    expected = "Phone (X, 128GB, Black) - 100.0 руб., 1 шт., эффективность: 90.0"
    assert str(s) == expected


def test_lawngrass_str():
    g = LawnGrass("Grass", "Desc", 50.0, 2, "Россия", "7 дней", "Зеленый")
    expected = "Grass (Зеленый, Россия) - 50.0 руб., 2 шт., всхожесть: 7 дней"
    assert str(g) == expected


def test_category_and_product_counts():
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("P1", "Desc", 100.0, 1)
    p2 = Smartphone("P2", "Desc", 150.0, 2, 91.0, "M2", 64, "Blue")
    c = Category("Test", "Testing", [p1, p2])
    assert Category.category_count == 1
    assert c.product_count == 2
    assert Category.product_count == 2


def test_category_add_only_products():
    c = Category("Test", "Test", [])
    with pytest.raises(TypeError):
        c.add_product("not a product")
    with pytest.raises(TypeError):
        c.add_product(123)
    with pytest.raises(TypeError):
        c.add_product([])


def test_add_same_class_products():
    s1 = Smartphone("S1", "D", 100.0, 1, 90.0, "X", 64, "Black")
    s2 = Smartphone("S2", "D", 200.0, 2, 95.0, "Y", 128, "White")
    assert s1 + s2 == 100.0 * 1 + 200.0 * 2

    g1 = LawnGrass("G1", "D", 50.0, 3, "US", "5 дней", "Green")
    g2 = LawnGrass("G2", "D", 70.0, 4, "UK", "7 дней", "Blue")
    assert g1 + g2 == 50.0 * 3 + 70.0 * 4


def test_base_product_abstract():
    with pytest.raises(TypeError):
        BaseProduct("Test", "Desc", 100.0, 1)


def test_log_mixin_repr():
    class TestClass(LogMixin):
        def __init__(self, a, b):
            super().__init__()
            self.a = a
            self.b = b

    obj = TestClass(1, 2)
    assert repr(obj) == "TestClass(a=1, b=2)"


def test_product_inherits_base_product():
    p = Product("Test", "Desc", 100.0, 1)
    assert isinstance(p, BaseProduct)


def test_zero_quantity_product():
    with pytest.raises(ZeroQuantityError):
        Product("Test", "Desc", 100.0, 0)


def test_category_middle_price():
    p1 = Product("P1", "D", 100.0, 2)
    p2 = Product("P2", "D", 200.0, 3)
    c = Category("Test", "Test", [p1, p2])
    assert c.middle_price() == 150.0


def test_empty_category_middle_price():
    c = Category("Test", "Test", [])
    assert c.middle_price() == 0


def test_zero_quantity_add_to_category():
    c = Category("Test", "Test", [])
    with pytest.raises(ZeroQuantityError):
        p = Product("P", "D", 100.0, 0)
        c.add_product(p)


def test_category_add_product_with_zero_quantity():
    p = Product("P", "D", 100.0, 1)
    c = Category("Test", "Test", [p])
    with pytest.raises(ZeroQuantityError):
        c.add_product(Product("P2", "D2", 200.0, 0))
