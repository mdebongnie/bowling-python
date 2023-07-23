class BowlingGame():
    def __init__(self):

        self.rolls = []
        pass
    
    def roll(self, pins_down: int) -> None:

        self.rolls.append(pins_down)
        pass

    def score(self) -> int:
        
        return sum([self.rolls.pop(0) + self.rolls[0] + self.rolls[1] if self.rolls[0] == 10 else self.rolls.pop(0) + self.rolls.pop(0) + self.rolls[0] if self.rolls[0] + self.rolls[1] == 10 else self.rolls.pop(0) + self.rolls.pop(0) for i in range(10)])