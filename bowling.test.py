
import unittest
from bowling import BowlingGame;

class TestStringMethods(unittest.TestCase):
    
    def _roll_a_game_and_score(self, rolls):
        game = BowlingGame();
        [game.roll(pins_down) for pins_down in rolls]
        return game.score()

    def test_should_be_able_to_score_a_game_with_all_zeros(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 0)

    def test_should_be_able_to_score_a_game_with_no_strikes_or_spares(self):
        rolls = [3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]

        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 90)

    def test_should_be_able_to_score_a_game_with_no_strikes_and_a_spare(self):
        rolls = [3, 6, 3, 6, 3, 6, 3, 6, 4, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]

        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 94)

    def test_should_be_able_to_score_a_game_with_no_strikes_and_two_spares(self):
        rolls = [3, 6, 3, 6, 3, 6, 3, 6, 4, 6, 4, 6, 3, 6, 3, 6, 3, 6, 3, 6]

        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 99)

    def test_should_be_able_to_score_a_game_with_a_strike_and_no_spare(self):
        rolls = [3, 6, 3, 6, 3, 6, 3, 6, 10, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]

        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 100)
    
    def test_should_be_able_to_score_a_game_with_a_strike_and_no_spare(self):
        rolls = [3, 6, 10, 3, 6, 3, 6, 10, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]

        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 110)

    def test_should_be_able_to_score_a_game_with_two_strikes_and_a_spare(self):
        rolls = [3, 6, 10, 3, 6, 4, 6, 10, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]

        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 121)

    def test_should_be_able_to_score_a_game_with_two_consecutive_strikes_and_a_spare(self):
        rolls = [3, 6, 10, 10, 4, 6, 10, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]

        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 137)

    def test_should_be_able_to_score_a_game_with_spare_at_end(self):
        rolls = [3, 6, 10, 10, 4, 6, 10, 3, 6, 3, 6, 3, 6, 3, 6, 4, 6, 3]

        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 141) 

    def test_should_be_able_to_score_a_game_with_strike_at_end(self):
        rolls = [3, 6, 10, 10, 4, 6, 10, 3, 6, 3, 6, 3, 6, 3, 6, 10, 3, 6]

        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 147) 
    
    def test_should_be_able_to_score_a_perfect_game(self):
        rolls = [10 for i in range(12)]

        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 300)
        
if __name__ == '__main__':
    unittest.main()