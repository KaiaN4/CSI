import sys #imports the sys library
import random #imports the random library
import csv #imports the csv library
from pathlib import Path #imports the path library

def insert_wup(websites, usernames, passwords): #creates a function named insert_wup
    '''
    Allows the user to enter a new website, username, and password
    Args:
        websites (str): Allows the user to enter a new website
        usernames (str): Allows the user to enter a new username
        passwords (str): Allows the user to enter a new password
    Returns:
        str: Adds the new websites, usernames, and passwords to their designated lists
    '''
   #creates a variable for the user to input their website
    websites.append(input("Enter your website: ")) #asks the user to enter a website and adds it to the list
    usernames.append(input("Enter your username: ")) #asks the user to enter a username and adds it to the list
    passwords.append(input("Enter your password: ")) #asks the user to enter a password and adds it to the list

def change_value(websites, change_list, change, website): #creates a function named change_value
    '''
    Allows the user to change either a username or password that they have already input
    Args:
        websites (str): Finds the index of a website that the user wants to change the password or username of
        change_list (str): Allows the user to say what website they want to change the password or username of
        change (str): Allows the user to change either their password or
        website (str): context
    Returns:
        str: Changes the user's password or username that they want to change within the list that it is already in
    '''
    change_list[websites.index(website)] = input(f"Enter your new {change}: ") #creates a variable for the user to input their new username

def check_security(password): #creates a function named check_security
    '''
    Checks the security of a password that the user inputs by individually checking if there is a special character, uppercase letter, lowercase letter, or a number. If the password is missing any of those, it will tell the user which one, and say that it is not secure
    Args:
        password(str): A password that is going to be checked for its security
    Prints:
        description: If the user is missing a special character, uppercase letter, lowercase letter, or number, it will tell the user which one and say that it is not secure if one is missing
    '''
    security = 0 #starts the security at 0
    if len(password) < 8: #if the length of the password is less than 8
        print("Create a longer password") #prints "Create a longer password"
        security -= 1 #subtracts one from the security
    if not any(char in list("!@#$%^&*()") for char in password): #if any of the characters in the list are not in password
        print("You should include a special character") #print "You should include a special character"
        security -= 1 #subtracts one from the security
    if not any(char.isupper() for char in password): #if there is not an uppercase letter in password
        print("You should have an uppercase letter") #print "You should have an uppercase letter"
        security -= 1 #subtracts one from the security
    if not any(char.islower() for char in password): #if there are no lowercase letters in password
        print("You should insert a lowercase letter") #print "You should insert a lowercase letter"
        security -= 1 #subtracts one from the security
    if not any(char.isdigit() for char in password): #if there are no numbers in password
        print("You should add a number") #print "You should add a number"
        security -= 1 #subtracts one from the security

    if security < 0: #if the security is less than 0
        print("\nYour password is not secure") #print "Your password is not secure"
    else: #if the security is not less than 0
        print("Secure") #print "Secure"

def main(): #creats a main function
    websites = [] #creates an empty list for websites
    usernames = [] #creates an empty list for usernames
    passwords = [] #creates an empty list for passwords
    insert_wup(websites, usernames, passwords) #runs the insert_wup function for websites, usernames, passwords

    special_characters = list("!@#$%^&*()") #creates a list of special characters
    upper_case = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") #creates a list of uppercase letters
    lower_case = list("abcdefghijklmnopqrstuvwxyz") #creates a list of lowercase letters
    numbers = list("0123456789")#creates a list of numbers    

    while True: #creates an infinite loop
        mode = input('''\nDo you want to:  
    1.Enter a new password
    2.Print all of your websites, usernames, and passwords
    3.Access a previous website, username, and password
    4.Edit a previous password
    5.Create a generated password
    6.Check if password is secure
    7.Access the Google Sheets of passwords
    8.Exit program
        ''') #creates an input so that the user can choose a mode for their password

        if mode == "1": #if the user chooses mode 1
            print() #prints a space
            insert_wup(websites, usernames, passwords) #runs the function insert_wup for websites, usernames, and passwords
            print() #prints a space
       
        elif mode == "2": #if the user chooses mode 2
            for i in range(len(websites)): #goes through the index of websites
                print(f"\nWebsite: {websites[i]}, Username: {usernames[i]}, Password: {passwords[i]}") #prints every website and its username and password

        elif mode == "3": #if the user chooses mode 3
            while True: #creates an infinite loop
                which_password = input("\nWhich website's password would you like to access?") #creates a variable which asks the user which password they would like to access
                if which_password not in (websites): #if the website is not in the websites list
                    print("\nEnter a website that you have already entered!\n") #print "Enter a website that you have already entered!"
                else: #if the website is in the list of websites
                    i = websites.index(which_password) #find the index of the website
                    print(f"\nWebsite: {websites[i]}, Username: {usernames[i]}, Password: {passwords[i]}") #print the website and its username and password
                    break #breaks the infinite loop

        elif mode == "4": #if the user chooses mode 4
            while True: #creates an infinite loop
                web = input("\nWhich website's password would you like to change?") #creates a variable which asks the user which password they would like to change
                if web not in (websites): #if the website is not in websites
                    print("\nEnter a website that you have already entered!") #print "Enter a website that you have already entered!"
                else: #if the website is in the list of websites
                    while True: #creates an infinite loop
                        change_what = input("Do you want to change the username or password?") #creates a variable that asks the user if they want to change the username or password
                        if change_what == "username": #if the user inputs username
                            change_value(websites, usernames, "username", web)
                            break #breaks the infinite loop
                        elif change_what == "password": #if the user inputs password
                            change_value(websites, passwords, "password", web)
                            break #breaks the infinite loop
                        else: #if the user does not input username or password
                            print("\nChoose to change your username or password!") #print "Choose to change your username or password!"
                    break #breaks the infinite loop

        elif mode == "5": #if the user chooses mode 5
            generated_password = [] #creates a blank list for the final generated password
            length = 12 #sets the length of the password to 12
            for i in range(int(length/4)): #the generated password will 12 characters
                generated_password.append(random.choice(special_characters)) #randomly adds special characters to the generated_password list
                generated_password.append(random.choice(upper_case)) #randomly adds uppercase letters to the generated_password list
                generated_password.append(random.choice(lower_case)) #randomly adds lowercase letters to the generated_password list
                generated_password.append(random.choice(numbers)) #randomly adds numbers to the generated_password list
            random.shuffle(generated_password) #shuffles the randomly added characters
            generated_password = ''.join(generated_password) #joins each of the 12 characters
            print() #prints a space
            print(generated_password) #prints the generated_password
            print() #prints a space

        elif mode == "6": #if the user chooses mode 6
            check_password = str(input("\nEnter the password you would like to check the security of: ")) #asks the user to input the password they would like to check is secure or not
            print() #prints a space
            check_security(check_password) #runs check_security on the input check_password
            print() #prints a space

        elif mode == "7": #if the user chooses mode 7
            columns = {} #creates an empty list of columns for sheets
            columns['websites'] = websites #creates a column named websites
            columns['usernames'] = usernames #creates a column named usernames
            columns['passwords'] = passwords #creates a column named passwords
           
            rows = zip(columns['websites'],columns['usernames'], columns['passwords']) #groups the websites, usernames, and passwords in a list of tuples through its index
            with open('my_passwords.csv','w',newline='') as f: #create a new line to enter websites, usernames, and passwords
                writer = csv.writer(f) #inserts the websites, usernames, and passwords the user entered into a sheets document
                writer.writerow(['websites', 'usernames', 'passwords']) #write the website, username, and password into its designated column
                writer.writerows(rows) #writes the websites, usernames, and passwords into their designated rows
            file_path = (Path.cwd()) #finds the file in which the sheets is stored
            print(f'''
                Your file is stored in: {file_path}
                  ''') #print where the sheets file is stored
           
        elif mode == "8": #if the user chooses mode 6
            print("Then why are you here?\n") #prints "Then why are you here?"
            sys.exit() #fully exits the code

        else: #if the user does not enter a numbered mode
            print("Enter 1, 2, 3, 4, 5, 6, 7, or 8!") #prints "Enter 1, 2, 3, 4, 5, 6, 7, or 8!"

main() #runs the main function