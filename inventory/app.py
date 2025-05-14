# Inventory Management System

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    # methods
    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    # Setter methods
    def set_price(self, price):
        self.__price = price

    def set_quantity(self, quantity):
        self.__quantity = quantity

    # product info
    def display(self):
        print(f"ID: {self.__product_id}, Name: {self.__name}, Price: Rs.{self.__price}, Quantity: {self.__quantity}")


# Electronic product, inherits from Product
class Electronic(Product):
    def __init__(self, product_id, name, price, quantity, brand):
        super().__init__(product_id, name, price, quantity)
        self.__brand = brand

    def display(self):
        super().display()
        print(f"Brand: {self.__brand}")


# Inventory to manage products
class Inventory:
    def __init__(self):
        self.__products = {}

    def add_product(self, product):
        pid = product.get_id()
        if pid in self.__products:
            print("Product already exists. Updating quantity.")
            existing = self.__products[pid]
            new_quantity = existing.get_quantity() + product.get_quantity()
            existing.set_quantity(new_quantity)
        else:
            self.__products[pid] = product
        print("Product added/updated successfully.")

    def remove_product(self, product_id):
        if product_id in self.__products:
            del self.__products[product_id]
            print("Product removed successfully.")
        else:
            print("Product not found.")

    def update_quantity(self, product_id, quantity):
        product = self.__products.get(product_id)
        if product:
            product.set_quantity(quantity)
            print("Quantity updated.")
        else:
            print("Product not found.")

    def show_inventory(self):
        if not self.__products:
            print("Inventory is empty.")
            return
        print("\n=== Current Inventory ===")
        for product in self.__products.values():
            product.display()
            print("-" * 30)


# Main function
def main():
    inventory = Inventory()

    while True:
        print("\n===== Inventory Menu =====")
        print("1. Add Product")
        print("2. Add Electronic Product")
        print("3. Remove Product")
        print("4. Update Quantity")
        print("5. Show Inventory")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            try:
                pid = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                price = float(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))
                product = Product(pid, name, price, quantity)
                inventory.add_product(product)
            except ValueError:
                print("Invalid input. Please enter correct values.")

        elif choice == '2':
            try:
                pid = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                price = float(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))
                brand = input("Enter Brand: ")
                electronic = Electronic(pid, name, price, quantity, brand)
                inventory.add_product(electronic)
            except ValueError:
                print("Invalid input. Please enter correct values.")

        elif choice == '3':
            try:
                pid = int(input("Enter Product ID to remove: "))
                inventory.remove_product(pid)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '4':
            try:
                pid = int(input("Enter Product ID: "))
                quantity = int(input("Enter new quantity: "))
                inventory.update_quantity(pid, quantity)
            except ValueError:
                print("Invalid input. Please enter correct values.")

        elif choice == '5':
            inventory.show_inventory()

        elif choice == '6':
            print("Exiting Inventory System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option (1-6).")


if __name__ == "__main__":
    main()
