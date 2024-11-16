# importing the choice module
from random import choice
# importing to gain operating system access
import os
# importing a vanishing man instance
from hangingMan import VanishingMan

# List of words to randomly choose from
WORDS = ['PYTHON', 'PROGRAMMING', 'COMPUTER', 'ALGORITHM', 'DATABASE', 'NETWORK', 
         'DEVELOPER', 'SOFTWARE', 'CODING', 'DEBUGGING', 'FUNCTION', 'VARIABLE']

# The class Player is the user functionality that uses the VanishingMan class
class Player(object):
    
    # The method that creates a game session of the Vanishing Man
    def __init__(self):
        self.username = ""

        # Total games played by the user
        self.total_games = 0

        # Pass or fail games count
        self.passed = 0
        self.failed = 0
        
        # Words that the player failed or not to guess
        self.guessed_words = []
        self.missed_words = []

    # clear_screen Method that clears the console screen
    def clear_screen(self):
      os.system('cls' if os.name == 'nt' else 'clear')
    
    # The get_player_name method ask user for the player name
    # with input validation
    def get_player_name(self):
        # We continue to ask for a player name until name is valid
        while True:
            # strip removes any leading and trailing whitespaces from the inputted name
            name = input("Welcome! Please enter your name to begin: ").strip()

            # Check if name entered is valid
            try:
                if name:
                    self.username = name
                    print("Welcome to Vanish Man, " + self.username)
                    return
                else:
                    print("Please enter a valid name here: ")
            except ValueError:
                print("Name cannot be empty. Please try again.")
                print("Please enter a valid name here: ")

    # The play_game method that starts a game session
     # Main game logic
    def play_game(self):
      # Select a random word
      word = choice(WORDS)
      
      # Sets a data collection of the word letters
      word_letters = set(word)

      # Creates a data collection of the alphabet
      alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

      # Creates an empty set of used letters
      used_letters = set()

      # Number of opportunities for the player to guess
      tries = 6
      # Sets an instance of the Vanishing Man
      vanishing_man = VanishingMan()
      
      # Game loop
      while tries > 0 and len(word_letters) > 0:
          # Clear previous screen state to display next state
          self.clear_screen()

          print(f"\nPlayer: {self.username}")
          print("\nYou have", tries, "tries left.")
          print("\nUsed letters:", ' '.join(sorted(used_letters)))
          
          # Display current word state
          word_list = [letter if letter in used_letters else '_' for letter in word]
          print("\nCurrent word:", ' '.join(word_list))
          print(vanishing_man.display_vanish_man(tries))
          
          # Get player input
          guess = input("\nGuess a letter or the full word: ").upper()
          # guess is the full word
          if guess == word:
            print("\nAMAZING GUESS!")
            # empty the entire set and claim the win
            word_letters.clear()

          # Is guess in alphabet and not in used_letters:
          elif guess in alphabet - used_letters:
              # Add guess letter to the used letter collection
              used_letters.add(guess)
              # Is the guess letter in the word letter collection
              if guess in word_letters:
                  # Remove the letter from the collection
                  word_letters.remove(guess)
                  print("\nGood guess!")
              # subtract 1 player try if guess letter not in word_letters
              else:
                  tries -= 1
                  print(f"\nSorry, '{guess}' is not in the word.")
          # Is the guess letter in the used letters collection
          elif guess in used_letters:
              print("\nYou already used that letter. Try again!")
          # guess letter not in the used letters collection
          else:
              print("\nInvalid character. Please enter a letter.")
          # Press Enter to move to the next step
          input("\nPress Enter to continue...")
      
      # Game end
      # Clear last screen state to display last Vanishing man state
      self.clear_screen()

      # Displays the last state of the hanging man
      print(vanishing_man.display_vanish_man(tries))
      # Increment the total of games count by 1
      self.total_games += 1
      # If the player ran out of tries
      if tries == 0:
          # Add the word failed to guess to the missed word list
          self.missed_words.append(word)
          # Increment the failed games count by 1
          self.failed +=1
          print(f"\nSorry {self.username}, you lost! The word was {word}")
      else:
          # Add the guessed word to the guessed word list
          self.guessed_words.append(word)
          # Increment the passed games count by 1
          self.passed +=1
          print(f"\nCongratulations {self.username}! You won! The word was {word}")

            