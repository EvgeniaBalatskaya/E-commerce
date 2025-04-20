from src.models import Category, LawnGrass, Product, Smartphone

if __name__ == "__main__":
    # Создание базовых продуктов
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создание категории с базовыми продуктами
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Создание продуктов-наследников
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

    # Проверка строкового представления
    print("\n--- Смартфоны ---")
    print(smartphone1)
    print(smartphone2)
    print(smartphone3)

    print("\n--- Газонная трава ---")
    print(grass1)
    print(grass2)

    # Проверка сложения продуктов одного класса
    print("\n--- Сложение продуктов ---")
    print(smartphone1 + smartphone2)  # OK
    print(grass1 + grass2)  # OK

    # Проверка TypeError при сложении разных классов
    try:
        result = smartphone1 + grass1
    except TypeError:
        print("Ошибка: Нельзя складывать продукты разных типов.")

    # Создание и расширение категорий
    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
    )
    category_smartphones.add_product(smartphone3)

    category_grass = Category(
        "Газонная трава", "Различные виды газонной травы", [grass1, grass2]
    )

    print("\n--- Категория Смартфоны ---")
    print(category_smartphones)

    print("\n--- Категория Газонная трава ---")
    print(category_grass)

    # Проверка количества продуктов и категорий
    print("\n--- Статистика ---")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего продуктов: {Category.product_count}")

    # Проверка TypeError при добавлении не-продукта
    try:
        category_smartphones.add_product("Не продукт")
    except TypeError:
        print("Ошибка: Можно добавлять только объекты Product или его наследников.")
