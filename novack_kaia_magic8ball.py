import random #brings in the random library for use of random functions

eightball = ['yes', 'maybe', 'no', 'all signs point to yes', 'it is decidedly so', 'without a doubt' 'yes definitely', 'you may rely on it', 'ask again later', 'better not tell you now', 'cannot predict now', 'concentrate and ask again', 'my reply is no', 'my sources say no', 'outlook not so good', 'very doubtful']#creates a list with answers a magic eight ball will give
words = ['how', 'why', 'is', 'who', 'what', 'where', 'when', 'are', 'will']#creates a list with question words

while True: #an infinite loop (while condition True is true)
    ball = str.lower(input("Enter your question: (say stop to end and make sure to add a question mark to your question)"))#prompts the user to enter a question

    if (ball == 'stop'):#if the user says 'stop'
        print ('bye')#displays the message 'bye'
        break#manually breaks the while true loop
    elif ('?' in ball or any(word in ball for word in words)):#otherwise if the user does not say stop or if there is a word in the question that is in the list words
        print(random.choice(eightball))#displays one of the elements in the list randomly
    else:#if the user does not say stop and the answer does not contain a question mark
        print('that is not a question')#displays the message 'that is not a question'
