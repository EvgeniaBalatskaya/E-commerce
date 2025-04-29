from abc import ABC, abstractmethod


class ZeroQuantityError(Exception):
    """Исключение для товаров с нулевым количеством."""

    pass


class LogMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs):
        msg = f"Создан объект {self.__class__.__name__} с параметрами: {args}, {kwargs}"
        print(msg)
        super().__init__(*args, **kwargs)

    def __repr__(self):
        attrs = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}({attrs})"


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float):
        pass


class Product(BaseProduct, LogMixin):
    """Класс продукта."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ZeroQuantityError(
                "Товар с нулевым количеством не может быть добавлен"
            )
        super().__init__(
            name=name, description=description, price=price, quantity=quantity
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("Нельзя складывать продукты разных типов.")
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self._price:
            user_input = input(f"Понизить цену с {self._price} до {value}? (y/n): ")
            if user_input.lower() == "y":
                self._price = value
        else:
            self._price = value


class Smartphone(Product):
    """Класс смартфона."""

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
            f"{self.name} ({self.model}, {self.memory}GB, {self.color}) - "
            f"{self.price} руб., {self.quantity} шт., эффективность: {self.efficiency}"
        )


class LawnGrass(Product):
    """Класс газонной травы."""

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
            f"{self.name} ({self.color}, {self.country}) - {self.price} руб., "
            f"{self.quantity} шт., всхожесть: {self.germination_period}"
        )


class Category:
    """Класс категории продуктов."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self._products: list[Product] = []
        Category.category_count += 1
        self.product_count = 0

        for product in products:
            try:
                self.add_product(product)
            except ZeroQuantityError as e:
                print(f"Ошибка при добавлении товара: {e}")
            else:
                print(f"Товар {product.name} успешно добавлен")
            finally:
                print("Обработка добавления товара завершена")

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return (
            f"{self.name}, {self.description}. "
            f"Количество продуктов: {total_quantity} шт."
        )

    def add_product(self, product):
        if not issubclass(type(product), Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников."
            )
        if product.quantity == 0:
            raise ZeroQuantityError("Нельзя добавить товар с нулевым количеством")
        self._products.append(product)
        self.product_count += 1
        Category.product_count += 1

    def middle_price(self):
        try:
            total = sum(product.price for product in self._products)
            return total / len(self._products)
        except ZeroDivisionError:
            return 0

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
