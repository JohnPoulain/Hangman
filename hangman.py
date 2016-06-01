#constants
HANGMAN = ("__________    ",
           "|         |   ",
           "|         0   ",
           "|        /|\  ",
           "|        / \  ",
           "|             ",
           "|____________ ")

hangman_words = open("07hangman_words.txt", "r")
messy_list = hangman_words.readlines()
WORDS = [elem.strip() for elem in messy_list]
hangman_words.close()

incorrect = []
wrong = 0 #number of incorrect guesses

#main
import random
correct = random.choice(WORDS)
correct = correct.lower()

#to generate a string of underscores as long as the word
sofar = ""
for i in range(len(correct)):
    sofar += "_"

print ("\t\tWelcome to Hangman")
print ("\nYou already know how to play")

while wrong < 7:                    #7 is the number of mistakes you can make
    if sofar.lower() == correct.lower():
        print ("well done the word was ", sofar)
        input ("press enter to exit")
        exit()
        #victory condition
    #shows your status
    print ("so far you have: ", sofar, "and your incorrect guesses are: ", incorrect)
    guess = input("guess a letter ")
    #checks first to see if you already go that letter wrong
    if guess.lower() in incorrect:
        print ("You already guessed ", guess, end = "\n")
    #if the guess is right
    elif guess.lower() in correct:                #for when the guess is right
        print ("yes", guess, "is in the word \n")
        #adds the correct letter to the guesses so far
        new = ""
        for i in range(len(correct)):
            if guess.lower() == correct[i]:
                new += guess
            else:
                new += sofar[i]
        sofar = new
    #if the guess is wrong
    else:
        print ("no ", guess, "is not in the word")
        incorrect.append(guess)
        wrong += 1
        incorrect.sort()
    #prints the slice of the HANGMAN depending on how many incorrect guesses you've made
    if wrong > 0:
        print ("\n", "\n".join(HANGMAN[0:wrong]), "\n")

print ("\t\tGAME OVER")
print ("\tthe correct word was ", correct)
input ("press enter to exit")
