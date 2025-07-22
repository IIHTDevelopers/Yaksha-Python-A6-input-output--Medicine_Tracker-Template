# Medicine List Maker
# This program helps track medicine inventory using input/output operations

"""
You need to create a medicine inventory tracker that collects medicine details,
performs calculations, and displays organized information.

Required Variables (define these with correct data types):
- medicine_name (string)
- manufacturer (string) 
- batch_number (string)
- quantity (integer)
- min_quantity (integer)
- tablets_per_strip (integer)
- price_per_strip (float)
- discount_percent (float)
- manufacture_date (string)
- expiry_date (string)
- storage_instructions (string)
- total_strips (integer - calculated)
- loose_tablets (integer - calculated)
- discounted_price (float - calculated)
- stock_value (float - calculated)

Required Functions:
- calculate_strips(quantity, tablets_per_strip) - returns integer
- calculate_loose(quantity, tablets_per_strip) - returns integer  
- calculate_discount(price, discount_percent) - returns float
- calculate_stock_value(strips, price) - returns float

Required Output Sections:
- Basic Information
- Stock Information  
- Price Information
- Date and Storage Information
- Stock Status
"""

# TODO: Define all required variables with appropriate initial values

# TODO: Implement calculation functions
def calculate_strips(quantity, tablets_per_strip):
    """Calculate complete strips from total quantity"""
    # TODO: Use integer division to return complete strips
    pass

def calculate_loose(quantity, tablets_per_strip):
    """Calculate loose tablets remaining"""
    # TODO: Use modulo operation to return remaining tablets
    pass

def calculate_discount(price, discount_percent):
    """Calculate discounted price"""
    # TODO: Apply discount formula and return discounted price
    pass

def calculate_stock_value(strips, price):
    """Calculate total stock value"""
    # TODO: Calculate and return total value
    pass

# Main program
if __name__ == "__main__":
    # TODO: Display welcome message
    
    # TODO: Collect all user inputs with proper type conversions
    
    # TODO: Perform all calculations using the functions
    
    # TODO: Display formatted output in required sections
    
    pass
