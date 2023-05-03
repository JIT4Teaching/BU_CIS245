# Mike Tomb
# Assignment 8.1
# Due: May 7th, 2023
# CIS245-309H Into to Python
# This program creates a file and performs file-processing activities.

# This code imports the OS module, which provides functions for interacting with the operating system.
import os

# This function clears the screen.
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

# This function prompts the user to enter their name, street address, and phone number.
# The function then stores the user's input in variables.
def get_user_details():
    name = input("Enter your name: ")
    street_address = input("Enter your street address: ")
    phone_number = input("Enter your phone number: ")
    return name, street_address, phone_number

# This function takes in four arguments: file_name, name, street_address, and phone_number.
# It then opens the file specified by file_name in append mode.
# It then writes the name, street_address, and phone_number to the file, separated by commas and followed by a new line. 
# Finally, it closes the file.
def write_to_file(file_name, name, street_address, phone_number):
    with open(file_name, 'a') as f:
        f.write(f"{name}, {street_address}, {phone_number}\n")

# This code defines two variables: red and reset.
# The red variable stores the ANSI escape code for red text.
# The reset variable stores the ANSI escape code for resetting the text color.
def read_file(file_name):
  red = "\033[31m"
  reset = "\033[0m"

# This code opens a file with the given file name in read mode.
# It then prints the contents of the file line by line, with each line being printed in red.
  with open(file_name, 'r') as f:
        print(f"\nContents of file - {file_name}:\n")
        for line in f:
            print(f"{red}{line.strip()}{reset}")

# This code prompts the user to enter a file name.
# It then calls the get_user_details() function to get the user's name, street address, and phone number.
# It then calls the write_to_file() function to write the user's details to the file.
# It then calls the read_file() function to read the file and print out the user's details.
# It then prompts the user if they would like to enter another entry, and if not, exits the program.
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

# This code checks if the current module is the main module.
# If it is, then it calls the main() function.
if __name__ == "__main__":
    main()
