To run all tests 
python -m pytest test/


The skeleton file is the code skeleton with instructions which would be given to the students


System Requirements Specification Index

For

Medicine List Maker Console Application
Version 1.0   

IIHT Pvt. Ltd.
fullstack@iiht.com
TABLE OF CONTENTS

1	Project Abstract	
2	Business Requirements	
3	Constraints	
4	Template Code Structure	
5	Execution Steps to Follow	

 
Medicine List Maker Console 
System Requirements Specification

1	PROJECT ABSTRACT

MedTrack Solutions, a healthcare software provider in Bangalore, has been approached by JanAushadhi, a chain of government-subsidized pharmacy stores, to create a simple inventory tracking solution for their new pharmacists. Many of their stores are in rural areas where internet connectivity is unreliable, so they need a basic console application that can run offline. The Medicine List Maker will help new pharmacy staff record essential medicine details, calculate stock requirements, and manage inventory pricing.
2	BUSINESS REQUIREMENTS:

Screen Name	Console input screen
Problem Statement	1.	Application must collect medicine details using different data types
2.	System should perform basic calculations on the input data
3.	Program should format and display information in organized sections
4.	Console should demonstrate: String input/output, Integer input/output with calculations, Float input/output with calculations, Basic formatting techniques

3	CONSTRAINTS 
3.1	INPUT REQUIREMENTS
1.	Medicine Name: 
o	Must be stored as float in variable medicine_name
o	Example: "Crocin 500mg"
2.	Manufacturer: 
o	Must be stored as string in variable manufacturer
o	Example: "GlaxoSmithKline"
3.	Batch Number: 
o	Must be stored as string in variable batch_number
o	Example: "BN2024001"
4.	Quantity: 
o	Must be stored as integer in variable quantity 
o	Must be converted using int() 
o	Example: 500
5.	Minimum Quanitity:
o	Must be stored as integer in variable min_quantity 
o	Must be converted using int() 
o	Example: 100 
6.	Tablets Per Strip:
o	Must be stored as integer in variable tablets_per_strip 
o	Must be converted using int() 
o	Example: 10
7.	Price:
o	Must be stored as float in variable price_per_strip 
o	Must be converted using float() 
o	Example: 45.50
8.	Discount:
o	Must be stored as float in variable discount_percent 
o	Must be converted using float() 
o	Example: 10.0

9.	Dates:
o	Must be stored as string in variables manufacture_date and expiry_date 
o	Format: DD-MM-YYYY 
o	Example: "15-02-2024"
10.	Storage:
o	Must be stored as string in variable storage_instructions 
o	Example: "Store in a cool, dry place"
3.2	CALCULATION CONSTRAINTS
1.	Strip Calculations: 
○	Complete Strips: quantity // tablets_per_strip 
○	Loose Tablets: quantity % tablets_per_strip 
○	Example: 500 tablets with 10 per strip = 50 strips and 0 loose
2.	Price Calculations:
○	Discounted Price: price_per_strip * (1 - discount_percent/100) 
○	Total Value: total_strips * price_per_strip 
○	Example: ₹45.50 with 10% discount = ₹40.95
3.3	OUTPUT CONSTRAINTS
1. Display Format:
o	Must show "Basic Information" 
o	Must show "Stock Information" 
o	Must show "Price Information" 
o	Must show "Date and Storage Information" 
o	Must show "Stock Status"

2.	Number Output Format:
o	Prices must show 'Rs.' prefix
o	Prices must show 2 decimal places 
o	Quantities must show as whole numbers 
o	Percentages must show % symbol
3.	Status messages:
o	Show "REORDER REQUIRED" if quantity <= min_quantity 
o	Show "STOCK SUFFICIENT" if quantity > min_quantity

4. TEMPLATE CODE STRUCTURE:
1. Display Header Section:
o	Welcome message at the start "Welcome!"
2. Input Collection:
o	String inputs for names and dates
o	Integer inputs for quantities
o	Float inputs for prices
3. Calculations Section:
o	Strip calculations 
o	Price calculations 
o	Status determination 
4. Output Section:
o	Formatted sections 
o	Organized information 
o	Status message

5. EXECUTION STEPS TO FOLLOW:
1.	Run the program
2.	Enter medicine basic details
3.	Enter quantity information
4.	Enter price information
5.	Enter dates and storage
6.	View formatted output