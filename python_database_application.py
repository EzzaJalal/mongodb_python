from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["shopping_db"]

# ---------------------- CREATE OPERATIONS ----------------------

# Function to create a new shopping list document
def create_shopping_list():
    # Collect user input for shopping list details
    name = input("Enter list name: ")
    store = input("Enter store name: ")
    shopper = input("Enter shopper name: ")
    completed = input("Is the list completed? (yes/no): ").lower() == "yes"

    # Insert the document into the shopping_lists collection
    result = db.shopping_lists.insert_one({
        "name": name,
        "store_name": store,
        "shopper_name": shopper,
        "is_completed": completed
    })

    # Print confirmation with the generated ObjectId
    print(f"Shopping list created with ID: {result.inserted_id}")

# Function to create a new item document linked to a shopping list
def create_item():
    # Collect item details from user
    list_id = input("Enter shopping list ID: ")  # Must be a valid ObjectId
    name = input("Enter item name: ")
    brand = input("Enter brand: ")
    quantity = int(input("Enter quantity: "))
    tags = input("Enter tags (comma-separated): ").split(",")
    purchased = input("Is the item purchased? (yes/no): ").lower() == "yes"

    # Insert the item into the items collection
    result = db.items.insert_one({
        "list_id": ObjectId(list_id),  # Reference to shopping_lists._id
        "name": name,
        "brand": brand,
        "quantity": quantity,
        "tags": [tag.strip() for tag in tags],
        "is_purchased": purchased
    })

    # Print confirmation with the generated ObjectId
    print(f"Item added with ID: {result.inserted_id}")

# ---------------------- READ OPERATIONS ----------------------

# Function to display all shopping lists
def read_shopping_lists():
    print("\nShopping Lists:")
    for lst in db.shopping_lists.find():
        print(lst)  # Each document is printed as a dictionary

# Function to display all items
def read_items():
    print("\nItems:")
    for item in db.items.find():
        print(item)

# ---------------------- UPDATE OPERATIONS ----------------------

# Function to update a shopping list field
def update_shopping_list():
    list_id = input("Enter list ID to update: ")
    field = input("Field to update (name/store_name/shopper_name/is_completed): ")
    value = input("New value: ")

    # Convert boolean field appropriately
    if field == "is_completed":
        value = value.lower() == "yes"

    # Update the document in the shopping_lists collection
    db.shopping_lists.update_one(
        {"_id": ObjectId(list_id)},
        {"$set": {field: value}}
    )
    print("Shopping list updated.")

# Function to update an item field
def update_item():
    item_id = input("Enter item ID to update: ")
    field = input("Field to update (name/brand/quantity/tags/is_purchased): ")
    value = input("New value: ")

    # Convert data types based on field
    if field == "quantity":
        value = int(value)
    elif field == "tags":
        value = [tag.strip() for tag in value.split(",")]
    elif field == "is_purchased":
        value = value.lower() == "yes"

    # Update the document in the items collection
    db.items.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": {field: value}}
    )
    print("Item updated.")

# ---------------------- DELETE OPERATIONS ----------------------

# Function to delete a shopping list and its associated items
def delete_shopping_list():
    list_id = input("Enter list ID to delete: ")

    # Delete the shopping list
    db.shopping_lists.delete_one({"_id": ObjectId(list_id)})

    # Delete all items linked to that list
    db.items.delete_many({"list_id": ObjectId(list_id)})

    print("Shopping list and its items deleted.")

# Function to delete a single item
def delete_item():
    item_id = input("Enter item ID to delete: ")
    db.items.delete_one({"_id": ObjectId(item_id)})
    print("Item deleted.")

# ---------------------- MAIN MENU ----------------------

# Main loop for the command-line interface
def main():
    while True:
        print("\n🛒 Shopping List Manager")
        print("1. Create shopping list")
        print("2. Create item")
        print("3. Read shopping lists")
        print("4. Read items")
        print("5. Update shopping list")
        print("6. Update item")
        print("7. Delete shopping list")
        print("8. Delete item")
        print("9. Exit")

        choice = input("Choose an option: ")

        # Call the appropriate function based on user choice
        if choice == "1":
            create_shopping_list()
        elif choice == "2":
            create_item()
        elif choice == "3":
            read_shopping_lists()
        elif choice == "4":
            read_items()
        elif choice == "5":
            update_shopping_list()
        elif choice == "6":
            update_item()
        elif choice == "7":
            delete_shopping_list()
        elif choice == "8":
            delete_item()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Entry point of the application
if __name__ == "__main__":
    main()