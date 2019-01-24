"""
Hangman.

Authors: Aidan Moss, Guang Yang and James Kelley.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.
import random


def main():
    n, word, m, false = initialization()
    m = guessing(m, word, false)
    if m == 0:
        print("You lost. The secret word is ", end="")
        for x in word:
            print(x, end="")
        print()
    else:
        print("You won. Good job.")
    if input("Play another game?") == "n":
        quit("Thanks for playing!")
    else:
        main()


def initialization():
    n = int(input('Enter minimum word length:'))
    word = get_word(n)
    m = int(input('Number of segments'))
    false=[]
    for k in range(len(word)):
        false += ['-']

    return n, word, m,false


def get_word(n):
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
        item = []
    while len(item) < n:
        r = random.randrange(0,len(words))
        temp = words[r]
        for x in temp:
            item += [x]
    return item


def guessing(m, word, false):
    while m > 0:
        for x in false:
            print(x, end="")
        print()
        guess = input('Letter:')
        false, m = check(word,guess,false,m)
        print("You have ", m, " unsuccessful guesses left.")
        if false == word:
            break
    return m

def check(word,guess,false,m):
    temp = False
    for k in range(len(word)):
        if guess == word[k]:
            false[k] = guess
            temp = True
    if not temp:
        m -= 1
        print("Sorry, there are no ", guess, " letters in word.")
    return false, m


main()

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

