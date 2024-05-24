import random #import random library
sizes = ["appetizer", "entree", "side"]#creates a list of different sized dishes
sizes_prices = [10, 20, 8]#sets the prices for the different sizes using a parrallel array
dishes = ["cauliflower", "tilapia fillet", "pork loin", "green beans", "rainbow carrots", "potatoes", "three color squash", "eggplant", "eye round of beef", "baguette"] #creates a list of dishes
dish_insult = ["cauliflower is gross!", "awful choice", "ewwww, why would you eat prok loin", "green beans are disgusting", "why do you want carrots? ewwwwww", "ewwww potatoes!", "squash is nasty", "why would you eat eggplant!", "what made you decide to eat an eye of round beef", "baguettes are disgusting"]#creates a list of insults for the dishes
flairs = ["with balsamico", "with garlic and olive oil", "with minted yogurt", "soup", "chutney", "salad", "with salsa", "over sticky rice", "au jus", "with basmati rice"] #creates a list of sides
flair_insult = ["adding balsamic doesn't make it better", "garlic and olive oil makes food worse", "what even is minted yogurt?", "why soup?", "I've never heard of chutney. I bet it's disgusting", "salads are too basic", "salsa doesn't even go with your dish","why do you want your rice sticky?", "is au jus a made up food?", "basmati rice is disgusting"]#creates a list of insults for the sides

while True:#creates an infinite loop
    try:#tries the next piece of code so that if it does not work, there is not an error
        num_items = int(input("Hello! How many dishes would you like?"))#defines num_items and asks how many dishes the user would like
        break#breakes the infinite loop
    except ValueError:#if there is a ValueError from the try
        print("Please enter an integer!")#print "Please enter an integer!"

total_cost = 0#starts the total cost at 0
used = []#creates a used list starting with none

for i in range(num_items): #for the number of items the user chooses
    size = random.choice(sizes)#chooses a random size for the dish
    flair = random.choice(flairs)#defines side as a random side for later code

    while True:#creates an infinite loop
        dish = random.choice(dishes)#defines dish as a random dish for later code

        if dish not in used:#if the dish has not been used
            used.append(dish)#add to the used list
            break#break the infinite loop
    print(f"{dish} {flair}")#print that amount of dishes with sides the user chose
    print(f"{dish_insult[dishes.index(dish)]} {flair_insult[flairs.index(flair)]}")#prints an insult for the same index of dishes and sides.
    print (f"Your cost for this item is ${sizes_prices[sizes.index(size)]}\n")#uses the parrallel array to find if the dish is an appetizer, entree, or side and sets the price
    total_cost += sizes_prices[sizes.index(size)]#adds all of the costs to produce a total cost

print (f"Your total cost is ${total_cost}\n")#prints the total cost for the meal

       
    
