from datetime import datetime

class Product:

    def __init__(self, product_id,product_name,category,cost_price,selling_price,quantity,supplier):

        self.product_id = product_id
        self.product_name = product_name.title()
        self.category = category.title()

        self.cost_price= float(cost_price)
        self.selling_price= float(selling_price)

        self.quantity = int(quantity)
        self.supplier = supplier


       #minimum stock feature
        self.minimum_stock = 5 

        self.created_at = datetime.now()
        




    def display(self):
        print("-"*70)

        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Category: {self.category}")
        print(f"Cost Price : ₹{self.cost_price:.2f}")
        print(f"Selling Price : ₹{self.selling_price:.2f}")
        print(f"Available Stock: {self.quantity}")
        print(f"Supplier: {self.supplier}")
        print(f"Minimum Stock : {self.minimum_stock}")
        print(f"Created On: {self.created_at.strftime('%d-%m-%Y %H:%M:%S')}")
        print("-"*70)


    def update_name(self,name):
        self.product_name = name.title()

    def update_category(self,category):
        self.category= category.title()


    def update_quantity(self, quantity):
        self.quantity = float(quantity)

    def update_cost_price(self,cost_price):
        self.cost_price = float(cost_price)

    def update_selling_price(self,selling_price):
        self.selling_price = float(selling_price)
    
    def update_supplier(self,supplier):
        self.supplier = supplier    
        
    def update_minimum_stock(self,minimum_stock):
        self.minimum_stock = int(minimum_stock)



    def restock(self,quantity):
        self.quantity += int(quantity)


    def sell_product(self, quantity):

        if quantity> self.quantity:

            print(f"Only {self.quantity} items available in Stock")
            return False

        self.quantity -= quantity
        return True

    def is_low_stock(self):

        return self.quantity <= self.minimum_stock
        # if product.is_low_stock():
        #     print("LOW STOCK ALERT")

    

    def calculate_profit(self):
        return self.selling_price - self.cost_price


    def inventory_value(self):
       return self.cost_price * self.quantity
    
    
    def stock_status(self):

        if self.quantity == 0:
          return "Out of Stock"

        elif self.quantity <= self.minimum_stock:
            return "Low Stock"

        return "In Stock"