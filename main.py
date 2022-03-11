from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#Creación escenario
screen = Screen() #Creación de variable/objeto para el escenario
screen.setup(width=600, height=600)
screen.bgcolor("brown")
screen.title("Programate snake game")

screen.tracer(0)


#Animación serpiente
game_is_on = True

#creo a la serpiente- instanciar objeto serpiente
snake = Snake()

#creo la comida - instanciar objeto comida
food = Food()

#creo el tabler - instanciar objeto tablero
scoreboard =ScoreBoard()

#metodo de escucha de las teclas
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detectar colisión comida
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        #Con extend extiende el cuerpo -funcion creada en snake
        snake.extend()

    #Detector colisiones de paredes
    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 275 or snake.head.ycor() < -275:
        game_is_on = False
        scoreboard.game_over()


    #detector de colisiones de segmento de serpiente
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()