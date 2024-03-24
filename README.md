# Medical Lab Inventory Management System

## Overview

This project is a Medical Lab Inventory Management System designed to manage the inventory of a medical lab using a relational database. The system is built with Python, MySQL, and HTML, aiming to demonstrate the fundamentals of full-stack software development and data warehousing. This project serves as a learning tool and a stepping stone towards a more technical role in the field.

## Database Schema

The database schema consists of four main tables:

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

- **InventoryItems to Suppliers**: One-to-Many. One supplier can supply multiple items, but each item is supplied by one supplier.
- **Orders to Suppliers**: Many-to-One. Each order is placed with one supplier, but a supplier can have multiple orders.
- **Orders to InventoryItems (via OrderItems)**: Many-to-Many. An order can contain multiple items, and an item can be part of multiple orders.

## Development Plan

The development plan includes setting up the database schema, implementing basic CRUD operations for inventory items and orders, and adding a user interface. Future enhancements will include integrating with external APIs for real-time inventory updates.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues to discuss potential improvements or features.

## Database Setup

### Steps to Create the Database and Tables

1. **Create the Database**: `CREATE DATABASE IF NOT EXISTS medical_lab_inventory;`
2. **Use the Database**: `USE medical_lab_inventory;`
3. **Create the Tables**: Use the provided SQL commands to create each table.
4. **Verify the Creation**: `SHOW TABLES`

## Suppliers: Basic CRUD Operations

### Python Functions for CRUD Operations on Suppliers

- **Connect to the Database**: Use `create_connection()` to establish a connection.
- **Insert Operation**: `insert_supplier(connection, supplier_name, contact_name, phone, email)`
- **Read Operation**: `get_suppliers(connection)`
- **Update Operation**: `update_supplier(connection, supplier_id, new_contact_name)`
- **Delete Operation**: `delete_supplier(connection, supplier_id)`

## Inventory Items: Basic CRUD Operations

### Python Functions for CRUD Operations on Inventory Items

- **Connect to Database**: Use `create_connection(test_mode=True)` for test environment.
- **Insert Item**: `insert_item(connection, item_name, quantity, unit_price, supplier_id, reorder_level, reorder_quantity)`
- **Read Operation**: Implemented in `get_items(connection)`
- **Update Item**: Implemented in `update_item(connection, item_id, ...)`
- **Delete Item**: Implemented in `delete_item(connection, item_id)`

## Testing

Unit tests are provided for both suppliers and inventory items to ensure the CRUD operations work as expected.

## Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` package

## Installation

1. Install Python 3.x.
2. Install `mysql-connector-python` using pip: `pip install mysql-connector-python`.
3. Clone this repository or download the necessary scripts.
4. Set up your MySQL database with the required schema.

## Web Application with Flask and HTML

This project also includes a Flask web application that provides an interactive user interface for managing the inventory. The Flask application is defined in `app.py` and uses HTML templates to render the user interface.

### Key Features

- **Home Page**: The home page (`/`) provides an overview of the inventory management system.
- **About Page**: The about page (`/about`) provides information about the project.
- **Suppliers Page**: The suppliers page (`/suppliers`) lists all suppliers in the database.
- **Inventory Items Page**: The inventory items page (`/inventory_items`) lists all inventory items.
- **Order History Page**: The order history page (`/order_history`) lists all orders.
- **Add Supplier**: Allows adding a new supplier to the database.
- **Delete Supplier**: Allows deleting a supplier from the database.
- **Update Supplier**: Allows updating a supplier's information in the database.
- **Insert Item**: Allows adding a new item to the inventory.
- **Update Item**: Allows updating an item's information in the inventory.
- **Delete Item**: Allows deleting an item from the inventory.

### Running the Flask Application

To run the Flask application, ensure you have Python 3.x and the required packages installed. Then, navigate to the project directory in your terminal and run: bash python app.py

The application will start, and you can access it by opening a web browser and navigating to `http://localhost:5000`.

## Conclusion

This project is a comprehensive demonstration of managing a medical lab inventory using a relational database, Python, and MySQL. It serves as a learning tool and a foundation for further development in the field of software engineering.
