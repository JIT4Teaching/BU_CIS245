def get_user_details():
    name = input("Enter your name: ")
    street_address = input("Enter your street address: ")
    phone_number = input("Enter your phone number: ")
    return name, street_address, phone_number

def write_to_file(file_name, name, street_address, phone_number):
    with open(file_name, 'a') as f:
        f.write(f"{name}, {street_address}, {phone_number}\n")

def read_file(file_name):
    with open(file_name, 'r') as f:
        print(f"Contents of {file_name}:")
        for line in f:
            print(line.strip())

def main():
    file_name = input("Enter the file name: ")
    while True:
        name, street_address, phone_number = get_user_details()
        write_to_file(file_name, name, street_address, phone_number)
        read_file(file_name)

        another_entry = input("Would you like to input another entry? (yes/no): ").lower()
        if another_entry not in ('y', 'yes'):
            print("Closing file and exiting program.")
            break

if __name__ == "__main__":
    main()
