from src.models import (Category, LawnGrass, Product, Smartphone,
                        ZeroQuantityError)

if __name__ == "__main__":
    print("=== Тестирование создания продукта с нулевым количеством ===")
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ZeroQuantityError as e:
        print(f"Ошибка: {e}")
    else:
        print("Не возникла ошибка при попытке добавить продукт с нулевым количеством")

    print("\n=== Создание корректных продуктов ===")
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print("\n=== Создание категории и проверка среднего ценника ===")
    category1 = Category(
        "Смартфоны", "Категория смартфонов", [product1, product2, product3]
    )
    print(f"Средняя цена в категории: {category1.middle_price()}")

    print("\n=== Проверка пустой категории ===")
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(f"Средняя цена в пустой категории: {category_empty.middle_price()}")

    print("\n=== Проверка добавления товара с нулевым количеством в категорию ===")
    try:
        product_zero = Product("Тестовый", "Товар с нулевым количеством", 100.0, 0)
        category1.add_product(product_zero)
    except ZeroQuantityError as e:
        print(f"Ошибка при добавлении в категорию: {e}")

    print("\n=== Создание продуктов-наследников ===")
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )

    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )

    print("\n=== Проверка строкового представления ===")
    print("\n--- Смартфоны ---")
    print(smartphone1)
    print(smartphone2)
    print(smartphone3)

    print("\n--- Газонная трава ---")
    print(grass1)
    print(grass2)

    print("\n=== Проверка сложения продуктов одного класса ===")
    print("\n--- Сложение продуктов ---")
    print(smartphone1 + smartphone2)
    print(grass1 + grass2)

    print("\n=== Проверка TypeError при сложении разных классов ===")
    try:
        result = smartphone1 + grass1
    except TypeError as e:
        print(f"Ошибка: {e}")

    print("\n=== Создание и расширение категорий ===")
    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
    )
    category_smartphones.add_product(smartphone3)

    category_grass = Category(
        "Газонная трава", "Различные виды газонной травы", [grass1, grass2]
    )

    print("\n--- Категория Смартфоны ---")
    print(category_smartphones)
    print(f"Средняя цена: {category_smartphones.middle_price()}")

    print("\n--- Категория Газонная трава ---")
    print(category_grass)
    print(f"Средняя цена: {category_grass.middle_price()}")

    print("\n=== Проверка количества продуктов и категорий ===")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего продуктов: {Category.product_count}")

    print("\n=== Проверка TypeError при добавлении не-продукта ===")
    try:
        category_smartphones.add_product("Не продукт")
    except TypeError as e:
        print(f"Ошибка: {e}")
