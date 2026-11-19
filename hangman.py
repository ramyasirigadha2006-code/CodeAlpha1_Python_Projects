Python 3.14.10 (tags/v3.14.10:b703b2c, Oct 25 2026, 17:36:52) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import random

... words = ["apple", "mango", "banana", "orange", "grapes"]
... 
... word = random.choice(words)
... guessed = []
... chances = 6
... 
... print("Welcome to Hangman Game!")
... 
... while chances > 0:
...     display = ""
... 
...     for letter in word:
...         if letter in guessed:
...             display += letter + " "
...         else:
...             display += "_ "
... 
...     print("\nWord:", display)
... 
...     if all(letter in guessed for letter in word):
...         print("Congratulations! You won!")
...         break
... 
...     guess = input("Guess a letter: ").lower()
... 
...     if len(guess) != 1 or not guess.isalpha():
...         print("Enter one letter only.")
...         continue
... 
...     if guess in guessed:
...         print("You already tried this letter!")
...         continue
... 
...     guessed.append(guess)
... 
...     if guess in word:
...         print("Good guess!")
...     else:
...         chances -= 1
...         print("Wrong guess! Chances left:", chances)

if chances == 0:
    print("Game over! The word was:", word)

