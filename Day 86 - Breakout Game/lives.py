from turtle import Turtle

class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.update()

    def update(self):
        self.clear()
        self.goto(320, - 250)
        self.write(f"Lives : {self.lives}", align="center", font=("Arial", 25, "normal"))


    def live(self):
        self.lives -= 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=("Arial", 20, "normal"))
