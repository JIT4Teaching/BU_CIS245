import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def get_user_details():
    name = input("Enter your name: ")
    street_address = input("Enter your street address: ")
    phone_number = input("Enter your phone number: ")
    return name, street_address, phone_number

def write_to_file(file_name, name, street_address, phone_number):
    with open(file_name, 'a') as f:
        f.write(f"{name}, {street_address}, {phone_number}\n")

def read_file(file_name):
  red = "\033[31m"
  reset = "\033[0m"
    
  with open(file_name, 'r') as f:
        print(f"\nContents of file - {file_name}:\n")
        for line in f:
            print(f"{red}{line.strip()}{reset}")

def main():
    file_name = input("Enter the file name: ")
    while True:
        clear_screen()
        name, street_address, phone_number = get_user_details()
        write_to_file(file_name, name, street_address, phone_number)
        read_file(file_name)

        another_entry = input("\nWould you like to input another entry? (yes/no): ").lower()
        if another_entry not in ('y', 'yes'):
            print("\nClosing file and exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()
