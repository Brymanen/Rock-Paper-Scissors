import sys
import pygame
from settings import Settings



class RockPaperScissors:
	"""Overall class to manage game assets and behavior."""
	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		# Set a caption for the pygame window
		pygame.display.set_caption("Rock Paper Scissors")
		pygame.font.init()
		# Display the game in fullscreen
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.screen_width = self.screen.get_rect().width
		self.screen_height = self.screen.get_rect().height
		self.settings = Settings()
		# create a list to store the list of messages
		self.list_of_messages = []
		self.text_font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
		
		# Assign values to the x and y coordinates, where the messages will be shown
		posX = (self.screen_width * 1/8)
		posY = (self.screen_height * 1/8)
		position = posX, posY

	def run_game(self):
		"""Start the main loop for the game."""
		self.display_greeting_message()
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
                

	def display_greeting_message(self):
		"""Displays a text message on the screen"""
		self.list_of_messages.append(self.settings.greeting_message)
    	
	def _display_user_input(self):
		"""First the player enters r for rock, p for paper or s for scissors, the user input will be shown on the screen."""
		self.user_input_message = f"You selected: {self.user_input}"
		self.list_of_messages.append(self.user_input_message)
		print(self.user_input)

	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_r:
			self.user_input = "rock"
			self._display_user_input()
		elif event.key == pygame.K_p:
			self.user_input = "paper"
			self._display_user_input()
		elif event.key == pygame.K_s:
			self.user_input = "scissors"
			self._display_user_input()

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
        
		self.text_surface = self.text_font.render(str(self.list_of_messages), True, (0, 0, 0))
		#for message in self.list_of_messages:
			#pygame.draw.rect(self.screen, (255, 255, 0), str(message))
		#pygame.display.update()

		self.screen.blit(self.text_surface, (0,0))
		# Make the most recently drawn screen visible.
		pygame.display.flip()
            
if __name__ == '__main__':
	# Make a game instance, and run the game.
	rps = RockPaperScissors()
	rps.run_game()