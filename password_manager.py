import os
from cryptography.fernet import Fernet
from generate_key import master_password

# Load encryption key from file
with open("key.key", "rb") as file:
    key = file.read()
    cipher = Fernet(key)

def add():
    os.system('cls' if os.name=='nt' else 'clear')
    application_name = input("Enter application name: ").lower()
    user_name = input("Enter application username: ").lower()
    password = input("Enter password: ").lower()

    # string -> binary -> encrypt -> write
    data = f"{application_name}|{user_name}|{password}"
    encrypted_data = cipher.encrypt(data.encode())
    
    with open("./passwords.txt", "ab") as f:
        f.write(encrypted_data + b"\n")
    
    print("Entry added successfully.")
    print()

def view():
    os.system('cls' if os.name=='nt' else 'clear')
    print()
    with open("./passwords.txt", "rb") as file:
        for i, line in enumerate(file.readlines()):
            decrypted_data = cipher.decrypt(line).decode()
            application_name, user_name, password = decrypted_data.split('|')
            print(f"id: {i+1} application name: {application_name} -----> username: {user_name}, password: {password}")
    
    print()

def update():
    os.system('cls' if os.name=='nt' else 'clear')
    print()
    max_id = 0
    with open("./passwords.txt", "rb") as file:
        for i, line in enumerate(file.readlines()):
            decrypted_data = cipher.decrypt(line).decode()
            data = decrypted_data.split('|')
            print(f"id: {i+1} application name: {data[0]} -----> username: {data[1]}, password: {data[2]}")
            max_id = i + 1

    index_number = input("Enter the id number to update an entry: ")
    if index_number.isdigit() and 1 <= int(index_number) <= max_id:
        index_number = int(index_number)
        application_name = input("Enter new application name: ").lower()
        user_name = input("Enter new application username: ").lower()
        password = input("Enter new password: ").lower()
        data = f"{application_name}|{user_name}|{password}"
        
        # Read all lines
        with open("./passwords.txt", "rb") as file:
            lines = file.readlines()

        # Update the specified line
        lines[index_number - 1] = cipher.encrypt(data.encode()) + b"\n"

        # Write back to the file
        with open("./passwords.txt", "wb") as file:
            file.writelines(lines)

        print("Entry updated successfully.")
    else:
        print("Invalid id number, Please try again.")

def delete():
    os.system('cls' if os.name=='nt' else 'clear')
    print()
    view()
    index_number = input("Enter the id number to delete an entry: ")

    if index_number.isdigit():
        index_number = int(index_number)
        with open("./passwords.txt", "rb") as file:
            lines = file.readlines()

        if 1 <= index_number <= len(lines):
            del lines[index_number - 1]

            with open("./passwords.txt", "wb") as file:
                file.writelines(lines)

            print("Entry deleted successfully.")
        else:
            print("Invalid id number.")
    else:
        print("Invalid input, Please try again.")


def check_master_password():
    master_password_hashed = master_password # Replace with the hash of your master password
    attempts = 3

    while attempts > 0:
        entered_password = input("Enter master password: ")
        if (entered_password).encode() == master_password_hashed:
            return True
        else:
            attempts -= 1
            os.system('cls' if os.name=='nt' else 'clear')
            print(f"Incorrect password. {attempts} attempts remaining.")
    
    print("Too many incorrect attempts. Exiting.")
    return False

def main():
    os.system('cls' if os.name=='nt' else 'clear')
    print("**********Password Manager**********")
    print()
    if check_master_password():
        print("Login Successful!")
    else:
        quit()
    print()
    while True: 
        choice = input(
'''Choose any one from below:
    "add"   (a) >> To add a new entry.
    "view"  (v) >> To view existing entries.
    "update"(u) >> To update existing entries.
    "delete"(d) >> To delete existing entries.
    "quit"  (q) >> To quit the application.
        Type here your choice------>> ''').lower()
    
        if choice == 'add' or choice == 'a':
            add()
        elif choice == 'view' or choice == 'v':
            view()
        elif choice == 'update' or choice == 'u':
            update()
        elif choice == 'delete' or choice == 'd':
            delete()
        elif choice == 'quit' or choice == 'q':
            break
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()