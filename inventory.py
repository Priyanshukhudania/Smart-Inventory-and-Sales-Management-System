from product import Product

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self,product):
        
        if product.product_id in self.products:
            print("Product alresady exisit.")
            return
        self.products[product.product_id] = product
        print("Product added successfully.")


    def remove_product(self,product_id):
        if product_id in self.products:

            del self.products[product_id]

            print("Product removed successfully.")
        
        else:
            print("product not found.")

    
    def search_product(self,product_id):

        product = self.products.get(product_id)

        if product:
            product.display()
        else:
            print("Product not found.")


    def display_products(self):

        if not self.products:
            print("Inventory is empty.")
            return

        for product in self.products.values():

            product.display()
        

    def restock_product(self,product_id,quantity):
        product = self.products.get(product_id)
        if product:
            product.restock(quantity)  
            print("stock Updated.")
        else:
            print("Product Not Found.")



    def low_stock_product(self):

        found = False
        for product in self.products.values():

            if product.is_low_stock():
                product.display()
                found = True
        if not found:
            print("No low stock product.")

    def total_inventory_value(self):
        total =0
        for product in self.products.values():
            total+= product.inventory_value()

        print(total)


    def inventory_summary(self):

        print("\nInventory Summary")
        print("-"*50)

        print(f"Total Products : {len(self.products)}")

        self.total_inventory_value()