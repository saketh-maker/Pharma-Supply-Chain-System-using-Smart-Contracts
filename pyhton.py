class PharmaSupplyChain:
    def __init__(self):
        self.products = {}  
        self.history = {}  

    def register_product(self, product_id, name, manufacturer):
        """Registers a new product."""
        if product_id in self.products:
            raise ValueError(f"Product ID {product_id} already exists.")
        self.products[product_id] = {
            'name': name,
            'manufacturer': manufacturer,
            'current_owner': manufacturer,
            'status': 'Manufactured',
            'is_verified': False
        }
        self.history[product_id] = []
        print(f"Product {name} (ID: {product_id}) registered by {manufacturer}.")

    def transfer_product(self, product_id, new_owner, status):
        """Transfers product to a new owner and updates status."""
        if product_id not in self.products:
            raise ValueError(f"Product ID {product_id} does not exist.")
        product = self.products[product_id]
        self.history[product_id].append({
            'from': product['current_owner'],
            'to': new_owner,
            'status': status
        })
        product['current_owner'] = new_owner
        product['status'] = status
        print(f"Product {product_id} transferred to {new_owner} with status '{status}'.")

    def verify_product(self, product_id):
        """Verifies the authenticity of a product."""
        if product_id not in self.products:
            raise ValueError(f"Product ID {product_id} does not exist.")
        self.products[product_id]['is_verified'] = True
        print(f"Product {product_id} verified.")

    def get_product_details(self, product_id):
        """Returns the details of a product."""
        if product_id not in self.products:
            raise ValueError(f"Product ID {product_id} does not exist.")
        return self.products[product_id]

    def get_transfer_history(self, product_id):
        """Returns the transfer history of a product."""
        if product_id not in self.history:
            raise ValueError(f"Product ID {product_id} does not exist.")
        return self.history[product_id]

if __name__ == "__main__":
    system = PharmaSupplyChain()

    while True:
        print("\nChoose an option:")
        print("1. Register a product")
        print("2. Transfer a product")
        print("3. Verify a product")
        print("4. Get product details")
        print("5. Get transfer history")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            manufacturer = input("Enter Manufacturer Name: ")
            system.register_product(product_id, name, manufacturer)

        elif choice == '2':
            product_id = int(input("Enter Product ID: "))
            new_owner = input("Enter New Owner: ")
            status = input("Enter Product Status: ")
            system.transfer_product(product_id, new_owner, status)

        elif choice == '3':
            product_id = int(input("Enter Product ID to Verify: "))
            system.verify_product(product_id)

        elif choice == '4':
            product_id = int(input("Enter Product ID: "))
            details = system.get_product_details(product_id)
            print(f"\nProduct Details:\n{details}")

        elif choice == '5':
            product_id = int(input("Enter Product ID: "))
            history = system.get_transfer_history(product_id)
            print(f"\nTransfer History:\n{history}")

        elif choice == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice! Please try again.")

