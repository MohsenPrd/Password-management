import random
import string
import json
import os


lower = string.ascii_lowercase
uppper = string.ascii_uppercase

# print(uppper)
# print(string.ascii_letters)

symbols = "!@#$%^&*()-+[]{}"
numbers = "0123456789"
all = lower + uppper + symbols + numbers

while True:
    
    print("choose an option :\n\t1) create a password\n\t2) show saved password\n\t3) exit")
    choice = input("your choice : ")

    while choice != '1' and choice != '2' and choice != '3':
        choice = input("invalid option!! select your choice : ")
        

    if choice == "1":

        length = int(input("enter the password length : "))
        password = "".join(random.sample(all, length))
        print(password)


    elif choice == "2":

        if not os.path.exists('Password-management/data_passwords.json'):

            print('you have no saved password!')

        else:

            with open('Password-management/data_passwords.json', 'r') as data_file:

                try:

                    existing_data = json.load(data_file)
                    print(existing_data)

                except json.JSONDecodeError:

                    print('you have no saved password!')

                break
    else:
        print('\n=== End of program ===\n')
        break



    platform = input("Ok, what platform do you want to use this password for? ")



    # Check if the file exists
    if os.path.exists('Password-management/data_passwords.json'):

        with open('Password-management/data_passwords.json', 'r') as data_file:

            try:
                existing_data = json.load(data_file)
            except json.JSONDecodeError:
                existing_data = {}

    else:
        existing_data = {}




    if platform in existing_data:

        submission = input('you have another password for this platform, do you want to update it? ( y / n ) ')
        while submission != 'y' and submission != 'n':
            submission = input('Invalid!!! do you want to update it? ( y / n ) ')
            

        if submission == 'y':
            description = input('write the new description for this password (if you wish): ')

            new_data = { platform : [password, description] }

            # Update the existing data with the new data
            existing_data.update(new_data)



            # Write the updated data back to the file
            with open('Password-management/data_passwords.json', 'w') as data_file:
                json.dump(existing_data, data_file, indent = 4)
        else:
            print('\n=== End of program ===\n')
            break
        


    else:

        description = input('write the description for this password (if you wish): ')

        new_data = { platform : [password, description] }

        # Update the existing data with the new data
        existing_data.update(new_data)


        # Write the updated data back to the file
        with open('Password-management/data_passwords.json', 'w') as data_file:
            json.dump(existing_data, data_file, indent = 4)