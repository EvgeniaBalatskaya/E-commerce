class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(
            other, type(self)
        ):  # используем isinstance для проверки типов
            raise TypeError("Нельзя складывать продукты разных типов.")
        if not isinstance(other, Product):
            return NotImplemented
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if value < self.__price:
                user_input = input(
                    f"Вы хотите понизить цену с {self.__price} до {value}? (y/n): "
                )
                if user_input.lower() == "y":
                    self.__price = value
            else:
                self.__price = value


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self._products: list[Product] = []
        Category.category_count += 1
        self.product_count = 0  # Инициализация счётчика продуктов для этой категории

        # Добавляем продукты с помощью метода add_product
        for product in products:
            self.add_product(product)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, {self.description}. Количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников."
            )
        self._products.append(product)
        self.product_count += 1  # Увеличиваем счётчик продуктов в категории

    @property
    def products(self):
        return "\n".join(str(product) for product in self._products) + "\n"

    @classmethod
    def new_product(cls, product_data: dict):
        return Product(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )


# Новый класс-наследник: Смартфоны
class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (
            f"{self.name} ({self.model}, {self.memory}GB, {self.color}) — "
            f"{self.price} руб., {self.quantity} шт., эффективность: {self.efficiency}"
        )


# Новый класс-наследник: Газонная трава
class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (
            f"{self.name} ({self.color}, {self.country}) — {self.price} руб., "
            f"{self.quantity} шт., всхожесть: {self.germination_period}"
        )
