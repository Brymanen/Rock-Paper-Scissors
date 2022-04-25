class Settings():
	def __init__(self):
		self.background_color = (255, 255, 255)
		
		# Store the different message that will be displayed to the user
		self.greeting_message = f"Let's play a game of rock paper scissors! "
		self.greeting_message += "Press the key r for rock, p for paper and s for scissors.\n"
		self.message_draw = "The game ended in a draw!"
		self.message_player_won = "You won the game!"
		self.message_computer_won = "You lost the game!"

		#settings for the display of the messages
		self.pos_x_spacing = 1/36
		self.pos_y_spacing = 1/36
		self.pos_y_spacing_top = 1/100
		self.font_color = (0, 0, 0)
