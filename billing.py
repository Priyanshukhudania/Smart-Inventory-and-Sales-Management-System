from datetime import datetime


class Billing:

    def __init__(self):

        self.gst_percentage = 18
        self.discount_percentage = 0

    # -----------------------------------------
    # Set Discount
    # -----------------------------------------

    def set_discount(self, discount):

        self.discount_percentage = discount

    # -----------------------------------------
    # Generate Invoice
    # -----------------------------------------

    def generate_invoice(self, sale):

        subtotal = sale["amount"]

        discount_amount = (subtotal * self.discount_percentage) / 100

        amount_after_discount = subtotal - discount_amount

        gst_amount = (amount_after_discount * self.gst_percentage) / 100

        final_amount = amount_after_discount + gst_amount

        print("\n")
        print("=" * 60)
        print("             SMART INVENTORY SYSTEM")
        print("                  SALES INVOICE")
        print("=" * 60)

        print(f"Invoice No     : {sale['invoice']}")
        print(f"Date           : {sale['date']}")

        print("-" * 60)

        print(f"Customer       : {sale['customer']}")
        print(f"Product        : {sale['product']}")
        print(f"Quantity       : {sale['quantity']}")

        unit_price = subtotal / sale["quantity"]

        print(f"Unit Price     : ₹{unit_price:.2f}")

        print("-" * 60)

        print(f"Subtotal       : ₹{subtotal:.2f}")
        print(f"Discount ({self.discount_percentage}%) : -₹{discount_amount:.2f}")
        print(f"GST ({self.gst_percentage}%)      : +₹{gst_amount:.2f}")

        print("-" * 60)

        print(f"Final Amount   : ₹{final_amount:.2f}")

        print("=" * 60)

        print("       Thank You For Shopping!")

        print("=" * 60)

    # -----------------------------------------
    # Save Invoice
    # -----------------------------------------

    def save_invoice(self, sale):

        filename = f"Invoice_{sale['invoice']}.txt"

        subtotal = sale["amount"]

        discount_amount = (subtotal * self.discount_percentage) / 100

        amount_after_discount = subtotal - discount_amount

        gst_amount = (amount_after_discount * self.gst_percentage) / 100

        final_amount = amount_after_discount + gst_amount

        with open(filename, "w") as file:

            file.write("=" * 60 + "\n")
            file.write("SMART INVENTORY SYSTEM\n")
            file.write("SALES INVOICE\n")
            file.write("=" * 60 + "\n\n")

            file.write(f"Invoice No : {sale['invoice']}\n")
            file.write(f"Date       : {sale['date']}\n\n")

            file.write(f"Customer   : {sale['customer']}\n")
            file.write(f"Product    : {sale['product']}\n")
            file.write(f"Quantity   : {sale['quantity']}\n\n")

            file.write(f"Subtotal   : ₹{subtotal:.2f}\n")
            file.write(f"Discount   : ₹{discount_amount:.2f}\n")
            file.write(f"GST        : ₹{gst_amount:.2f}\n")
            file.write(f"Final Bill : ₹{final_amount:.2f}\n")

            file.write("\n")
            file.write("Thank You For Shopping!")

        print(f"\nInvoice Saved Successfully as {filename}")

    # -----------------------------------------
    # Change GST
    # -----------------------------------------

    def update_gst(self, gst):

        self.gst_percentage = gst

        print("GST Updated Successfully.")

    # -----------------------------------------
    # Display Current Settings
    # -----------------------------------------

    def billing_settings(self):

        print("\nBilling Settings")

        print("-" * 40)

        print(f"GST Percentage      : {self.gst_percentage}%")
        print(f"Discount Percentage : {self.discount_percentage}%")