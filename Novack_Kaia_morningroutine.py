print ("Alarm!")

while True:
    snooze = str.lower(input("Do you want to snooze?"))
    
    if(snooze == 'yes'):
        print("Sleep for 10 more minutes")
    elif(snooze == 'no'):
        print("Wake up")
        break
    else:
        print("invalid response")

while True:
    shower = str.lower(input("Do you want to shower?"))

    if(shower == 'yes'):
        print("Get in the shower")    

        while True:
            music = str.lower(input("Do you want to listen to music?"))

            if(music == 'yes'):
                print("Awesome!")

                type_of_music = str.lower(input("What type of music would you like to listen to?"))

                if(type_of_music == "taylor swift"):
                    print ("She's my favorite!")
                elif(type_of_music == "olivia rodrigo"):
                    print ("I love her music!")
                else:
                    print("I love that music!")
                break

            elif(music == 'no'):
                print("Lame")
                break
            else:
                print("invalid answer")
        break
    elif(shower == 'no'):
        break
    else:
        print("invalid response")

while True:
    get_ready = str.lower(input("Do you want to get ready?"))

    if(get_ready == 'yes'):
        break
    elif(get_ready == 'no'):
        print("Go get ready!")
    else:
        print("invalid response")
        

if shower == "yes":
    print("Do hair your hair routine")

while True:
    brush_your_teeth = str.lower(input ("Do you want to brush your teeth?"))

    if(brush_your_teeth == 'yes'):
        print("Pack your bag and you are all good to go")
        break
    elif(brush_your_teeth == 'no'):
        print("Go brush your teeth!!!!")
    else:
        print("invalid answer")
        
print ("Have a good day!")
