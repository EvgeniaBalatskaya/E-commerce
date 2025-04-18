from src.models import Category, Product

if __name__ == "__main__":
    # Создание продуктов
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Вывод данных о продуктах
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    # Создание категории с продуктами
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Проверка имени категории и вывод информации о категории
    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))  # Показываем количество товаров
    print(Category.category_count)
    print(Category.product_count)

    # Создание нового продукта и новой категории
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    # Вывод данных о второй категории
    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    # Строковое представление продуктов и категорий
    print("\nСтроковое представление продуктов:")
    print(str(product1))
    print(str(product2))
    print(str(product3))

    print("\nСтроковое представление категории:")
    print(str(category1))

    # Пример сложения продуктов
    print("\nРезультат сложения продуктов:")
    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
