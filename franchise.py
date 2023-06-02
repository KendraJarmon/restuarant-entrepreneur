from order_factory import Order_Factory
from logger import logger

class Franchise:

    def __init__(self, store_number) -> None:
        self.name = "Kennie's Pizzaria"
        self.store_number = int(store_number)

    def place_order(self):
        print(f"Hello pizza lovers and welcome to {self.name}, location #{self.store_number}!")
        order = input("What would you be having today? Pizza, Pasta, or a salad? > ")
        ordered = Order_Factory.create_order(order)
        logger.log_transaction(ordered, self.store_number)
