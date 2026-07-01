from datetime import datetime
class Supplier:

    def __init__(self,supplier_id,company_name,phone , email, address):

        self.supplier_id = supplier_id
        self.company_name = company_name.title()
        self.phone = phone
        self.email = email
        self.address = address.title()

        self.products_supplied= []
        self.total_orders = 0
        self.created_at = datetime.now()

    def display(self):

        print("-"*70)

        print(f"Supplier ID : {self.supplier_id}")
        print(f"Company name : {self.company_name}")
        print(f"Phone : {self.phone}")
        print(f"Email : {self.email}")
        print(f"Address : {self.address}")
        print(f"Product Supplied : {self.products_supplied}")
        print(f"Purchase Orders : {self.total_orders}")
        print(f"Registered On : {self.created_at.strftime('%d-%m-%Y %H:%M:%S')}")

        print("-"*70)
        
    def update_company_name(self, name):
         self.company_name = name.title()


    def update_phone(self, phone):
      self.phone = phone


    def update_email(self, email):
       self.email = email.lower()


    def update_address(self, address):
       self.address = address.title()
    
    def add_product(self, product_id):
      
      if product_id not in self.products_supplied:
        self.products_supplied.append(product_id)


    def view_products(self):
        print(f"\nProducts supplied by {self.company_name}")

        if not self.products_supplied:
         print("No products assigned.")
         return

        for index, product in enumerate(self.products_supplied, start=1):
         print(f"{index}. {product}")
    
    def add_purchase_order(self):

       self.total_orders += 1



    def supplier_stats(self):

        print("\nSupplier Statistics")
        print("-"*50)

        print(f"Products Supplied : {len(self.products_supplied)}")
        print(f"Purchase Orders   : {self.total_orders}")


    def remove_product(self, product_id):

        if product_id in self.products_supplied:
          self.products_supplied.remove(product_id)
          print("Product removed successfully.")

        else:
          print("Product not found.")

    def search_product(self, product_id):

        if product_id in self.products_supplied:
          print("Product Found")

        else:
          print("Product Not Found")