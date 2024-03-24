# Medical Lab Inventory Management System

## Database Schema

This project utilizes a relational database to manage the inventory of a medical lab. 
The schema consists of four main tables: `InventoryItems`, `Orders`, `Suppliers`, and `OrderItems`. 
This project was started as a means of learning how to code utilizing Python, MySQL, and ultimately 
taking the relational database and creating a interactable user interface through HTML.

I built this project to understand the fundamentals of full-stack software development and data warehousing; In addition,
this project will serve as a means to help me sharpen my skill as I continue to make small iterations.
Ultimately, I used this a means to work on my technical acumen as I desire to transition from healthcare to that of a more technical rol

### Tables

1. **InventoryItems**
   - `item_id`: Primary Key, Unique Identifier for each inventory item.
   - `item_name`: Name of the inventory item.
   - `quantity`: Current quantity of the item in stock.
   - `unit_price`: Price per unit of the item.
   - `supplier_id`: Foreign Key, references `Suppliers(supplier_id)`.
   - `reorder_level`: The minimum quantity that triggers a reorder.
   - `reorder_quantity`: The quantity to order when reordering.

2. **Orders**
   - `order_id`: Primary Key, Unique Identifier for each order.
   - `order_date`: Date when the order was placed.
   - `supplier_id`: Foreign Key, references `Suppliers(supplier_id)`.
   - `total_cost`: Total cost of the order.

3. **Suppliers**
   - `supplier_id`: Primary Key, Unique Identifier for each supplier.
   - `supplier_name`: Name of the supplier.
   - `contact_name`: Name of the contact person at the supplier.
   - `phone`: Contact phone number.
   - `email`: Contact email address.

4. **OrderItems**
   - `order_id`: Foreign Key, references `Orders(order_id)`.
   - `item_id`: Foreign Key, references `InventoryItems(item_id)`.
   - `quantity`: Quantity of the item ordered.
   - `unit_price`: Price per unit of the item at the time of the order.

### Relationships

- **InventoryItems to Suppliers:** One-to-Many. One supplier can supply multiple items, but each item is supplied by one supplier.
- **Orders to Suppliers:** Many-to-One. Each order is placed with one supplier, but a supplier can have multiple orders.
- **Orders to InventoryItems (via OrderItems):** Many-to-Many. An order can contain multiple items, and an item can be part of multiple orders.

### Development Plan

The development of this project will follow a structured approach, starting with setting up the database schema and moving on to implementing the basic CRUD operations for inventory items and orders. 
Further enhancements will include adding a user interface and integrating with external APIs for real-time inventory updates.

### Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to discuss potential improvements or features.

------------------------------------------------------------------------------------------------------------------------

Section 1. ## [Database Setup]

This section outlines the steps to create the database and tables for the Medical Lab Inventory Management System.

### Step 1: Create the Database
	# [MySQL workbench] : CREATE DATABASE IF NOT EXISTS medical_lab_inventory;
### Step 2: Use the Database
	# [MySQL workbench] : USE medical_lab_inventory;
### Step 3: Create the Tables 
	# [MySQL workbench] CREATE TABLE (table_name) (.....
### Step 4: Verify the Creation
	# [MySQL workbench] SHOW TABLES

This documentation provides a clear record of how the database and tables were set up, which is crucial for future reference and for anyone else who might work on the project.

------------------------------------------------------------------------------------------------------------------------

Section 2. ## [Suppliers] [Basic CRUD Operations]

This section outlines how to perform basic CRUD (CREATE, READ, UPDATE, DELETE) operations on the Medical Laboratory Inventory Management System using Python.
This section outlines specifically for suppliers.

### Step 1: Connect to the Database

[Python]
import mysql.connector
def create_connection(): 
	connection = mysql.connector.connect( host="localhost", 
		user="your_username", 
		password="your_password", 
		database="medical_lab_inventory"
) 
return connection

### Step 2: Insert Operation

[Python]
def insert_supplier(connection, supplier_name, contact_name, phone, email): 
# Function implementation

### Step 3: Read Operation

[Python]
def get_suppliers(connection): 
# Function implementation

### Step 4: Update Operation
	
[Python]
def update_supplier(connection, supplier_id, new_contact_name): 
# Function implementation

### Step 5: Delete Operation

[Python]
def delete_supplier(connection, supplier_id): 
# Function implementation

### Step 6: Testing the Operations
# Creation of test_database_operations.py
# To enable a test environment and separation from the production environment, a new SQL Database was generated named: medical_laboratory_inventory_test

[Python]

import unittest
from Database.operations import create_connection, insert_supplier, get_suppliers, delete_supplier

class TestDatabaseOperations(unittest.TestCase):
	def setUp(self):
 		self.connection = create_connection(test_mode=True)
   	def tearDown(self):
    		self.connection.close()
      	def test_insert_supplier(self):
       		# Tests for inserting a supplier
	 	supplier_name = "Test Supplier"
   		contact_name = "Test Contact"
     		phone = "1234567890"
       		email = "test@example.com"
	 	supplier_id = insert_supplier(self.connection, supplier_name, contact_name, phone, email)
   	def test_get_suppliers(self):
    		suppliers = get_suppliers(self.connection)
 	def test_delete_supplier(self):
        	supplier_name = "Test Supplier to Delete"
        	contact_name = "Test Contact"
        	phone = "1234567890"
        	email = "test@example.com"
        	supplier_id = insert_supplier(self.connection, supplier_name, contact_name, phone, email)

delete_supplier(self.connection, supplier_id)

    # Add more test methods as needed for other operations

if __name__ == "__main__":
    unittest.main()

# Test environment is created to test for different functionalities that were established in operations.py.
------------------------------------------------------------------------------------------------------------------------
## Section 3: [Inventory Items] [Basic CRUD Operations]

This section introduces the `inventoryitems.py` script, which manages inventory items in a medical laboratory setting. The script provides functionalities to insert, retrieve, update, and delete inventory items from a MySQL database. This section was simplified but follows the same idea as the operations.py script regarding suppliers where we introduce basic CRUD operations: insert_item, get_items, update_item, and delete_item.

### Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` package

### Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the `mysql-connector-python` package using pip:
 	pip install mysql-connector-python
3. Clone this repository or download the 'inventoryitems.py' script.
4. Set up your MySQL database with the necessary schema for inventory items.

### Step-by-step documentation ###
# Step 1: Connect to Database

def create_connection(test_mode=True):
	if test_mode:
        	host = "localhost"
        	database = "medical_lab_inventory_test"
        	user = "root"
        	password = "MLSdatabaseproj"
	else:
        	host = "localhost"
        	database = "medical_lab_inventory"
        	user = "root"
        	password = "MLSdatabaseproj"
	connection = mysql.connector.connect(
        	host=host,
        	user=user,
        	password=password,
        	database=database
	 )
	print("Database connection successful.")
	return connection
 
### Step 2 : Insert Item function

def insert_item(connection, item_name, quantity, unit_price, supplier_id, reorder_level, reorder_quantity):
    cursor = connection.cursor()
    query = """
    INSERT INTO InventoryItems (item_name, quantity, unit_price, supplier_id, reorder_level, reorder_quantity)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    # Round unit_price to two decimal places
    unit_price_rounded = round(float(unit_price), 2)
    cursor.execute(query, (item_name, quantity, unit_price_rounded, supplier_id, reorder_level, reorder_quantity))
    connection.commit()
    print(f"Item {item_name} added successfully.")


