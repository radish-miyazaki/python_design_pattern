from abc import ABCMeta, abstractmethod


class PaymentStrategy(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, amount: int):
        pass


class CashPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int):
        print(f"クレジットカードで{amount}円の支払い")


class CreditCardPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int):
        print(f"現金で{amount}円の支払い")


class ShoppingCard:
    def __init__(self):
        self.__items = []
        self.__total = 0

    def add_item(self, item: str, price: int):
        self.__total += price
        self.__items.append((item, price))

    def pay(self, payment_strategy: PaymentStrategy):
        payment_strategy.pay(self.__total)


if __name__ == "__main__":
    cart = ShoppingCard()
    cart.add_item("item1", 500)
    cart.add_item("item2", 1000)

    payment_strategy1 = CreditCardPaymentStrategy()
    cart.pay(payment_strategy1)
    payment_strategy2 = CashPaymentStrategy()
    cart.pay(payment_strategy2)
