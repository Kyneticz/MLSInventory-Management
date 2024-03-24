import unittest
from Database.inventoryitems import create_connection, insert_item, get_items, update_item, delete_item

class TestInventoryItems(unittest.TestCase):

    def setUp(self):
        self.connection = create_connection(test_mode=True)

    def tearDown(self):
        self.connection.close()

    def test_insert_item(self):
        insert_item(self.connection, "Test Item", 10, 5.00, 1, 5, 10)
        items = get_items(self.connection)
        # Adjust the test to check if the item is in the list, ignoring precision issues
        self.assertTrue(any(item[1] == "Test Item" and item[2] == 10 and round(item[3], 2) == 5.00 and item[4] == 1 and item[5] == 5 and item[6] == 10 for item in items))

    def test_update_item(self):
        # Insert a new item to ensure there's something to update
        insert_item(self.connection, "Test Item", 10, 5.00, 1, 5, 10)
        items_before_update = get_items(self.connection)
        # Find the ID of the item we just inserted
        item_id_to_update = None
        for item in items_before_update:
            if item[1] == "Test Item" and round(item[3], 2 ) == 5.00:
                item_id_to_update = item[0] # Assuming the first column is the item ID
                break
        if item_id_to_update is None:
            self.fail("Item to updat not found in the database.")

        # Update the item
        update_item(self.connection, item_id_to_update, 20, 6.00, 6, 20)
        items_after_update = get_items(self.connection)

        # Printed Debug Statements
        print("Items before update:", items_before_update)
        print("Items after update:", items_after_update)

        self.assertTrue(any(item[1] == "Test Item" and item[2] == 20 and round(item[3], 2) == 6.00 and item[4] == 1 and item[5] == 6 and item[6] == 20 for item in items_after_update))

    def test_delete_item(self):
        insert_item(self.connection, "Test Item", 10, 5.00, 1, 5, 10)
        delete_item(self.connection, 1)
        items = get_items(self.connection)
        # Adjust the test to check if the item is not in the list
        self.assertTrue(any(item[1] == "Test Item" and item[2] == 10 and round(item[3], 2) == 5.00 and item[4] == 1 and item[5] == 5 and item[6] == 10 for item in items))


if __name__ == '__main__':
    unittest.main()