class Reports:

    def __init__(self):
        pass

    # -----------------------------------
    # Inventory Report
    # -----------------------------------

    def inventory_report(self, inventory):

        print("\n========== INVENTORY REPORT ==========")

        if len(inventory.products) == 0:
            print("Inventory is Empty.")
            return

        for product in inventory.products.values():

            print("-" * 60)

            print(f"ID        : {product.product_id}")
            print(f"Product   : {product.product_name}")
            print(f"Category  : {product.category}")
            print(f"Stock     : {product.quantity}")
            print(f"Status    : {product.stock_status()}")
            print(f"Value     : ₹{product.inventory_value():.2f}")

        print("-" * 60)

    # -----------------------------------
    # Low Stock Report
    # -----------------------------------

    def low_stock_report(self, inventory):

        print("\n========== LOW STOCK REPORT ==========")

        found = False

        for product in inventory.products.values():

            if product.is_low_stock():

                found = True

                print("-" * 50)

                print(f"{product.product_name}")
                print(f"Stock : {product.quantity}")

        if not found:
            print("No Low Stock Products.")

    # -----------------------------------
    # Customer Report
    # -----------------------------------

    def customer_report(self, customers):

        print("\n========== CUSTOMER REPORT ==========")

        if len(customers) == 0:

            print("No Customers Found.")

            return

        for customer in customers.values():

            customer.display()

    # -----------------------------------
    # Supplier Report
    # -----------------------------------

    def supplier_report(self, suppliers):

        print("\n========== SUPPLIER REPORT ==========")

        if len(suppliers) == 0:

            print("No Suppliers Found.")

            return

        for supplier in suppliers.values():

            supplier.display()

    # -----------------------------------
    # Sales Report
    # -----------------------------------

    def sales_report(self, sales):

        print("\n========== SALES REPORT ==========")

        sales.display_sales()

    # -----------------------------------
    # Purchase Report
    # -----------------------------------

    def purchase_report(self, purchase):

        print("\n========== PURCHASE REPORT ==========")

        purchase.display_purchases()

    # -----------------------------------
    # Profit Report
    # -----------------------------------

    def profit_report(self, sales):

        print("\n========== PROFIT REPORT ==========")

        profit = sales.total_profit()

        print(f"Overall Profit : ₹{profit}")

    # -----------------------------------
    # Inventory Value
    # -----------------------------------

    def inventory_value_report(self, inventory):

        print("\n========== INVENTORY VALUE ==========")

        total = 0

        for product in inventory.products.values():

            total += product.inventory_value()

        print(f"Total Inventory Value : ₹{total:.2f}")

    # -----------------------------------
    # Complete System Report
    # -----------------------------------

    def system_summary(self,
                       customers,
                       suppliers,
                       inventory,
                       sales,
                       purchase):

        print("\n")
        print("=" * 60)
        print("      SMART INVENTORY SYSTEM REPORT")
        print("=" * 60)

        print(f"Total Customers        : {len(customers)}")

        print(f"Total Suppliers        : {len(suppliers)}")

        print(f"Total Products         : {len(inventory.products)}")

        print(f"Total Sales            : {len(sales.sales_history)}")

        print(f"Total Purchases        : {len(purchase.purchase_history)}")

        inventory_value = 0

        for product in inventory.products.values():

            inventory_value += product.inventory_value()

        print(f"Inventory Value        : ₹{inventory_value:.2f}")

        print(f"Total Profit : ₹{sales.total_profit():.2f}")

        print("=" * 60)