class Settings():
	"""A class to store all settings for rock paper scissors."""
	def __init__(self):
		"""Initialize the game's settings."""
		self.background_color = (255, 255, 255)
		
		# Store the greeting message.
		self.greeting_message = (
			f"Let's play rock, paper, scissors! "
		 	f"Press the key r for rock, p for paper and s for scissors. "
		 	f"Press q to end to end the game."
		 	)

		# Messages explaining the user input.
		self.text_game_number = "This is game number: "
		self.text_user_picked = "You picked: "
		self.text_computer_picked = "The computer picked: "

		# Messages explaining the end of the game.
		self.text_result = {
			0: "The game ended in a draw!",
			1: "You won the game!",
			2: "You lost the game!"
			}

		# Settings regarding the display of the messages.
		self.font_color = (0, 0, 0)
		self.pos_x_spacing = 1/25
		self.pos_y_spacing = 1/75
		self.pos_y_spacing_between_games = 1/150
		self.screen_bottom_cutoff = 0.9

		# Mapping the choices of rock, paper, scissors to numbers in a 
		# dictionary.
		self.rock_paper_scissors_mapping = {
			0: "rock",
			1: "paper",
			2: "scissors"
			}

		# Storing the text for the messages regarding to the scoreboard
		self.text_scoreboard_draw = "Draws: "
		self.text_scoreboard_won_games = "Won games: " 
		self.text_scoreboard_lost_games = "Lost games: "

		# Parameters to adjust the x and y coordinates of the scoreboard
		self.scoreboard_x = 1/2
		self.scoreboard_y = 1/3
		self.scoreboard_y_spacing = 1/25

