from order import Order

class Pasta(Order):
    def __init__(self, dish_name: str, price: int) -> None:
        super().__init__(dish_name, price)