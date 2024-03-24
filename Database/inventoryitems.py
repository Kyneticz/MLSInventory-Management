import mysql.connector

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

def get_items(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM InventoryItems"
    cursor.execute(query)
    items = cursor.fetchall()
    return items # Ensures the function returns the items

def update_item(connection, item_id, new_quantity, new_unit_price, new_reorder_level, new_reorder_quantity):
    cursor = connection.cursor()
    query = """
    UPDATE InventoryItems
    SET quantity = %s, unit_price = %s, reorder_level = %s, reorder_quantity = %s
    WHERE item_id = %s
    """
    # Round new_unit_price to two decimal places
    new_unit_price_rounded = round(new_unit_price, 2)
    cursor.execute(query, (new_quantity, new_unit_price_rounded, new_reorder_level, new_reorder_quantity, item_id))
    connection.commit()
    print(f"Item with ID {item_id} updated successfully.")

def delete_item(connection, item_id):
    cursor = connection.cursor()
    query = "DELETE FROM InventoryItems WHERE item_id = %s"
    cursor.execute(query, (item_id,))
    connection.commit()
    print(f"Item with ID {item_id} deleted successfully.")

if __name__ == "__main__":
    connection = create_connection()

    # Example: Insert a new item
    insert_item(connection, "New Item", 100, 10.00, 1, 50, 100)

    # Example: Get all items
    get_items(connection)

    # Example: Update an item's quantity, unit price, reorder level, and reorder quantity
    update_item(connection, 1, 150, 12.00, 60, 150)

    # Example: Delete an item
    delete_item(connection, 1)

    connection.close()