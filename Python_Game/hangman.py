import random

hangman_parts = [

        """
        
        
        
        
        
        
        
        """
        ,
        """
         
         
         
         
         
         
          -
        """
        ,
        """
         
             
         
         
         
         
         --
        """
        ,
        """
         
             
         
         
         
         
        ---
        """
        ,
        """
         
             
         
         
         
         |
        ---
        """
        ,
        """
         
             
         
         
         |
         |
        ---
        """
        ,
        """
         
        
         
         |
         |
         |
        ---
        """
        ,
        """
         
             
         |
         |
         |
         |
        ---
        """
        ,
        """
         
         |    
         |
         |
         |
         |
        ---
        """
        ,
        """
         -
         |    
         |
         |
         |
         |
        ---
        """
        ,
        """
         --
         |    
         |
         |
         |
         |
        ---
        """
        ,
        """
         ---
         |    
         |
         |
         |
         |
        ---
        """
        ,
        """
         ----
         |    
         |
         |
         |
         |
        ---
        """
        ,
        """
         -----
         |    
         |
         |
         |
         |
        ---
        """
        ,
        """
         ------
         |    
         |
         |
         |
         |
        ---
        """
        ,
        """
         ------
         |    |
         |
         |
         |
         |
        ---
        """
        ,
        """
         ------
         |    |
         |    O
         |
         |
         |
         |
        ---
        """
        ,
        """
         ------
         |    |
         |    O
         |    |
         |
         |
         |
        ---
        """
        ,
        """
         ------
         |    |
         |    O
         |   /|
         |
         |
         |
        ---
        """
        ,
        """
         ------
         |    |
         |    O
         |   /|\
         |
         |
         |
        ---
        """
        ,
        """
         ------
         |    |
         |    O
         |   /|\
         |   /
         |
         |
        ---
        """
        ,
        """
         ------
         |    |
         |    O
         |   /|\
         |   / \
         |
         |
        ---
        """
    ]

def load_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

dictionary = load_words_from_file('dictionary.txt')

def choose_word():
    return random.choice(dictionary)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters or letter == '-':
            display += letter
        else:
            display += '_'
    return display

def display_hangman(incorrect_guesses):
        print(hangman_parts[incorrect_guesses])

def hangman():
    print("Welcome to Hangman!")

    try:
        input_function = raw_input
    except NameError:
        input_function = input

    secret_word = choose_word()

    guessed_letters = []
    incorrect_guesses = 0

    while incorrect_guesses < len(hangman_parts):
        print("Secret Word:", display_word(secret_word, guessed_letters))
        display_hangman(incorrect_guesses)

        if display_word(secret_word, guessed_letters) == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input_function("Enter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess. Try again.")
                guessed_letters.append(guess)
                incorrect_guesses += 1
        else:
            print("Invalid input. Please enter a single letter.")

    if incorrect_guesses == len(hangman_parts) - 1:
        print("Sorry, you ran out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    hangman()
