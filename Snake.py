from tkinter import *
from random import *
from time import *
from pynput import *

root = Tk()
root.title("Snake")
root.geometry("600x675")
root.resizable(False, False)

game_frame = Frame(root, width=600, height=600)
game_frame.grid(column=0, row=0)
canvas_width = 600
canvas_height = 600
board = Canvas(game_frame, width=canvas_width,
               height=canvas_height, bg="black")

score_frame = Frame(root, width=600, height=75)
score_frame.grid(column=0, row=1)
score = Label(score_frame, text="",
              fg="red", font=("Comic Sans", 18))
restart_button = Button(score_frame, text="Restart?")

block_length = 20
# canvas_width and canvas_height,
# when divided by block_length, must be even
starting_X = canvas_width / 2 / block_length
starting_Y = canvas_height / 2 / block_length
snake = [[starting_X, starting_Y],
         [starting_X + 1, starting_Y + 1],
         [starting_X + 2, starting_Y + 2]]
food = [5, 5]
direction = 'W'
in_game = True

# Canvas + Keyboard

def on_press(key):
    global direction
    if key == keyboard.Key.up:
        if direction == 'S':
            pass
        else:
            direction = 'N'
    elif key == keyboard.Key.down:
        if direction == 'N':
            pass
        else:
            direction = 'S'
    elif key == keyboard.Key.left:
        if direction == 'E':
            pass
        else:
            direction = 'W'
    elif key == keyboard.Key.right:
        if direction == 'W':
            pass
        else:
            direction = 'E'

def draw_board():
    global snake
    for body in snake:
        top_left_X = body[0] * block_length
        top_left_Y = body[1] * block_length
        board.create_rectangle(top_left_X, top_left_Y,
                               top_left_X + block_length,
                               top_left_Y + block_length,
                               fill="green")

    food_left_X = food[0] * block_length
    food_left_Y = food[1] * block_length
    board.create_rectangle(food_left_X, food_left_Y,
                           food_left_X + block_length,
                           food_left_Y + block_length,
                           fill="purple")

def update_board():
    board.pack()
    root.update()
    board.delete('all')

def update_score():
    global snake
    current_score = len(snake)
    score_text = "Score: " + str(current_score)
    score.config(text=score_text)
    score.grid()

# Snake functions

def update_snake():
    global snake
    index = len(snake) - 1
    for i in range(index, -1, -1):
        if i > 0:
            snake[i][0] = snake[i-1][0]
            snake[i][1] = snake[i - 1][1]
        else:
            new_head()
            food_eaten()
            snake_death()

def new_head():
    global direction
    if direction == 'N':
        snake[0][1] -= 1
    elif direction == 'S':
        snake[0][1] += 1
    elif direction == 'W':
        snake[0][0] -= 1
    elif direction == 'E':
        snake[0][0] += 1

def snake_death():
    global in_game, snake, canvas_width, \
        canvas_height, block_length
    snake_head_X = snake[0][0]
    snake_head_Y = snake[0][1]

    for i in range(1, len(snake), 1):
        body = snake[i]
        if snake_head_X == body[0] \
                and snake_head_Y == body[1]:
            in_game = False

    if snake_head_X < 0 \
            or snake_head_X > (canvas_width/block_length - 1) \
            or snake_head_Y < 0 \
            or snake_head_Y > (canvas_height/block_length - 1):
        in_game = False

# Food functions

def food_eaten():
    global snake
    index = len(snake) - 1
    snake_head_X = snake[0][0]
    snake_head_Y = snake[0][1]
    if snake_head_X == food[0] and snake_head_Y == food[1]:
        snake_tail_X = snake[index][0]
        snake_tail_Y = snake[index][1]
        snake.append([snake_tail_X, snake_tail_Y])
        respawn_food()
        update_score()

def respawn_food():
    global food, canvas_width, canvas_height, block_length
    food[0] = randrange(0, int(canvas_width/block_length - 1))
    food[1] = randrange(0, int(canvas_height/block_length - 1))
    check_food()

def check_food():
    global snake, food
    for body in snake:
        if body[0] == food[0] and body[1] == food[1]:
            respawn_food()
        else:
            pass

# Game loop

def game_loop():
    update_score()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while in_game:
        sleep(0.08)
        update_snake()
        draw_board()
        update_board()

    post_game_menu()

def post_game_menu():
    global snake
    board.delete("all")
    score_text = "Final Score: " + str(len(snake))
    score.config(text=score_text)
    restart_button.config(command=restart)
    score.grid()
    restart_button.grid(row=1, pady=5)


# Restart

def restart():
    global in_game, snake, food, \
        direction, starting_X, starting_Y
    restart_button.grid_remove()
    in_game = True
    snake = [[starting_X, starting_Y],
             [starting_X + 1, starting_Y],
             [starting_X + 2, starting_Y]]
    direction = 'W'
    respawn_food()
    game_loop()


game_loop()
root.mainloop()
