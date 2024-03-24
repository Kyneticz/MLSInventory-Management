import mysql.connector
def create_connection(test_mode=True):
    if test_mode:
        # Use the test database connection details
        host = "localhost"
        database = "medical_lab_inventory_test",
        user = "root"
        password = "MLSdatabaseproj"
    else:
        # Use the production database connection details
        host = "localhost"
        database = "medical_lab_inventory"
        user = "root"
        password = "MLSdatabaseproj"

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MLSdatabaseproj",
        database="medical_lab_inventory", #Change databases to enable testing environment
    )
    print("Database connection successful.") # Add this line to verify
    return connection
def insert_supplier(connection, supplier_name, contact_name, phone, email):
    cursor = connection.cursor()
    query = """
    INSERT INTO Suppliers (supplier_name, contact_name, phone, email)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (supplier_name, contact_name, phone, email))
    connection.commit()
    print(f"Supplier {supplier_name} added successfully.")
def get_suppliers(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM Suppliers"
    cursor.execute(query)
    suppliers = cursor.fetchall()
    for supplier in suppliers:
        print(supplier)
def update_supplier(connection, supplier_id, new_contact_name):
    cursor = connection.cursor()
    query = """
    UPDATE Suppliers
    SET contact_name = %s
    WHERE supplier_id = %s
    """
    cursor.execute(query, (new_contact_name, supplier_id))
    connection.commit()
    print(f"Supplier contact name updated successfully.")
def delete_supplier(connection, supplier_id):
    cursor = connection.cursor()
    query = "DELETE FROM Suppliers WHERE supplier_id = %s"
    cursor.execute(query, (supplier_id,))
    connection.commit()
    print(f"Supplier with ID {supplier_id} deleted successfully.")

if __name__ == "__main__":
    connection = create_connection()

    # Example: Insert a new supplier
    insert_supplier(connection, "New Supplier", "John Doe", "1234567890", "john.doe@example.com")

    # Example: Get all suppliers
    get_suppliers(connection)

    # Example: Update a supplier's contact name
    update_supplier(connection, 1, "Jane Doe")

    # Example: Delete a supplier
    delete_supplier(connection, 1)

    connection.close()

