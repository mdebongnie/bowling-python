class BowlingGame():
    def __init__(self):

        self.rolls = []
        pass
    
    def roll(self, pins_down: int) -> None:

        self.rolls.append(pins_down)
        pass

    def score(self) -> int:
        
        points = []
        for i in range(10):

            points.append(self.rolls.pop(0))
            
            if points[-1] == 10:
                # Strike
                points[-1] += self.rolls[0] + self.rolls[1]
                continue

            points[-1] += self.rolls.pop(0)

            if points[-1] == 10:
                # Spare
                points[-1] += self.rolls[0]
                      
        return sum(points)