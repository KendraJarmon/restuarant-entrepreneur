from order import Pizza
from order import Pasta
from order import Salad
from order import Order





class Order_Factory:
    def create_order(type: str) -> Order: 
        if dish_name == "pizza":
            return Pizza(1)
        elif dish_name == "pasta":
            return Pasta(8)
        elif dish_name == "salad":
            return Salad(5)