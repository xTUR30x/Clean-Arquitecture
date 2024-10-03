#Facade Pattern

class PaymentSystem:
    def make_payment(self, amount: int) -> None:
        print(f"Processing Payment { amount }")

class InventorySystem:
    def check_inventory(self, product:str ) -> None:
        print(f"Verifiying stock: { product }")

class DeliverySystem:
    def deliver_product(self, direction: str) -> None:
        print(f"Delivered in: { direction }")

class FacadeShop:
    def __init__(self) -> None:
        self.payment_system = PaymentSystem()
        self.inventory_system = InventorySystem()
        self.delivery_system = DeliverySystem()

    def order_prodcut(self, product: str, amount:int, direction: str) -> None:
        self.payment_system.make_payment(amount)
        self.inventory_system.check_inventory(product)
        self.delivery_system.deliver_product(direction)


if __name__ == '__main__':
    shop = FacadeShop()
    shop.order_prodcut("Book", 30, "Fake Street 123")