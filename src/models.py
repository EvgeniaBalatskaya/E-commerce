class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для получения цены продукта."""
        return self._price

    @price.setter
    def price(self, value: float):
        """Сеттер для установки цены продукта."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if value < self._price:
                user_input = input(
                    f"Вы хотите понизить цену с {self._price} до {value}? (y/n): "
                )
                if user_input.lower() == "y":
                    self._price = value
            else:
                self._price = value


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self._products = products  # Приватный атрибут

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        """Метод для добавления продукта в категорию."""
        self._products.append(product)  # Добавление через append
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для получения списка продуктов в строковом формате."""
        return (
            "\n".join(
                [
                    f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
                    for product in self._products
                ]
            )
            + "\n"
        )  # Добавляем символ новой строки в конец

    @classmethod
    def new_product(cls, product_data: dict):
        """Метод для создания нового продукта."""
        return Product(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )
