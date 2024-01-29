import turtle
import random

# Initialize game variables
food = turtle.Vector(0, 0)
snake = [turtle.Vector(10, 0)]
direction = turtle.Vector(0, -10)

# Function to change snake direction
def change(x, y):
    direction.x = x
    direction.y = y

# Function to check if head is inside boundaries
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

# Function to move the snake
def move():
    head = snake[-1].copy()
    head.move(direction)

    if not inside(head) or head in snake:
        game_over()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10
    else:
        snake.pop(0)

    update_screen()
    turtle.ontimer(move, 100)

# Function to handle game over
def game_over():
    turtle.square(snake[-1].x, snake[-1].y, 9, 'red')
    update_screen()
    turtle.bye()

# Function to update the screen
def update_screen():
    turtle.clear()

    for body in snake:
        turtle.square(body.x, body.y, 9, 'black')

    turtle.square(food.x, food.y, 9, 'green')
    turtle.update()

# Setup the game window
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()

# Set up key bindings
turtle.onkey(lambda: change(10, 0), 'Right')
turtle.onkey(lambda: change(-10, 0), 'Left')
turtle.onkey(lambda: change(0, 10), 'Up')
turtle.onkey(lambda: change(0, -10), 'Down')

# Start the game loop
move()
turtle.done()
