# Medical Lab Inventory Management System

## Database Schema

This project utilizes a relational database to manage the inventory of a medical lab. 
The schema consists of four main tables: `InventoryItems`, `Orders`, `Suppliers`, and `OrderItems`. 
This project was started as a means of learning how to code utilizing Python, MySQL, and ultimately 
taking the relational database and creating a interactable user interface through HTML.

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

1. ## Database Setup

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

2. ## Basic CRUD Operations

This section outlines how to perform basic CRUD (CREATE, READ, UPDATE, DELETE) operations on the Medical Laboratory Inventory Management System using Python.

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
def insert_supplier(connection, supplier_name, contact_name, phone, email): # Function implementation

### Step 3: Read Operation

[Python]
def get_suppliers(connection): # Function implementation

### Step 4: Update Operation
	
[Python]
def update_supplier(connection, supplier_id, new_contact_name): # Function implementation

### Step 5: Delete Operation

[Python]
def delete_supplier(connection, supplier_id): # Function implementation

### Step 6: Testing the Operations

