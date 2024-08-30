# Product Store
# Write a class Product that has three attributes:
# type
# name
# price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
# Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement
# additional classes to operate on a certain type of product, etc.
# Also, the ProductStore class must have the following methods:
# add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your
# store(30 percent)
# set_discount(identifier, percent, identifier_type='name') - adds a discount for all products specified by input
# identifiers (type or name). The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other
# case raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.

class Product:
    def __init__(self, product_type: str, name: str, price: float) -> None:
        self.product_type = product_type
        self.name = name
        self.price = price


class ProductInStore(Product):
    def __init__(self, product_type: str, name: str, price: float, amount: int) -> None:
        super().__init__(product_type, name, price)
        self.amount = amount
        self.price_in_store = price * 1.3
        self.discount = 0

    def is_match(self, identifier: str, identifier_type: str) -> bool:
        if identifier_type == "name":
            return self.name == identifier
        else:
            return self.product_type == identifier

    def get_discount_price(self) -> float:
        return self.price_in_store * (1 - self.discount / 100)


class ProductStore:
    def __init__(self) -> None:
        self.products = {}
        self.income = 0.0

    def add(self, product: Product, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Amount must be a positive integer.")
        if product.name in self.products:
            self.products[product.name].amount += amount
        else:
            self.products[product.name] = ProductInStore(product.product_type, product.name, product.price, amount)

    def set_discount(self, identifier: str, percent: int, identifier_type: str = 'name') -> None:
        if identifier_type not in ['name', 'type']:
            raise ValueError("Invalid identifier_type. Use 'name' or 'type'.")

        if not (0 <= percent <= 100):
            raise ValueError("Discount percent must be between 0 and 100.")

        discount_applied = False
        for product in self.products.values():
            if product.is_match(identifier, identifier_type):
                product.discount = percent
                discount_applied = True

        if not discount_applied:
            raise ValueError(f"No products found for the given identifier: {identifier}")

    def sell_product(self, product_name: str, amount: int):
        if product_name not in self.products:
            raise ValueError(f"Product {product_name} not found in the store.")

        product = self.products[product_name]

        if product.amount < amount:
            raise ValueError(f"Not enough {product_name} in stock. Available: {product.amount}")

        self.income += product.get_discount_price() * amount
        product.amount -= amount

    def get_income(self) -> float:
        return self.income

    def get_all_products(self) -> list:
        return [(product.name, product.amount) for product in self.products.values()]

    def get_product_info(self, product_name: str) -> tuple:
        if product_name not in self.products:
            raise ValueError(f"Product {product_name} not found in the store.")

        product = self.products[product_name]
        return (product.name, product.amount)


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product("Food", "Ramen", 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.set_discount("Food", 10, "type")
s.sell_product("Ramen", 10)
print(s.get_all_products())
print(s.get_product_info("Ramen"))
print(s.get_income())

assert s.get_product_info("Ramen") == ("Ramen", 290)
assert s.get_income() == 17.55
