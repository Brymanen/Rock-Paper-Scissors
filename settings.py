class Settings():
	def __init__(self):
		self.background_color = (255, 255, 255)
		
		# Store the greeting message that will be shown at the start of the game
		self.greeting_message = f"Let's play a game of rock paper scissors! "
		self.greeting_message += "Press the key r for rock, p for paper and s for scissors.\n"

		#settings for the display of the messages
		self.pos_x_spacing = 1/36
		self.pos_y_spacing = 1/36
		self.pos_y_spacing_top = 1/100
		self.font_color = (0, 0, 0)