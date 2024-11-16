# The class will implement a hanging man type of image
class VanishingMan:

  # The init method is used to create a new instance of the hanging man
  def __init__(self):
    self.stages = [
        # Final state: completely vanished
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        ___|___
        """,
        # 1 try left
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        ___|___
        """,
        # 2 player_tries left
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
        ___|___
        """,
        # 3 player_tries left
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
        ___|___
        """,
        # 4 player_tries left
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
        ___|___
        """,
        # 5 player_tries left
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |     
        ___|___
        """,
        # 6 player_tries left (starting state)
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
        ___|___
        """
    ]

# The method will display the vanish man based on remaining player_tries number
  def display_vanish_man(self,player_tries):
    return self.stages[player_tries]

  
