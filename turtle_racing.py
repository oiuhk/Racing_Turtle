from turtle import Turtle, done, Screen
from random import randint
from time import sleep


class Baikal(Turtle):
    """ Turtle bot """
    def __init__(self, x: int, y: int, shp: str, clr: str, stp: int) -> None:
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.color(clr)
        self.shape(shp)
        self.step = stp
    
    def move(self) -> None:
        self.goto(self.xcor() + self.step, self.ycor())

    def stop(self) -> None:
        global win_color
        
        if self.xcor() >= 290:
            win_color = self.color()[0]
            return True
        return False


class Start_Finish(Turtle):
    """ Bild bot """
    def __init__(self, clr, siz):
        super().__init__()
        self.penup()
        self.ht()

        self.pencolor(clr)
        self.pensize(siz)
        self.speed(50)

    def bild(self):
        self.goto(-300, -150)
        self.left(90)
        self.pendown()
        self.forward(300)

        self.penup()

        self.goto(300, -150)
        self.pendown()
        self.forward(300)

    def text(self):
        self.pencolor('red')

        self.penup()
        self.goto(-300, 160)
        self.pendown()
        
        self.write(arg='START', align='center', font=('Verdana', 25, 'normal'))

        self.penup()
        self.goto(300, 160)
        self.pendown()

        self.write(arg='FINISH', align='center', font=('Verdana', 25, 'normal'))
        

class Circle_Turtle(Turtle):
    """ Сircle of turtles """
    def __init__(self, shp: str, clr: str, x: int, y: int, degree: int) -> None:
        super().__init__()
        self.ht()
        self.penup()
        self.speed(50)
        self.shape(shp)
        self.color(clr)
        self.goto(x, y)
        self.left(degree)
        self.st()


class Star(Turtle):
    """ Star """
    def __init__(self, siz, clr, x, y) -> None:
        super().__init__()
        self.penup()
        self.ht()
        self.speed(50)
        self.goto(x, y)
        self.pendown()
        self.color(clr)
        count=1
        self.pendown()

        self.begin_fill()
        for item in range(4):
            self.forward(siz)
            self.right(144)
        self.end_fill()


class Write_Win(Turtle):
    """ Winner inscription """
    def __init__(self, clr) -> None:
        super().__init__()
        self.penup()
        self.ht()
        self.speed(50)
        self.goto(0, 0)
        self.color(clr)
        self.pendown()
        self.write(arg='WINNER', align='center', font=('Verdana', 25, 'normal'))


def main():
    """ Start func. """
    wn = Screen()
    wn.title('turtle racing')
    wn.bgcolor('black')
    wn.setup(width=800, height=500)

    # Base game
    bob_stroitel = Start_Finish(clr='light steel blue', siz=5)
    bob_stroitel.bild()
    bob_stroitel.text()
    
    player1 = Baikal(x=-325, y=-130, shp='turtle', clr='yellow', stp=randint(5, 10))
    player2 = Baikal(x=-325, y=-80, shp='turtle', clr='white', stp=randint(5, 10))
    player3 = Baikal(x=-325, y=-30, shp='turtle', clr='pink', stp=randint(5, 10))
    player4 = Baikal(x=-325, y=20, shp='turtle', clr='orange', stp=randint(5, 10))
    player5 = Baikal(x=-325, y=70, shp='turtle', clr='purple', stp=randint(5, 10))
    player6 = Baikal(x=-325, y=120, shp='turtle', clr='blue', stp=randint(5, 10))

    sleep(2)
    
    while True:
        player1.move()
        player2.move()
        player3.move()
        player4.move()
        player5.move()
        player6.move()
        
        if player1.stop() or player2.stop() or player3.stop() or player4.stop() or player5.stop() or player6.stop():
            break
    
    wn.reset()
    # two window
    bot1 = Circle_Turtle(shp='turtle', clr=win_color, x=0, y=150, degree=-90)
    bot2 = Circle_Turtle(shp='turtle', clr=win_color, x=75, y=125, degree=-135)
    bot3 = Circle_Turtle(shp='turtle', clr=win_color, x=125, y=75, degree=-135)
    bot4 = Circle_Turtle(shp='turtle', clr=win_color, x=150, y=0, degree=180)
    bot5 = Circle_Turtle(shp='turtle', clr=win_color, x=125, y=-75, degree=135)
    bot6 = Circle_Turtle(shp='turtle', clr=win_color, x=75, y=-125, degree=135)
    bot7 = Circle_Turtle(shp='turtle', clr=win_color, x=0, y=-150, degree=90)
    bot8 = Circle_Turtle(shp='turtle', clr=win_color, x=-75, y=-125, degree=-315)
    bot9 = Circle_Turtle(shp='turtle', clr=win_color, x=-125, y=-75, degree=-315)
    bot10 = Circle_Turtle(shp='turtle', clr=win_color, x=-150, y=0, degree=0)
    bot11 = Circle_Turtle(shp='turtle', clr=win_color, x=-125, y=75, degree=315)
    bot12 = Circle_Turtle(shp='turtle', clr=win_color, x=-75, y=125, degree=315)
    
    win_text = Write_Win(clr=win_color)

    star1 = Star(siz=50, clr='yellow', x=-110, y=-20)
    star2 = Star(siz=50, clr='yellow', x=-25, y=-20)
    star3 = Star(siz=50, clr='yellow', x=60, y=-20)

    done()



if __name__ == '__main__':
    main()