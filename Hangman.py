
# Hangman

import random as rnd
import numpy as np
import time

#reading file
words_file = open("words.txt","r", encoding = "utf-8")
words_list = words_file.read()
words = words_list.split(",")

#chosing random word
range = len(words)
word = rnd.choice(words)

#intro for game
print("""
    Welcome to Hangman!

    Gallow is empty.

    Play to keep him alive.
""")
gallow = (
    """
        |
        |      
        |     
        |
        |
       /|
      / |
   -----------
    """
)
time.sleep(0.5)
print(gallow)

#printing word len by using "—"
wordsign_0 = "— " * len(word)
wordsign_1 = wordsign_0.split(" ")
wordsign_1 = wordsign_1[0:-1]
wordsign_1 = list(wordsign_1)
time.sleep(0.5)
print(wordsign_0 + "\n")

#lives
lives = 7

#dict of gallow
hangman = {7: """
        |
        |      
        |     
        |
        |
       /|
      / |
   -----------
    """,
    6: """
        -------
        |
        |      
        |     
        |
        |
       /|
      / |
   -----------
    """,
    5: """
        -------
        |     |
        |      
        |     
        |
        |
       /|
      / |
   -----------
    """,
    4: """
        -------
        |     |
        |    ( ) 
        |     
        |
        |
       /|
      / |
   -----------
    """,
    3: """
        -------
        |     |
        |    ( ) 
        |     | 
        |
        |
       /|
      / |
   -----------
    """,
    2: """
        -------
        |     |
        |    ( ) 
        |   / | \\
        |     
        |    
       /|
      / |
   -----------
    """,
    1: """
        -------
        |     |
        |    ( ) 
        |   / | \\
        |     |
        |    
       /|
      / |
   -----------
    """,
    0: """
        -------
        |     |
        |    ( ) 
        |   / | \\
        |     |
        |    / \\
       /|
      / |
   -----------
    """}

#main game
word_2 = word
word = list(word)
word_display = " ".join(word)
word_display = list(word_display)
time.sleep(0.5)
print("You have", lives, "lives." + "\n")
time.sleep(0.5)
word_guess = str(input("Please make your letter guess: "))

while True:
    #her seferinde yenilenmesi için
    values = np.array(word)
    searchval = word_guess
    ii = np.where(values == searchval)[0]
    indexs = len(ii)
    display = " ".join(wordsign_1)

    #if there is just one letter
    if indexs == 1:
        location = word.index(word_guess)
        wordsign_1[location] = word_guess
        time.sleep(0.5)
        print("Good job, you found one." + "\n")
        display = " ".join(wordsign_1)
        print(hangman[lives])
        print(display)
        if "—" not in display:
            time.sleep(0.5)
            print(hangman[lives] + "\n" + "You won.")
            break
        time.sleep(0.5)
        word_guess = str(input("Please make another letter guess: " + "\n"))
        display = list(display)


    # winning

    #if there is more than one letter
    elif indexs > 1:
        counter = 0
        while True:
            wordsign_1[ii[counter]] = word_guess
            counter += 1
            if counter == indexs:
                break
        time.sleep(0.5)
        print("Good job, you found one." + "\n")
        display = " ".join(wordsign_1)
        print(hangman[lives])
        print(display)
        if "—" not in display:
            time.sleep(0.5)
            print(hangman[lives] + "\n" + "You won.")
            break
        time.sleep(0.5)
        word_guess = str(input("Please make another letter guess: " + "\n"))
        display = list(display)


    elif indexs == 0:
        lives -= 1
        time.sleep(0.5)
        print("There is no", word_guess, "in the word. Sorry :(" + "\n" + "Try again." + "\n")
        time.sleep(0.5)
        print("Remaining lives:", lives, "\n")
        display = " ".join(wordsign_1)
        print(hangman[lives])
        print(display)
        if "—" not in display:
            time.sleep(0.5)
            print(hangman[lives] + "\n" + "You won.")
            break
        time.sleep(0.5)
        word_guess = str(input("Please make your letter guess again: " + "\n"))
        display = list(display)


    # game over situation
    if lives == 1:
        time.sleep(0.5)
        print("Remaining lives: 0", "\n")
        time.sleep(0.5)
        print("Word is:", word_2)
        print(hangman[0] + "\n" + "You lost :)")
        break


