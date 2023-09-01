import unittest
from main import get_user_choice, determine_winner, get_computer_choice

class TestRPSLSGame(unittest.TestCase):

    def test_get_computer_choice(self):
        # This will test if the function always returns a number between 1 and 5
        for _ in range(100):
            self.assertIn(get_computer_choice(), [1, 2, 3, 4, 5])

    def test_determine_winner(self):
        # Some simple test cases
        self.assertEqual(determine_winner(1, 1), 'draw')
        self.assertEqual(determine_winner(1, 3), 'user')
        self.assertEqual(determine_winner(1, 2), 'computer')
        # Add more test cases based on your logic
        self.assertEqual(determine_winner(1, 4), 'user')
        self.assertEqual(determine_winner(1, 5), 'computer')
        self.assertEqual(determine_winner(2, 1), 'user')
        self.assertEqual(determine_winner(2, 3), 'computer')
        self.assertEqual(determine_winner(2, 4), 'computer')
        self.assertEqual(determine_winner(2, 5), 'user')
        self.assertEqual(determine_winner(3, 1), 'computer')
        self.assertEqual(determine_winner(3, 2), 'user')
        self.assertEqual(determine_winner(3, 4), 'user')
        self.assertEqual(determine_winner(3, 5), 'computer')
        self.assertEqual(determine_winner(4, 1), 'computer')
        self.assertEqual(determine_winner(4, 2), 'user')
        self.assertEqual(determine_winner(4, 3), 'computer')
        self.assertEqual(determine_winner(4, 5), 'user')
        self.assertEqual(determine_winner(5, 1), 'user')
        self.assertEqual(determine_winner(5, 2), 'computer')
        self.assertEqual(determine_winner(5, 3), 'user')
        self.assertEqual(determine_winner(5, 4), 'computer')


    # Mock the built-in input function to simulate different user inputs
    def mock_input(self, prompt):
        return self.mocked_input_value

    def test_get_user_choice(self):
        # Mock the built-in input function to simulate user input
        global input
        input = self.mock_input

        self.mocked_input_value = "Rock"
        self.assertEqual(get_user_choice(), 1)

        self.mocked_input_value = "Spock"
        self.assertEqual(get_user_choice(), 5)

        self.mocked_input_value = "Paper"
        self.assertEqual(get_user_choice(), 2)

        self.mocked_input_value = "Scissors"
        self.assertEqual(get_user_choice(), 3)

        self.mocked_input_value = "Lizard"
        self.assertEqual(get_user_choice(), 4)
        # Test more user inputs...

if __name__ == "__main__":
    unittest.main()
