# test_game.py
import unittest
from game import determine_winner

class TestDetermineWinner(unittest.TestCase):
            def test_tie(self):
                for choice in ["rock", "paper", "scissors"]:
                    self.assertEqual(determine_winner(choice, choice), "tie")

            def test_win(self):
                self.assertEqual(determine_winner("rock", "scissors"), "win")
                self.assertEqual(determine_winner("paper", "rock"), "win")
                self.assertEqual(determine_winner("scissors", "paper"), "win")

            def test_lose(self):
                self.assertEqual(determine_winner("rock", "paper"), "lose")
                self.assertEqual(determine_winner("paper", "scissors"), "lose")
                self.assertEqual(determine_winner("scissors", "rock"), "lose")

            def test_invalid_input(self):
                self.assertNotIn(determine_winner("lizard", "rock"), ["win", "lose", "tie"])
                self.assertNotIn(determine_winner("rock", "spock"), ["win", "lose", "tie"])
                self.assertNotIn(determine_winner("", "rock"), ["win", "lose", "tie"])
                self.assertNotIn(determine_winner(None, "rock"), ["win", "lose", "tie"])
                self.assertNotIn(determine_winner("rock", None), ["win", "lose", "tie"])
                self.assertNotIn(determine_winner(123, "rock"), ["win", "lose", "tie"])
                self.assertNotIn(determine_winner("rock", []), ["win", "lose", "tie"])

            def test_case_sensitivity(self):
                self.assertEqual(determine_winner("Rock".lower(), "rock"), "tie")
                self.assertEqual(determine_winner("PAPER".lower(), "rock"), "win")
                self.assertEqual(determine_winner("ScIsSoRs".lower(), "paper"), "win")

if __name__ == "__main__":
    unittest.main()