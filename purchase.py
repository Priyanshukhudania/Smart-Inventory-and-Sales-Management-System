from datetime import datetime


class Purchase:

    def __init__(self):

        self.purchase_history = []
        self.purchase_counter = 5001

    # ---------------------------------
    # Purchase Product from Supplier
    # ---------------------------------

    def purchase_product(self, supplier, inventory, product_id, quantity):

        product = inventory.products.get(product_id)

        if not product:
            print("Product Not Found.")
            return

        # Restock Inventory
        product.restock(quantity)

        # Supplier Purchase Order Increase
        supplier.add_purchase_order()

        purchase_id = self.purchase_counter

        total_cost = product.cost_price * quantity

        purchase = {

            "purchase_id": purchase_id,
            "supplier": supplier.company_name,
            "product": product.product_name,
            "quantity": quantity,
            "cost_price": product.cost_price,
            "total_cost": total_cost,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        }

        self.purchase_history.append(purchase)

        self.purchase_counter += 1

        print("\nPurchase Completed Successfully.")
        print(f"Purchase ID : {purchase_id}")

        return purchase

    # ---------------------------------
    # Display All Purchases
    # ---------------------------------

    def display_purchases(self):

        if len(self.purchase_history) == 0:

            print("No Purchase Records Found.")
            return

        print("\n========== PURCHASE HISTORY ==========\n")

        for purchase in self.purchase_history:

            print("-" * 60)

            print(f"Purchase ID : {purchase['purchase_id']}")
            print(f"Supplier    : {purchase['supplier']}")
            print(f"Product     : {purchase['product']}")
            print(f"Quantity    : {purchase['quantity']}")
            print(f"Cost Price  : ₹{purchase['cost_price']:.2f}")
            print(f"Total Cost  : ₹{purchase['total_cost']:.2f}")
            print(f"Date        : {purchase['date']}")

        print("-" * 60)

    # ---------------------------------
    # Search Purchase
    # ---------------------------------

    def search_purchase(self, purchase_id):

        for purchase in self.purchase_history:

            if purchase["purchase_id"] == purchase_id:

                print("\nPurchase Found\n")

                print("-" * 60)

                print(f"Purchase ID : {purchase['purchase_id']}")
                print(f"Supplier    : {purchase['supplier']}")
                print(f"Product     : {purchase['product']}")
                print(f"Quantity    : {purchase['quantity']}")
                print(f"Cost Price  : ₹{purchase['cost_price']:.2f}")
                print(f"Total Cost  : ₹{purchase['total_cost']:.2f}")
                print(f"Date        : {purchase['date']}")

                print("-" * 60)

                return purchase

        print("Purchase Record Not Found.")

    # ---------------------------------
    # Total Purchase Cost
    # ---------------------------------

    def total_purchase_cost(self):

        total = 0

        for purchase in self.purchase_history:

            total += purchase["total_cost"]

        print(f"\nTotal Purchase Cost : ₹{total:.2f}")

        return total

    # ---------------------------------
    # Purchase Summary
    # ---------------------------------

    def purchase_summary(self):

        print("\n========== PURCHASE SUMMARY ==========\n")

        print(f"Total Purchases : {len(self.purchase_history)}")

        self.total_purchase_cost()

    # ---------------------------------
    # Delete Purchase Record
    # ---------------------------------

    def delete_purchase(self, purchase_id):

        for purchase in self.purchase_history:

            if purchase["purchase_id"] == purchase_id:

                self.purchase_history.remove(purchase)

                print("Purchase Deleted Successfully.")

                return

        print("Purchase Not Found.")