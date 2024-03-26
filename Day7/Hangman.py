import random
import hangman_art
import hangman_words

# Variables
word_list = hangman_words.word_list
display_list = []
lives = 6
# Select a random word
chosen_word = random.choice(word_list)
# Create a blank slot in display list for each letter in chosen word
for letter in chosen_word:
    display_list.append("_")
# Display logo
print(hangman_art.logo)



# Prompt user, check letters and replace blank letters/update art in display if correct
while "_" in display_list and lives > 0:
    success = False
    # Display art and blank word
    print(hangman_art.stages[lives])
    print(f"{" ".join(display_list)}\n")
    # Prompt user
    chosen_letter = input("Guess a letter: ").lower()
    # Clear the console after every guess
    print("\033c", end="", flush=True)
    # Check if letter has already been chosen
    if chosen_letter in display_list:
        print("You have already chosen this letter!")
    else:
        # Check each letter in the chosen word and replace in the display list if correct
        for pos in range(len(chosen_word)):
            letter = chosen_word[pos]
            if chosen_letter == letter:
                display_list[pos] = chosen_letter
                success = True
        
        #  Fail or succeed
        if success == False:
            lives -= 1
            print(f"{chosen_letter} was incorrect! {lives} lives remaining!")    
        else:
            print(f"{chosen_letter} was correct!")
        
# Win or lose
if lives > 0:
    print(f"{" ".join(display_list)}\n")
    print("You win!")
else:
    print(hangman_art.stages[lives])
    print("You lose!")