class Invoice:
    def send_invoice(self, name: str):
        print(f"{name} の請求書が送信されました")


class Payment:
    def make_payment(self, name: str):
        print(f"{name} の支払いが完了しました")


class Product:
    def get_product(self, name: str):
        print(f"{name} を取得しました")


class Order:
    def place_order(self, name: str):
        print("注文開始")
        product = Product()
        product.get_product(name)

        payment = Payment()
        payment.make_payment(name)

        invoice = Invoice()
        invoice.send_invoice(name)
        print("注文が正常に完了しました")


if __name__ == '__main__':
    order = Order()
    order.place_order("Gof Design Patterns")
