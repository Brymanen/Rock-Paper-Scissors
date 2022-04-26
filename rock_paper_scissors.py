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
		# Create an instance of Settings
		self.settings = Settings()
		# Display the game in fullscreen and 
		# grab the width and height of the game window
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.screen_width = self.screen.get_rect().width
		self.screen_height = self.screen.get_rect().height
		# Create an empty list to store the all played games, assign the 
		# number of played games to 0 and create a list to hold all messages
		self.played_games = []
		self.game_number = 0
		self.messages = []
		self.scoreboard_messages = []
		self.result_0_count = 0
		self.result_1_count = 0
		self.result_2_count = 0
		# Assign a font and font size
		self.text_font = pygame.font.SysFont(pygame.font.get_default_font(), 30)

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			self._update_screen()
        	
	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
	
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
		self.display_greeting_message()
		# Loop through all played games, starting with the latest game
		for game in reversed(self.played_games):
			# Create the text for the messages for every game
			self.create_message_text(game)
			# Loop through all the messages 
			for message in self.messages:
				# Create the actual messages and display them
				self.display_game_message(message)
				self.messages = []
		self.update_scoreboard()
		pygame.display.flip()
            
	def display_greeting_message(self):
		"""Displays a text message on the screen"""
		message_content = self.settings.greeting_message
		message = self.text_font.render(
			message_content, True, self.settings.font_color)
		self.message_y += self.screen_width * self.settings.pos_y_spacing 
		self.screen.blit(message,(self.message_x, self.message_y))

	def respond_to_user_input(self):
		"""
		The user can input rock, paper, scissors and the game 
		receives the input and responds to it
		"""
		# Randomly select a key from the dictioniary which maps 
		# rock, paper scissors to the number 0, 1, 2
		self.computer_choice = random.choice(
			list(self.settings.rock_paper_scissors_mapping.keys()))
		self.determine_result()
		self.store_game_data()

	def determine_result(self):
		"""Determines the outcome of the game"""
		# If result = 0 then the game ended in a draw, if result = 1, 
		# the player won the game and if result = 2 the computer won the game.
		# First, determine whether the game ended in a draw
		if self.user_input == self.computer_choice:
			self.result = 0
			self.result_0_count += 1
		# Next, determine whether the player won
		elif (
				self.user_input == 0 and self.computer_choice == 2 
				or self.user_input == 2 and self.computer_choice == 1 
				or self.user_input == 1 and self.computer_choice == 0
			):
			self.result = 1
			self.result_1_count += 1
		# Else the computer won the game
		else:
			self.result = 2
			self.result_2_count += 1

	def store_game_data(self):
		"""
		Stores the game data in dictionaries. 
		The dictionaries are being stored in a list.
		"""
		self.played_games.append(f"game_{self.game_number}")
		self.played_games[self.game_number] = {
		"game_number": self.game_number,
		"result": self.result,
		"user_input": self.user_input,
		"computer_choice": self.computer_choice 
		}
		self.game_number += 1

	def create_message_text(self, game):
		"""Creates messages explaining, what happened in the game"""
		# Create the string for the message for the message explaining 
		# explaining the game number to the list of messages
		self.messages.append(
			f'{self.settings.text_game_number}'
			f'{game["game_number"]+1}')
		# Create the string for the message explaining the 
		# user input to the list of messages
		self.messages.append(
			f'{self.settings.text_user_picked}'
			f'{self.settings.rock_paper_scissors_mapping[game["user_input"]].title()}')
		# Create the string for the message explaining the randomized computer 
		# choice to the list of messages
		self.messages.append(
			f'{self.settings.text_computer_picked}'
			f'{self.settings.rock_paper_scissors_mapping[game["computer_choice"]].title()}')
		# Create the string for the message explaining the 
		# game result to the list of messages
		self.messages.append(
			f'{self.settings.text_result[game["result"]]}')
		# Add a spacing between the messages of different games
		self.message_y += (
			self.screen_width * self.settings.pos_y_spacing_between_games)

	def display_game_message(self, message_content):
		"""Creates and displays the messages, will be blitted to the screen"""
		message = self.text_font.render(
			message_content, True, self.settings.font_color)
		self.message_y += self.screen_width * self.settings.pos_y_spacing 
		# Blit the messages to the screen, but only if the messages will be
		# displayed above a cut off starting from the bottom of the screen
		if self.message_y <= (
			self.screen_height * self.settings.screen_bottom_cutoff):
			# Blit the messages to the screen
			self.screen.blit(message,(self.message_x, self.message_y))

	def update_scoreboard(self):
		# First create the x and y coordinates for the scoreboard
		self.scoreboard_x = self.screen_width * self.settings.scoreboard_x
		self.scoreboard_y = self.screen_height * self.settings.scoreboard_y
		# Create the content of the scoreboard and store it in a list
		self.scoreboard_messages.append(
			f'{self.settings.text_scoreboard_draw}{self.result_0_count}')
		self.scoreboard_messages.append(
			f'{self.settings.text_scoreboard_won_games}{self.result_1_count}')
		self.scoreboard_messages.append(
			f'{self.settings.text_scoreboard_lost_games}{self.result_2_count}')
		for scoreboard_message in self.scoreboard_messages:
			message = self.text_font.render(
				scoreboard_message, True, self.settings.font_color)
			# Adjust the y coordinate for each message
			self.scoreboard_y += (
				self.screen_height * self.settings.scoreboard_y_spacing)
			# Blit the messages to the screen
			self.screen.blit(message,(self.scoreboard_x, self.scoreboard_y))
		self.scoreboard_messages = []

if __name__ == '__main__':
	# Make a game instance, and run the game.
	rps = RockPaperScissors()
	rps.run_game()