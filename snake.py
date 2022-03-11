from turtle import Turtle

#Construir cuerpo serpiente
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

#Creando clase
class Snake:

    #Constructor, def es lo mismo que function
    def __init__(self):
        #Almaceno los segmentos de la serpiente
        self.segments = []
        #metodo que crea la serpiente
        self.create_snake()
        #metodo que crea la serpiente
        self.head = self.segments[0]


    #Crear otra función -create snake
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            
    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("green")
        snake_segment.penup()
        #Funcion goto= ir a
        snake_segment.goto(position)
        self.segments.append(snake_segment)
        
    #añade segmento al final con el -1
    def extend(self):
        self.add_segment(self.segments[-1].position())


    #metodo move
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            #xcor:dice en que posicion está
            new_X = self.segments[seg_num -1].xcor()
            new_Y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_X, new_Y)

        self.head.forward(20)

    """ for segment in segments:
        segment.forward(20)
    #segment.left(90) """

    #creación metodo de escucha de las teclas
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT) 

               