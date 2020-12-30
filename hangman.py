import random
print("H A N G M A N")

while True:
    choice = input('Type "play" to play the game, "exit" to quit:')
    if choice == "play":
        break
    elif choice == "exit":
        os.kill()
    else:
        True

created_name = random.choice(['python', 'java', 'kotlin', 'javascript'])
guessed_name = len(created_name) * "-"
created_name = list(created_name)
guessed_name_list = list(guessed_name)
guessed_letters_set = set()

counter = 0

while counter < 8:

    found = False
    print("")
    print(guessed_name)
    letter = input("Input a letter: ")#can be more letters
    
    for i in range(len(created_name)):
        if created_name[i] == letter and "-" == guessed_name_list[i]:
            guessed_name_list[i] = created_name[i]
            found = True
    if found != True:
        if len(letter) != 1:
            print("You should input a single letter")
        elif letter.islower() == False:
            print("Please enter a lowercase English letter")
        elif letter in guessed_letters_set:
            print("You've already guessed this letter")
        else:
            print("That letter doesn't appear in the word")
            counter += 1

    guessed_letters_set.add(letter)
    guessed_name = "".join(guessed_name_list)
    
    if guessed_name == "".join(created_name):
        break    

if guessed_name == "".join(created_name):
    print("You guessed the word!")
    print("You survived!")
else:
    print("You lost!")
