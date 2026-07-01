from datetime import datetime

class Customer:

    def __init__(self,customer_id,name,phone,email,address):
        self.customer_id = customer_id
        self.name = name.title()
        self.phone = phone
        self.email = email.lower()
        self.address = address.title()
        self.purchase_history = []  # the purchase history of the customer
        self.created_at = datetime.now()

# Display Function - for displaying customer info
    def display(self):
        print("-"*70)
        print(f'Customer ID: {self.customer_id}')
        print(f'Customer Name: {self.name}')
        print(f'phone: {self.phone}')
        print(f' Email: {self.email}')
        print(f'Address: {self.address}')
        print(f'Order Placed: {len(self.purchase_history)}')
        print(f"Registered ON: {self.created_at.strftime('%d-%m-%Y %H:%M:%S')}")
        print("-"*70)

 #updating the customer info
    def update_name(self,name):
        self.name = name.title()
    def update_phone(self, phone):
        self.phone = phone
    def update_email(self,email):
        self.email = email.lower()
    def update_address(self,address):
        self.address = address.title()             
    
    #Purchase History of the customer
    def add_purchase(self,invoice_no,product_name,quantity,total_amount):
        purchase = {
            "invoice": invoice_no,
            "product": product_name,
            "quantity": quantity,
            "amount": total_amount,
            "date": datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        }
        self.purchase_history.append(purchase)
    
    def view_purchase_history(self):
        print(f'\nPurchase History of {self.name}')
        print('-'*70)

        if len(self.purchase_history) == 0:
            print("no purchase forund!")
            return 
        for index, purchase in enumerate(self.purchase_history,start=1):
            print(f'\nPurchase{index}')
            print(f'\ninvoice: {purchase['invoice']}')
            print(f'Product: {purchase["product"]}')
            print(f'Quantity: {purchase["quantity"]}')
            print(f'amount (in rupees): {purchase["amount"]:.2f}')
            print(f'date: {purchase["date"]}')
        
        print("-"*70)

        # customer stats . total orders, total_amount spent
    def customer_stats(self):
        total_orders = len(self.purchase_history)

        total_amount = 0

        for purchase in self.purchase_history:
            total_amount += purchase["amount"]

        print("\n Customer Statistics")
        print("-"*70)

        print(f"Total Orders:{total_orders}")
        print(f"Total Amount Spent:{total_amount:.2f}")

    def search_invoice(self, invoice_no):


        for purchase in self.purchase_history:
          
          if purchase["invoice"] == invoice_no:

            print("Invoice Found")
            print(purchase)
            return
        
        print("Invoice Not Found")
        