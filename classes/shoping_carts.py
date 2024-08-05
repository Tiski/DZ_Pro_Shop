import sys
import os

# Добавляем путь к директории classes
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from classes.products import Product

class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """
    def __init__(self, customer_name, registered_by):
        self.items = []
        self.customer_name = customer_name
        self.registered_by = registered_by

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity})

    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total

    def get_details(self):
        """
        Возвращает детализированную информацию о содержимом корзины и общей стоимости.
        """
        details = f"Корзина покупок для {self.customer_name}:\n"
        for item in self.items:
            details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
        details += f"Общая стоимость: {self.get_total()} руб\n"
        details += f"Покупки зарегистрировал пользователь: {self.registered_by}"
        return details

# Пример использования класса ShoppingCart
if __name__ == "__main__":
    # Создаем продукты
    product1 = Product("Laptop", 1000)
    product2 = Product("Smartphone", 500)
    product3 = Product("Ariel", 70)

    # Создаем корзину покупок
    cart = ShoppingCart(customer_name="Иван Иванов", registered_by="админ")

    # Добавляем товары в корзину
    cart.add_item(product1, 1)
    cart.add_item(product2, 2)
    cart.add_item(product3, 1)

    # Выводим детализированную информацию о корзине
    print(cart.get_details())
