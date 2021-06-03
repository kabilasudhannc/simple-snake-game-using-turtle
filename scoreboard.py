from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as file:
            self.high_score = int(file.read())
        self.speed('fastest')
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 280)
        self.write(arg=f'score: {self.score} High score: {self.high_score}', move=False, align='center',
                   font=('Arial', 10, 'normal'))

    def refresh(self):
        self.clear()
        self.write(arg=f'score: {self.score} High score: {self.high_score}', move=False, align='center', font=('Arial', 10, 'normal'))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f'GameOver.', move=False, align='center', font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.refresh()
