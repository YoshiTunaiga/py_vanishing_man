# This program allows a user to play a Vanishing Man game where
# the player has to guess a hidden word
# if the player rans out of tries, the player loses the current game session
# if the player wants to play again, the program will start a new session
# The purpose of the program is to display the hanging man as the player guesses the word

from player import Player

# Importing the datetime to get the current date and time
from datetime import datetime
# Importing the time module to use the sleep function
import time

# This function will start a session for the new player
def play(curr_player):
    # Loops through the number of games the curr_player would like to play
    while True:
        curr_player.play_game()
        # Checks if the player wants to start another game session
        if input("\nReady to play again? (Y/N): ").upper() != 'Y':
            # Record stat results to the playerResults text file
            display_results(curr_player)
            break

    
    print(f"\nThanks for playing, {curr_player.username}! Goodbye!")

# For every full game completed, this function will log the score with a timestamp
def display_results(final_player):
    file = open("playerResults.txt", 'a')

    # Create a game time stamp
    today_date = datetime.now()
    time_stamp_str = today_date.strftime("%m/%d/%Y %H:%M:%S")

    # Writing to the player results file
    file.write("\n================================================\n" )
    file.write("\nPlayer: " + final_player.username + " Timestamp: " + time_stamp_str )
    file.write("\nGuessed Words: " + ', '.join(final_player.guessed_words))
    file.write("\nMissed Words: " + ', '.join(final_player.missed_words))
    word_percentage = (final_player.passed/final_player.total_games) * 100
    file.write("\nThe guessed word percentage was: " + str(int(word_percentage)) + "%\n")

    # Ensure to close the file after changes were made
    file.close()

def main():
    print("Let's play a Vanish Man game")


    new_player = Player()
    new_player.get_player_name()

    # A delay of prints that provides excitement to the user before the screen brings the game up
    time.sleep(1)
    print("...Ready")
    time.sleep(1)
    print("\n...Set")
    time.sleep(1)
    print("\n...Go!")
    time.sleep(1)

    # Starts the game
    play(new_player)

if __name__ == "__main__":
    main()