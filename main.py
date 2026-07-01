# ==============================
# Smart Inventory Management System
# main.py
# ==============================

from authentication import Authentication
from customer import Customer
from supplier import Supplier
from product import Product
from inventory import Inventory
from sales import Sales
from purchase import Purchase
from billing import Billing
from reports import Reports


# ===========================
# OBJECTS
# ===========================

auth = Authentication()

inventory = Inventory()

sales_manager = Sales()

purchase_manager = Purchase()

billing = Billing()

reports = Reports()


customers = {}

suppliers = {}


# ===========================
# LOGIN
# ===========================

if not auth.login():
    exit()


# ===========================
# MAIN MENU
# ===========================

while True:

    print("\n")
    print("=" * 60)
    print(" SMART INVENTORY & SALES MANAGEMENT SYSTEM ")
    print("=" * 60)

    print("1. Customer Management")

    print("2. Supplier Management")

    print("3. Product Management")

    print("4. Inventory Management")

    print("5. Purchase Management")

    print("6. Sales Management")

    print("7. Billing")

    print("8. Reports")

    print("9. Authentication")

    print("10. Exit")

    choice = input("\nEnter Choice : ")

# =====================================================
# CUSTOMER MANAGEMENT
# =====================================================

    if choice == "1":

        while True:

            print("\n")
            print("========== CUSTOMER MENU ==========")

            print("1 Add Customer")

            print("2 Display Customers")

            print("3 Search Customer")

            print("4 Customer Statistics")

            print("5 Back")

            ch = input("Enter Choice : ")

            if ch == "1":

                customer_id = input("Customer ID : ")

                name = input("Name : ")

                phone = input("Phone : ")

                email = input("Email : ")

                address = input("Address : ")

                customer = Customer(
                    customer_id,
                    name,
                    phone,
                    email,
                    address
                )

                customers[customer_id] = customer

                print("Customer Added Successfully.")

            elif ch == "2":

                if len(customers) == 0:

                    print("No Customers Found.")

                else:

                    for customer in customers.values():

                        customer.display()

            elif ch == "3":

                customer_id = input("Enter Customer ID : ")

                customer = customers.get(customer_id)

                if customer:

                    customer.display()

                else:

                    print("Customer Not Found.")

            elif ch == "4":

                customer_id = input("Customer ID : ")

                customer = customers.get(customer_id)

                if customer:

                    customer.customer_stats()

                else:

                    print("Customer Not Found.")

            elif ch == "5":

                break

            else:

                print("Invalid Choice")


# =====================================================
# SUPPLIER MANAGEMENT
# =====================================================

    elif choice == "2":

        while True:

            print("\n========= SUPPLIER MENU =========")

            print("1. Add Supplier")
            print("2. Display Suppliers")
            print("3. Search Supplier")
            print("4. Supplier Statistics")
            print("5. Back")

            ch = input("Enter Choice : ")

            if ch == "1":

                supplier_id = input("Supplier ID : ")
                company_name = input("Company Name : ")
                phone = input("Phone : ")
                email = input("Email : ")
                address = input("Address : ")

                sup = Supplier(
                    supplier_id,
                    company_name,
                    phone,
                    email,
                    address
                )

                suppliers[supplier_id] = sup

                print("Supplier Added Successfully.")

            elif ch == "2":

                if not suppliers:

                    print("No Suppliers Found.")

                else:

                    for sup in suppliers.values():

                        sup.display()

            elif ch == "3":

                supplier_id = input("Enter Supplier ID : ")

                sup = suppliers.get(supplier_id)

                if sup:

                    sup.display()

                else:

                    print("Supplier Not Found.")

            elif ch == "4":

                supplier_id = input("Enter Supplier ID : ")

                sup = suppliers.get(supplier_id)

                if sup:

                    sup.supplier_stats()

                else:

                    print("Supplier Not Found.")

            elif ch == "5":

                break

            else:

                print("Invalid Choice.")


# =====================================================
# PRODUCT MANAGEMENT
# =====================================================

    elif choice == "3":

        while True:

            print("\n========== PRODUCT MENU ==========")

            print("1. Add Product")
            print("2. Display Products")
            print("3. Search Product")
            print("4. Update Stock")
            print("5. Back")

            ch = input("Enter Choice : ")

            if ch == "1":

                product_id = input("Product ID : ")

                product_name = input("Product Name : ")

                category = input("Category : ")

                cost_price = float(input("Cost Price : "))

                selling_price = float(input("Selling Price : "))

                quantity = int(input("Quantity : "))

                supplier_name = input("Supplier Name : ")

                product = Product(
                    product_id,
                    product_name,
                    category,
                    cost_price,
                    selling_price,
                    quantity,
                    supplier_name
                )

                inventory.add_product(product)

            elif ch == "2":

                inventory.display_products()

            elif ch == "3":

                product_id = input("Enter Product ID : ")

                inventory.search_product(product_id)

            elif ch == "4":

                product_id = input("Product ID : ")

                quantity = int(input("New Quantity : "))

                product = inventory.products.get(product_id)

                if product:

                    product.update_quantity(quantity)

                    print("Quantity Updated Successfully.")

                else:

                    print("Product Not Found.")

            elif ch == "5":

                break

            else:

                print("Invalid Choice.")



# =====================================================
# INVENTORY MANAGEMENT
# =====================================================

    elif choice == "4":

        while True:

            print("\n========== INVENTORY MENU ==========")

            print("1. Display Inventory")

            print("2. Restock Product")

            print("3. Low Stock Products")

            print("4. Inventory Value")

            print("5. Back")

            ch = input("Enter Choice : ")

            if ch == "1":

                inventory.display_products()

            elif ch == "2":

                product_id = input("Product ID : ")

                quantity = int(input("Restock Quantity : "))

                inventory.restock_product(product_id, quantity)

            elif ch == "3":

                print("\nLow Stock Products\n")

                found = False

                for product in inventory.products.values():

                    if product.is_low_stock():

                        product.display()

                        found = True

                if not found:

                    print("No Low Stock Products.")

            elif ch == "4":

                inventory.total_inventory_value()

            elif ch == "5":

                break

            else:

                print("Invalid Choice.")


# =====================================================
# PURCHASE MANAGEMENT
# =====================================================

    elif choice == "5":

        while True:

            print("\n========== PURCHASE MENU ==========")

            print("1. Purchase Product")
            print("2. View Purchase History")
            print("3. Search Purchase")
            print("4. Purchase Summary")
            print("5. Back")

            ch = input("Enter Choice : ")

            if ch == "1":

                supplier_id = input("Supplier ID : ")

                supplier = suppliers.get(supplier_id)

                if not supplier:

                    print("Supplier Not Found.")
                    continue

                product_id = input("Product ID : ")

                quantity = int(input("Quantity : "))

                purchase_manager.purchase_product(
                    supplier,
                    inventory,
                    product_id,
                    quantity,
                )

            elif ch == "2":

                purchase_manager.display_purchases()

            elif ch == "3":

                purchase_id = int(input("Purchase ID : "))

                purchase_manager.search_purchase(purchase_id)

            elif ch == "4":

                purchase_manager.purchase_summary()

            elif ch == "5":

                break

            else:

                print("Invalid Choice.")


# =====================================================
# SALES MANAGEMENT
# =====================================================

    elif choice == "6":

        while True:

            print("\n========== SALES MENU ==========")

            print("1. Make Sale")
            print("2. Sales History")
            print("3. Search Invoice")
            print("4. Sales Summary")
            print("5. Back")

            ch = input("Enter Choice : ")

            if ch == "1":

                customer_id = input("Customer ID : ")

                customer = customers.get(customer_id)

                if not customer:

                    print("Customer Not Found.")
                    continue

                product_id = input("Product ID : ")

                quantity = int(input("Quantity : "))

                sale = sales_manager.make_sale(
                    customer,
                    inventory,
                    product_id,
                    quantity
                )

                if sale:

                    print("\nSale Completed Successfully.")

            elif ch == "2":

                sales_manager.display_sales()

            elif ch == "3":

                invoice = int(input("Invoice Number : "))

                sales_manager.search_invoice(invoice)

            elif ch == "4":

                sales_manager.sales_summary()   

            elif ch == "5":

                break

            else:

                print("Invalid Choice.")


# =====================================================
# BILLING
# =====================================================

    elif choice == "7":

        invoice = int(input("Enter Invoice Number : "))

        sale = sales_manager.search_invoice(invoice)

        if sale:

            billing.generate_invoice(sale)

            save = input("\nSave Invoice? (Y/N): ")

            if save.upper() == "Y":

                billing.save_invoice(sale)


# =====================================================
# REPORTS
# =====================================================

    elif choice == "8":

        while True:

            print("\n========== REPORTS ==========")

            print("1. Inventory Report")

            print("2. Low Stock Report")

            print("3. Customer Report")

            print("4. Supplier Report")

            print("5. Sales Report")

            print("6. Purchase Report")

            print("7. Profit Report")

            print("8. Inventory Value")

            print("9. System Summary")

            print("10. Back")

            ch = input("Enter Choice : ")

            if ch == "1":

                reports.inventory_report(inventory)

            elif ch == "2":

                reports.low_stock_report(inventory)

            elif ch == "3":

                reports.customer_report(customers)

            elif ch == "4":

                reports.supplier_report(suppliers)

            elif ch == "5":

                reports.sales_report(sales_manager)

            elif ch == "6":

                reports.purchase_report(purchase_manager)

            elif ch == "7":

                reports.profit_report(sales_manager)

            elif ch == "8":

                reports.inventory_value_report(inventory)

            elif ch == "9":

                reports.system_summary(
                    customers,
                    suppliers,
                    inventory,
                    sales_manager,
                    purchase_manager
                )

            elif ch == "10":

                break

            else:

                print("Invalid Choice.")


# =====================================================
# AUTHENTICATION
# =====================================================

    elif choice == "9":

        while True:

            print("\n========== AUTHENTICATION ==========")

            print("1. Change Password")

            print("2. Add User")

            print("3. Display Users")

            print("4. Delete User")

            print("5. Back")

            ch = input("Enter Choice : ")

            if ch == "1":

                auth.change_password()

            elif ch == "2":

                auth.add_user()

            elif ch == "3":

                auth.display_users()

            elif ch == "4":

                auth.delete_user()

            elif ch == "5":

                break

            else:

                print("Invalid Choice.")


# =====================================================
# EXIT
# =====================================================

    elif choice == "10":

        auth.logout()

        print("\nThank You For Using Smart Inventory System.")

        break


    else:

        print("Invalid Choice.")