# 🛒 Shopping List Manager

A command-line database application built with **Python** and **MongoDB** for managing shopping lists and their items.  
This project was developed as part of the **"MongoDB with Python"** course and demonstrates full CRUD operations across two related collections.

---

## 🚀 Technologies Used

- **MongoDB** – NoSQL database for storing shopping lists and items  
- **PyMongo** – Python driver for MongoDB  
- **Python 3** – Core programming language

---

## 📂 Project Files

- `shopping_list_manager.py` – Main application with a menu-driven interface supporting full CRUD operations  
- `mongo_test.py` – A test script for verifying MongoDB connection, inserting sample data, and printing item details

---

## 🧑‍💻 How to Run the App

### 1. Install Dependencies

Make sure you have **Python** and **MongoDB** installed. Then install **PyMongo**:

```bash
pip install pymongo


2. Start MongoDB Locally
mongod

3. Run the Main Application
python shopping_list_manager.py


Follow the menu prompts to create, read, update, or delete shopping lists and items.

4. Run the Test Script (Optional)
python mongo_test.py


This script:

Connects to the database

Inserts a sample item (Cookies)

Prints all item details from the items collection

📋 Example Commands

📝 Create a Shopping List
Enter list name: Birthday Party
Enter store name: Lidl
Enter shopper name: Ezza
Is the list completed? (yes/no): no

🛍️ Create an Item
Enter shopping list ID: 507f1f77bcf86cd799439011
Enter item name: Chips
Enter brand: Pringles
Enter quantity: 2
Enter tags (comma-separated): Snacks, Salty
Is the item purchased? (yes/no): no

✏️ Update an Item
Enter item ID to update: <paste item ID>
Field to update: quantity
New value: 5

🖼️ Screenshots
🧪 mongo_test.py Output
Shows successful MongoDB connection, item insertion, and printed item details from the items collection.

🗂️ MongoDB Compass View
Displays the structure and contents of the shopping_lists and items collections, verifying that documents are inserted and linked correctly.

🛒 Shopping List Manager Interface
Command-line menu interface for managing shopping lists and items using full CRUD operations.
