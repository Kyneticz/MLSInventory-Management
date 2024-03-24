from flask import Flask, render_template, request, redirect, url_for, flash
from Database import operations, inventoryitems

app = Flask(__name__)
app.secret_key = 'MLSDatabaseproject' # Setting secret key
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('pages/about.html')
@app.route('/suppliers')
def suppliers():
    connection = operations.create_connection()
    suppliers = operations.get_suppliers(connection) # Placeholder function
    connection.close()
    return render_template('pages/suppliers.html', suppliers=suppliers)
@app.route('/inventory_items')
def inventory_items():
    # Placeholder for fetching and displaying inventory items
    return render_template('pages/inventory_items.html')
@app.route('/order_history')
def order_history():
    # Placeholder for fetching and displaying order history
    return render_template('pages/order_history.html')
@app.route('/add_supplier', methods=['GET', 'POST'])
def add_supplier(): # Corrected function name
    if request.method == 'POST':
        supplier_name = request.form['supplier_name']
        contact_name = request.form['contact_name']
        phone = request.form['phone']
        email = request.form['email']

        connection = operations.create_connection()
        operations.insert_supplier(connection, supplier_name, contact_name, phone, email)
        connection.close()

        return redirect(url_for('home'))
    return render_template('add_supplier.html')

@app.route('/delete_supplier', methods=['GET', 'POST'])
def delete_supplier(): # Corrected function name and parameters
    if request.method == 'POST':
        supplier_id = request.form['supplier_id']

        connection = operations.create_connection()
        operations.delete_supplier(connection, supplier_id)
        connection.close()

        return redirect(url_for('home'))
    return render_template('delete_supplier.html')

@app.route('/update_supplier', methods=['GET', 'POST'])
def update_supplier(): # Corrected function name and parameters
    if request.method == 'POST':
        supplier_id = request.form['supplier_id']
        new_contact_name = request.form['new_contact_name']

        connection = operations.create_connection()
        operations.update_supplier(connection, supplier_id, new_contact_name)
        connection.close()

        return redirect(url_for('home'))
    return render_template('update_supplier.html')

############### Separation for inventory items ###############

@app.route('/insert_item', methods=['GET', 'POST'])
def insert_item():
    if request.method == 'POST':
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        unit_price = request.form['unit_price']
        supplier_id = request.form['supplier_id']
        reorder_level = request.form['reorder_level']
        reorder_quantity = request.form['reorder_quantity']

        connection = inventoryitems.create_connection()
        inventoryitems.insert_item(connection, item_name, quantity, unit_price, supplier_id, reorder_level, reorder_quantity)
        connection.close()
        flash('Item successfully added into the inventory')

        return redirect(url_for('inventory_items'))
    return render_template('inventory_items.html')

@app.route('/update_item', methods=['GET', 'POST'])
def update_item():
    if request.method == 'POST':
        item_id = request.form['item_id']
        new_quantity = request.form['new_quantity']
        new_unit_price = request.form['new_unit_price']
        new_reorder_level = request.form['new_reorder_level']
        new_reorder_quantity = request.form['new_reorder_quantity']

        connection = inventoryitems.create_connection()
        inventoryitems.update_item(connection, item_id, new_quantity, new_unit_price, new_reorder_level, new_reorder_quantity)
        connection.close()
        flash('Item successfully updated in the inventory')

        return redirect(url_for('inventory_items'))
    return render_template('inventory_items.html')

@app.route('/delete_item', methods=['GET', 'POST'])
def delete_item():
    if request.method == 'POST':
        item_id = request.form['item_id']

        connection = inventoryitems.create_connection()
        inventoryitems.delete_item(connection, item_id)
        connection.close()
        flash('Item successfully deleted from the inventory')
        return redirect(url_for('inventory_items'))
    return render_template('inventory_items.html')

if __name__ == '__main__':
    app.run(debug=True)