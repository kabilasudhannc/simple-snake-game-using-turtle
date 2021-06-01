from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed('fastest')
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 280)
        self.write(arg=f'score: {self.score}', move=False, align='center', font=('Arial', 10, 'normal'))

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(arg=f'score: {self.score}', move=False, align='center', font=('Arial', 10, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f'GameOver.', move=False, align='center', font=('Arial', 20, 'normal'))
