'''
Author: Kaia Novack
Date: 19 April 2024
Description: Is a code with a lot of different functions. It prints a song, adds two numbers, creates a list and checks if the element the user enters is in the list, either finds the difference, says if an input is an integer or not, or picks a random number within two numbers, prints a word backwords, prints a plaindrome backwards, and asks the user for their name and prints their initials. 
Bugs: n/a
Challenges: I had a few challenges when writing code for the challenges, but Ms. Marciano taught me the new concept, and I was able to figure it out.
Sources: n/a
'''


import random #brings in the random library

def chorus(): #creates a function with the chorus
    print ("Jingle bells, jingle bells, jingle all the way")#chorus line 1
    print ("O what fun it is to ride in a one horse open sleigh")#chorus line 2
def song():#creates a function with the whole song
    chorus()#includes the chorus function
    print("Dashing through the snow")#prints verse line 1
    print("In a one horse open sleigh")#prints verse line 2
    print("O'er the fields we go")#prints verse line 3
    print("Laughing all the way")#prints verse line 4
    print("Ha ha ha")#prints verse line 5
    print("Bells on bobtails sing")#prints verse line 6
    print("Making spirits bright")#prints verse line 7
    print("What fun it is to ride and sing")#prints verse line 8
    print("A sleighing song tonight")#prints verse line 9
    chorus()#includes the chorus function

    
def add(num1, num2):#creates a function to add two numbers
    print(num1+num2)#prints number 1+2


def print_elements(list_to_print):#creates a list to print
    for element in list_to_print: #for an element in the list
        print (element) #print the elements


def contains_element(my_list, element): #creates a function that checks if the letter is in the list
    if element in my_list: #if the letter is in the list
        return True #returns true
    else: #if the letter is not in the list
        return False #returns false


def difference(num1, num2): #creates a function to find the difference between two numbers
    print(num2-num1)#prints number 1 minus number 2

    
def is_integer(string):#creates a function that intakes a string and says if it is a string or integer
    if "-" in string:#if a negative starts the string
        string = string[1:]#a string is any number 1 and up
    if string.isnumeric():#if the string is a number (can be negative)
        return True #returns true
    else: #if the string is not a number
        return False #returns false

    
def get_integer(order):#creates a function to randomly choose a number
    while True:#creates an infinite loop
        number = input(f"Enter your {order} integer: ")#asks the user to input their first and second number
        try:#checks if the user input a number before continuing
            number = int(number)#checks if the user input a number
            return number#stores the number
        except ValueError:#if the user did not input a number
            print("That is not a number!")#prints That is not a number!

            
def pick_integer():#creates a function for the computer to pick an integer
    num1 = get_integer("lower boundary")#asks the user to input an integer
    num2 = get_integer("upper boundary")#asks the user to input an integer
    if num1 < num2:#if num1 is less than num2
        print(random.randint(num1, num2)) #print a random integer that has been input
    elif num1 > num2: #if the second number is greater than the first number
        print(random.randint(num2, num1)) #switch the numbers around and print a random integer that has been input

        
def switch_letters(word, character1, character2):#creates a function to switch letters in a word
    new_word = ""#creates a space for a word
    for letter in word: #for every letter in a word
        if letter == character1: #if the letter is l
            new_word += character2 #switch it with w
        else: #if the letter is not l
            new_word += letter #copies the word down letter by letter
    return new_word #returns the word with switched leters


def reverse_string(string):#creates a function to reverse a word
    return string[::-1]#returns the word reversed
def is_palindrome(string):#creates a function to see if a word is a palindrome
    return string == reverse_string(string)#returns the palindrome


def return_initials(name):#creates a function to return initials
        name = name.split(" ")#creates a list with the name the user enters
        initials = ""#creates a list to intake initials
        for initial in name:#for the first initial in every name
            initials += initial[0]#add the initial to the initials list
        return initials#returns the initials list


def main():#creates a main function
    song()#prints the song
    num1 = get_integer("first")#calls get_integer to ask for a first number
    num2 = get_integer("second")#calss get_integer to ask for a second number
    add(num1, num2)#adds the numbers the user put in
    my_list= ["a", "b", "c"] #creates a list
    print_elements(my_list)#prints the list a,b,c
    element = input("Enter a string: ")#asks the user to input a letter
    print(contains_element(my_list, element))#print the function contains_element
    while True: #creates an infinite loop
        action = input("What would you like to do: 1. Find a difference or 2. Check if a string is an integer 3. Choose between two integers")#asks the user to choose an option
        if action == "1": #if the user chooses 1
            n1 = int(input("Enter number 1: "))#asks the user to input a number
            n2 = int(input("Enter number 2: "))#asks the user to input a number
            difference(n1, n2)#use the difference function
        elif action == "2":#if the user chooses 2
            string = input("Enter string: ")#asks the user to enter a string
            print (is_integer(string))#see if the string is an integer
        elif action == "3":#if the user chooses 3
            pick_integer()#runs pick_integer
        break#breaks the infinite loop
    print(switch_letters("hello", "l", "w"))#runs switch letters on hello
    print(reverse_string("Hello"))#reverse hello
    print(is_palindrome("racecar"))#reverse racecar
    name = input("Enter your name: ")#asks the user to input their name
    print (return_initials(name))#calls return_initials and executes it with the name the user enters
main()#calls the main function
