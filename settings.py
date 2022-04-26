class Settings():
	def __init__(self):
		self.background_color = (255, 255, 255)
		
		# Store the greeting message
		self.greeting_message = f"Let's play a game of rock paper scissors! "
		self.greeting_message += "Press the key r for rock, p for paper and s for scissors."

		# Messages explaining the user input
		self.text_game_number = "This is game number: "
		self.text_user_picked = "The user picked: "
		self.text_computer_picked = "The computer picked: "

		# Messages explaining the end of the game
		self.text_draw = "The game ended in a draw!"
		self.text_player_won = "You won the game!"
		self.text_computer_won = "You lost the game!"

		#settings for the display of the messages
		self.pos_x_spacing = 1/36
		self.pos_y_spacing = 1/20
		self.pos_y_spacing_top = 1/100
		self.font_color = (0, 0, 0)

		# Mapping the choices of rock, paper, scissors to numbers in a dictionary
		self.rock_paper_scissors_mapping = {
		0: "rock",
		1: "paper",
		2: "scissors"
		}

