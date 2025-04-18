class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

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
        for product in products:
            self.add_product(product)

    def __str__(self):
        return f"{self.name}: {self.description}"

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников."
            )
        self._products.append(product)
        Category.product_count += 1

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
