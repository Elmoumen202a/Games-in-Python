import unittest
from main import deal_card, calculate_score

class TestBlackjack(unittest.TestCase):
    def test_deal_card(self):
        # Test if dealt card is within valid range
        card = deal_card()
        self.assertTrue(2 <= card <= 11)

    def test_calculate_score(self):
        # Test calculate_score function with various card combinations
        hand1 = [2, 7]
        self.assertEqual(calculate_score(hand1), 9)

        hand2 = [10, 10, 1]
        self.assertEqual(calculate_score(hand2), 21)

        hand3 = [10, 10, 11]
        self.assertEqual(calculate_score(hand3), 21)

if __name__ == "__main__":
    unittest.main()
