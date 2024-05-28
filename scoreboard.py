from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        self.write(f'Score: {self.score}', align='center', font=('Times New Roman', 20, 'normal'))
        print('score')
    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f'Score: {self.score}', align='center', font=('Times New Roman', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Times New Roman', 20, 'normal'))
