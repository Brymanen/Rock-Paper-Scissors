import sys
import pygame
import random

from settings import Settings

class RockPaperScissors:
	"""Overall class to manage game assets and behavior."""
	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		pygame.display.set_caption("Rock Paper Scissors")
		pygame.font.init()

		# Import the settings
		self.settings = Settings()

		# Display the game in fullscreen and grab the width and height of the game window
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.screen_width = self.screen.get_rect().width
		self.screen_height = self.screen.get_rect().height
		

		# create an empty list to store the all messages
		#self.list_of_messages = []
		self.played_games = []
		self.game_number = 0
		self.messages = []

		# Assign a font and font size
		self.text_font = pygame.font.SysFont(pygame.font.get_default_font(), 30)


	def run_game(self):
		"""Start the main loop for the game."""
		self.create_greeting_message()
		while True:
			self._check_events()
			self._update_screen()
        	
        	
	# Watch for keyboard and mouse events.
	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
                

	def create_greeting_message(self):
		"""Displays a text message on the screen"""
		self.greeting_message = self.text_font.render(self.settings.greeting_message, True, self.settings.font_color)

	def respond_to_user_input(self):
		# Randomly select a key from the dictioniary which maps rock, paper scissors to the number 0, 1, 2
		self.computer_choice = random.choice(list(self.settings.rock_paper_scissors_mapping.keys()))
		self.determine_result()
		self.store_game_data()
		#self.create_messages()






	def determine_result(self):
		# Determine the outcome of the game
		# If result = 0 then the game ended in a draw, if result = 1, the player won the game and if result = 2 the computer won the game
		# Determine wether the game ended in a draw
		if self.user_input == self.computer_choice:
			self.result = 0
		# Determine wether the player won
		elif self.user_input == 0 and self.computer_choice == 2 or self.user_input == 2 and self.computer_choice == 1:
			self.result = 1
		# Else the computer won the game
		else:
			self.result = 2

	def store_game_data(self):
		self.played_games.append(f"game_{self.game_number}")
		self.played_games[self.game_number] = {
		"game_number": self.game_number,
		"result": self.result,
		"user_input": self.user_input,
		"computer_choice": self.computer_choice 
		}
		print(self.played_games[self.game_number])
		self.game_number += 1

	#def create_messages(self):
		
		




	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_r:
			self.user_input = 0
			self.respond_to_user_input()
		elif event.key == pygame.K_p:
			self.user_input = 1
			self.respond_to_user_input()
		elif event.key == pygame.K_s:
			self.user_input = 2
			self.respond_to_user_input()

	def _check_keyup_events(self, event):
		"""Respond to key releases."""
		if event.key == pygame.K_r:
			self.user_input == None
		elif event.key == pygame.K_p:
			self.user_input = None
		elif event.key == pygame.K_s:
			self.user_input = None


	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		# Redraw the screen during each pass through the loop.
		self.screen.fill(self.settings.background_color)
		self.message_x = self.screen_width * self.settings.pos_x_spacing
		self.message_y = self.screen_height * self.settings.pos_y_spacing

		for game in self.played_games:
			for game_key in game:
				message = self.text_font.render(str(game[game_key]), True, self.settings.font_color)
				self.message_y += self.screen_width * self.settings.pos_x_spacing 
				print(f"self.message_y {self.message_y}")
				self.screen.blit(message,(self.message_x, self.message_y))
		

		pygame.display.flip()
            
if __name__ == '__main__':
	# Make a game instance, and run the game.
	rps = RockPaperScissors()
	rps.run_game()