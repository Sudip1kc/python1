import json
import os

# Function to register a new user
def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user_type = input("Are you a buyer or a seller? (buyer/seller): ").strip().lower()

    if user_type not in ["buyer", "seller"]:
        print("Invalid user type. Please choose 'buyer' or 'seller'.")
        return

    user_data = {
        "username": username,
        "password": password,
        "user_type": user_type
    }

    # Load existing data if the file exists
    if os.path.exists("userdata.txt"):
        with open("userdata.txt", "r") as file:
            users = json.load(file)
    else:
        users = []

    # Check if username already exists
    if any(user["username"] == username for user in users):
        print("Username already exists. Please choose a different one.")
        return

    # Add new user and save to file
    users.append(user_data)
    with open("userdata.txt", "w") as file:
        json.dump(users, file, indent=4)

    print("Registration successful!")

# Function to authenticate a user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Load user data from file
    if not os.path.exists("userdata.txt"):
        print("No users registered yet.")
        return

    with open("userdata.txt", "r") as file:
        users = json.load(file)

    # Verify credentials
    user = next((user for user in users if user["username"] == username and user["password"] == password), None)
    if not user:
        print("Invalid username or password.")
        return

    print(f"Login successful! Welcome, {username}.")
    if user["user_type"] == "buyer":
        buyer_menu()
    elif user["user_type"] == "seller":
        seller_menu(username)

# Function for buyer menu
def buyer_menu():
    # Load products
    if os.path.exists("product.txt"):
        with open("product.txt", "r") as file:
            products = json.load(file)
    else:
        products = []

    # View available products
    print("\nAvailable Products:")
    for product in products:
        print(f"Name: {product['name']}, Description: {product['description']}, Price: {product['price']}, Seller: {product['seller']}")
    
    print("\n[Placeholder] You can implement buying functionality here.")

# Function for seller menu
def seller_menu(username):
    print("\nSeller Menu:")
    print("1. Add a product")
    print("2. View your products")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_product(username)
    elif choice == "2":
        view_seller_products(username)
    else:
        print("Invalid choice.")

# Function to add a product
def add_product(seller_username):
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = input("Enter product price: ")

    product_data = {
        "name": name,
        "description": description,
        "price": price,
        "seller": seller_username
    }

    # Load existing products
    if os.path.exists("product.txt"):
        with open("product.txt", "r") as file:
            products = json.load(file)
    else:
        products = []

    # Add the new product
    products.append(product_data)
    with open("product.txt", "w") as file:
        json.dump(products, file, indent=4)

    print("Product added successfully!")

# Function to view products added by a specific seller
def view_seller_products(seller_username):
    # Load products
    if os.path.exists("product.txt"):
        with open("product.txt", "r") as file:
            products = json.load(file)
    else:
        products = []

    # Filter products by seller
    seller_products = [product for product in products if product["seller"] == seller_username]

    print("\nYour Products:")
    for product in seller_products:
        print(f"Name: {product['name']}, Description: {product['description']}, Price: {product['price']}")
    
    print("\n[Placeholder] You can enhance this feature further.")

# Main function
def main():
    print("Welcome! Please choose an option:")
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        register()
    elif choice == "2":
        login()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
