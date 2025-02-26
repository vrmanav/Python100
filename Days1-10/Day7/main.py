words = ["circumstance", "show", "secure", "fade", "squash"]
import random
from os import system

chosen_word = random.choice(words)
word_len = len(chosen_word)
display = []
lives = 5
game_is_on = True
for letter in chosen_word:
    display.append(" _ ")

system("clear")
print("💀 WELCOME TO HANGMAN GAME 💀\n")
print(chosen_word)

while game_is_on:
    print("".join(display))
    user_guess = input("Make your guess:\n")

    for letter in range(word_len):
        if user_guess == chosen_word[letter]:
            display[letter] = user_guess

        if " _ " not in display:
            game_is_on = False
            print("🎉 YOU WIN 🎉")

    if user_guess not in chosen_word:
        lives -= 1
        print(f"\n⛔️ You made an incorrect guess! You have {lives} lives remaining ⛔️\n")

    if lives == 0:
        game_is_on = False
        print("YOU LOSE 🙁")
