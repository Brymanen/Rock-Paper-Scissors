class Settings():
	def __init__(self):
		self.background_color = (255, 255, 255)
		
		# Store the greeting message
		self.greeting_message = f"Let's play rock, paper, scissors! "
		self.greeting_message += "Press the key r for rock, p for paper and s for scissors. Press q to end to end the game."

		# Messages explaining the user input
		self.text_game_number = "This is game number: "
		self.text_user_picked = "You picked: "
		self.text_computer_picked = "The computer picked: "

		# Messages explaining the end of the game
		self.text_result = {
			0: "The game ended in a draw!",
			1: "You won the game!",
			2: "You lost the game!"
		}

		#settings for the display of the messages
		self.pos_x_spacing = 1/25
		self.pos_y_spacing = 1/75
		self.pos_y_spacing_top = 1/200
		self.font_color = (0, 0, 0)
		self.pos_y_spacing_between_games = 1/150
		self.screen_bottom_cutoff = 0.9

		# Mapping the choices of rock, paper, scissors to numbers in a dictionary
		self.rock_paper_scissors_mapping = {
			0: "rock",
			1: "paper",
			2: "scissors"
		}

