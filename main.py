import hangman_art
import random
import hangman_words
import os


print(hangman_art.logo)


chosen_word = random.choice(hangman_words.word_list)
#print(f'Pssst, the solution is {chosen_word}.')

display = []
display = ["_" for _ in range(len(chosen_word))]
print(f"Your guess so far: {' '.join(display)}\n")
lives = 6
print(hangman_art.stages[lives])


while lives > 0 and "_" in display:
  guess = input("Guess a letter: ").lower()
  os.system('cls')
  print(hangman_art.logo)
  NOTUGCU = chosen_word.count(guess)
  if display.count(guess) > 0:
    print("You already picked this letter. Pick something else\n")
  elif NOTUGCU > 0:
    id = -1
    i = 0
    while i < NOTUGCU:
      id = chosen_word.index(guess, id+1)
      display[id] = chosen_word[id]
      i+=1
    print(hangman_art.stages[lives])
    print(f"Your guess so far: {' '.join(display)}.\n\n")
  else:
    lives -= 1
    print(hangman_art.stages[lives])
    print(f"Your guess so far: {' '.join(display)}.\n\n")
    print(f"The letter you picked is not in the word.\nYou have {6-lives} strikes and {lives} more chances\n\n")


if display.count("_") == 0 or "_" not in display:
  print("You guessed all the letters correctly.\nYou win!!! 🏆")
elif lives == 0:
  print(f"You are out of lives. You lose 👎.\nThe word is '{chosen_word}'")
  
