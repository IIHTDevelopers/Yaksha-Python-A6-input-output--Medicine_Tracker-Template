# Medicine List Maker
# This program helps track medicine inventory using input/output operations

# Initialize variables with correct names as per requirements
medicine_name = ""
manufacturer = ""
batch_number = ""
quantity = 0
min_quantity = 0
tablets_per_strip = 0
price_per_strip = 0.0
discount_percent = 0.0
manufacture_date = ""
expiry_date = ""
storage_instructions = ""
total_strips = 0
loose_tablets = 0
discounted_price = 0.0
stock_value = 0.0

# Calculation functions with correct implementations
def calculate_strips(quantity, tablets_per_strip):
    return quantity // tablets_per_strip  # Integer division for complete strips

def calculate_loose(quantity, tablets_per_strip):
    return quantity % tablets_per_strip  # Modulo for remaining tablets

def calculate_discount(price, discount_percent):
    return price * (1 - discount_percent/100)  # Correct discount calculation

def calculate_stock_value(strips, price):
    return strips * price  # Multiplication for total value

# Main program
if __name__ == "__main__":
    # Display welcome header
    print("=" * 50)
    print("Welcome!".center(50))
    print("MEDICINE LIST MAKER".center(50))
    print("=" * 50)
    print()

    # Get Basic Information
    medicine_name = input("Enter medicine name: ")
    manufacturer = input("Enter manufacturer name: ")
    batch_number = input("Enter batch number: ")

    # Get Quantity Information
    quantity = int(input("Enter quantity in stock: "))
    min_quantity = int(input("Enter minimum required quantity: "))
    tablets_per_strip = int(input("Enter number of tablets per strip: "))

    # Get Price Information
    price_per_strip = float(input("Enter price per strip: "))
    discount_percent = float(input("Enter discount percentage: "))

    # Get Date and Storage Information
    manufacture_date = input("Enter manufacture date (DD-MM-YYYY): ")
    expiry_date = input("Enter expiry date (DD-MM-YYYY): ")
    storage_instructions = input("Enter storage instructions: ")

    # Perform Calculations
    total_strips = calculate_strips(quantity, tablets_per_strip)
    loose_tablets = calculate_loose(quantity, tablets_per_strip)
    discounted_price = calculate_discount(price_per_strip, discount_percent)
    stock_value = calculate_stock_value(total_strips, price_per_strip)

    # Display Information
    print("=" * 50)
    print("MEDICINE DETAILS")
    print("=" * 50)
    print()

    print("Basic Information")
    print("-" * 20)
    print("Medicine:", medicine_name)
    print("Manufacturer:", manufacturer)
    print("Batch Number:", batch_number)
    print()

    print("Stock Information")
    print("-" * 20)
    print("Total Quantity:", quantity)
    print("Complete Strips:", total_strips)
    print("Loose Tablets:", loose_tablets)
    print("Minimum Required:", min_quantity)
    print("Tablets Per Strip:", tablets_per_strip)
    print()

    print("Price Information")
    print("-" * 20)
    print(f"Price Per Strip: Rs.{price_per_strip:.2f}")
    print(f"Discount: {discount_percent}%")
    print(f"Discounted Price: Rs.{discounted_price:.2f}")
    print(f"Total Stock Value: Rs.{stock_value:.2f}")
    print()

    print("Date and Storage Information")
    print("-" * 20)
    print("Manufacturing Date:", manufacture_date)
    print("Expiry Date:", expiry_date)
    print("Storage:", storage_instructions)
    print()

    print("Stock Status")
    print("-" * 20)
    if quantity <= min_quantity:
        print("REORDER REQUIRED")
    else:
        print("STOCK SUFFICIENT")

    print()
    print("=" * 50)