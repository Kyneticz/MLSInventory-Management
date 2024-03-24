import unittest
from Database.operations import create_connection, insert_supplier, get_suppliers

class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        self.connection = create_connection(test_mode=True)
        # Optionally, insert some test data here if needed for your tests

    def tearDown(self):
        # Clean up after each test
        self.connection.close()

    def test_insert_supplier(self):
        # Test inserting a supplier
        supplier_name = "Test Supplier"
        contact_name = "Test Contact"
        phone = "1234567890"
        email = "test@example.com"
        insert_supplier(self.connection, supplier_name, contact_name, phone, email)
        # Here, you would typically add assertions to verify the operation
        # For example, you might fetch the newly inserted supplier and check its details

    # Add more test methods as needed for other operations

if __name__ == "__main__":
    unittest.main()