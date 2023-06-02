class Logger:

    def _init_(self) -> None:
        self.transaction_count = 0
        self.daily_sales = 0
        
    def log_transaction(self, order, store_number):
        self.transaction_count +=1
        self.daily_sales += order.price
        file = open("log.txt", "a")
        file.write(f"\n Order #{self.transaction_count}: {order.dish_name}: at location #{store_number} - ${order.price}; Total: ${self.daily_sales}\n")
        file.close()

logger = Logger