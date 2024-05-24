import random
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
       ===''', '''
   +---+
   O   |
   |   |
       |
       ===''', '''
  +---+
  O   |
 /|   |
      |
      ===''', '''
  +---+
  O   |
 /|\  |
      |
      ===''', '''
  +---+
  O   |
 /|\  |
 /    |
      ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
      ===''']
words = ['hello','world', 'python', 'best', 'worst', 'awesome', 'supercalifragilisticexpialidocious', 'hola', 'charger', 'cards', 'country', 'pencil', 'phone', 'sweater', 'building', 'clock', 'home', 'wonderful', 'classroom', 'window', 'panda', 'dolphin', 'monkey', 'flashlight', 'firework', 'summer', 'winter', 'spring', 'fall', 'hello world', 'green']
secret = random.choice(words)

secret_list = list(secret)
hidden = []
guesses = 0
max_guesses = 5

for character in secret_list:
    if character == '  ':
        hidden.append('  ')
    hidden.append('_ ')

print(''.join(hidden))

while '_ ' in hidden and guesses < len(HANGMAN_PICS):
    print(HANGMAN_PICS[guesses])
    

    while True:
        guess = input('Enter a letter:')

        if guess not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            print('Enter a letter please!')
        else:
            break

    if guess in secret_list:
        for index in range(len(secret_list)):
            if guess == secret_list[index]:
                hidden[index] = guess
        print(''.join(hidden))
    else:
        print('Letter not here!')
        guesses += 1

    
