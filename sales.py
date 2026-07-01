from datetime import datetime
class Sales:

    def __init__(self):
        
        self.sales_history =[]
        self.invoice_counter = 1111

    # def inventory_summary(self):


    def make_sale(self, customer, inventory, product_id, quantity):

        product = inventory.products.get(product_id)

        if not product:
            print("Product not Found.")
            return
        
        if quantity > product.quantity:
            print("Insufficient Product.")
            return
        
        product.sell_product(quantity)


        total_amount = product.selling_price * quantity
        profit = product.calculate_profit()*quantity
        
        invoice_no = self.invoice_counter

        customer.add_purchase( invoice_no ,product.product_name,quantity,total_amount)
        sale = {


            "invoice": invoice_no,

            "customer": customer.name,

            "product": product.product_name,

            "quantity": quantity,

            "amount": total_amount,

            "profit": profit,

            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
        self.sales_history.append(sale)

        self.invoice_counter += 1

        print("Sale Completed Successfully.")

        return sale
            

    def display_sales(self):

        print("\nSales History")
        print("-" * 70)

        if len(self.sales_history) == 0:
            print("No Sales Found.")
            return

        for index, sale in enumerate(self.sales_history, start=1):

            print(f"\nSale {index}")
            print(f"Invoice : {sale['invoice']}")
            print(f"Customer : {sale['customer']}")
            print(f"Product : {sale['product']}")
            print(f"Quantity : {sale['quantity']}")
            print(f"Amount : ₹{sale['amount']:.2f}")
            print(f"Profit : ₹{sale['profit']:.2f}")
            print(f"Date : {sale['date']}")

        print("-" * 70)



    def search_invoice(self, invoice_no):

        for sale in self.sales_history:

            if sale["invoice"] == invoice_no:

                print("\nInvoice Found")
                print("-" * 50)

                print(f"Invoice : {sale['invoice']}")
                print(f"Customer : {sale['customer']}")
                print(f"Product : {sale['product']}")
                print(f"Quantity : {sale['quantity']}")
                print(f"Amount : ₹{sale['amount']:.2f}")
                print(f"Profit : ₹{sale['profit']:.2f}")
                print(f"Date : {sale['date']}")

                return sale

        print("Invoice Not Found.")



    def total_sales(self):

        total = 0

        for sale in self.sales_history:

            total += sale["amount"]

        print(f"Total Sales : ₹{total:.2f}")

        return total
    
    def total_profit(self):
        profit = 0

        for sale in self.sales_history:
             profit += sale.get("profit", 0)

        # 
        return profit


    def sales_summary(self):

        print("\nSales Summary")
        print("-" * 50)

        print(f"Total Invoices : {len(self.sales_history)}")

        self.total_sales()

        print(f"Total Profit : ₹{self.total_profit():.2f}")
        #  self.total_profit()

        print("-" * 50)