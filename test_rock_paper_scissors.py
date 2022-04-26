import unittest

from rock_paper_scissors import RockPaperScissors

class RockPaperScissorsTestCase(unittest.TestCase):
	"""Tests for 'rock_paper_scissors.py'."""

	def setUp(self):
		"""Prepares the result counters for the upcoming test functions"""
		self.result_0_count = 0
		self.result_1_count = 0
		self.result_2_count = 0

	def test_resultd(self):
		"""
		User inputs and the randomized choices for the computer are given
		this fuction checks whether the winner of the match is being
		correctly determined
		"""
		# Player: rock, PC: rock, result: draw.
		self.user_input = 0 
		self.computer_choice = 0
		result = RockPaperScissors.determine_result(self)
		self.assertEqual(self.result, 0)
		# Player: rock, PC: paper, result: PC wins.
		self.user_input = 0 
		self.computer_choice = 1
		result = RockPaperScissors.determine_result(self)
		self.assertEqual(self.result, 2)
		# Player: rock, PC: scissors, result: player wins.
		self.user_input = 0 
		self.computer_choice = 2
		result = RockPaperScissors.determine_result(self)
		self.assertEqual(self.result, 1)
		# Player: paper, PC: rock, result: player wins.
		self.user_input = 1 
		self.computer_choice = 0
		result = RockPaperScissors.determine_result(self)
		self.assertEqual(self.result, 1)
		# Player: paper, PC: paper, result: player draw.
		self.user_input = 1 
		self.computer_choice = 1
		result = RockPaperScissors.determine_result(self)
		self.assertEqual(self.result, 0)
		# Player: paper, PC: scissors, result: PC wins.
		self.user_input = 1 
		self.computer_choice = 2
		result = RockPaperScissors.determine_result(self)
		self.assertEqual(self.result, 2)
		# Player: scissors, PC: rock, result: PC wins.
		self.user_input = 2
		self.computer_choice = 0
		result = RockPaperScissors.determine_result(self)
		self.assertEqual(self.result, 2)
		# Player: scissors, PC: paper, result: player wins.
		self.user_input = 2
		self.computer_choice = 1
		result = RockPaperScissors.determine_result(self)
		self.assertEqual(self.result, 1)
		# Player: scissors, PC: scissors, result: draw.
		self.user_input = 2
		self.computer_choice = 2
		result = RockPaperScissors.determine_result(self)
		self.assertEqual(self.result, 0)

	def test_scoreboard_counter(self):
		"""
		This fuction checks whether the amount of times the match ended in
		a draw, in the player winning or the computer winning are being
		calculated correctly.
		"""
		# Simulate 5 played games.  1 game ended in a draw, 3 games were won 
		# by the player and 1 game was won by the computer.
		self.played_games = [
		{'game_number': 0, 'user_input': 0, 'computer_choice': 0}, 
		{'game_number': 1, 'user_input': 0, 'computer_choice': 2}, 
		{'game_number': 2, 'user_input': 0, 'computer_choice': 2}, 
		{'game_number': 3, 'user_input': 0, 'computer_choice': 2}, 
		{'game_number': 4, 'user_input': 2, 'computer_choice': 0}
		]
		for self.played_game in self.played_games:
			self.game_number = self.played_game['game_number']
			self.user_input = self.played_game['user_input']
			self.computer_choice = self.played_game['computer_choice']
			RockPaperScissors.determine_result(self)
		# Find out whether only one game was identified as a draw.
		self.assertEqual(self.result_0_count, 1)
		# Find out if 3 wins have been assigned to the player.
		self.assertEqual(self.result_1_count, 3)
		# Find out if 1 win has been assigned to the computer.
		self.assertEqual(self.result_2_count, 1)

if __name__ == '__main__':
    unittest.main()