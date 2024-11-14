# Import the randint() function from the random module to generate random numbers.
from random import randint

# Set the dimensions of the game window.
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

# Initialize empty lists to hold the dance moves and the sequence to display.
move_list = []
display_list = []

# Initialize game variables, including score and current move index.
score_player1 = 0
score_player2 = 0
current_player = 2  # Player 1 starts first
current_move = 0
count = 4  # Countdown value before each new move sequence.
dance_length = 4  # Length of the dance sequence.
 
# Boolean flags to control various game states (e.g., countdown, game over).
say_dance = False
show_countdown = True
moves_complete = False
game_over = False

# Create the dancer object and position it at the center of the screen.
dancer = Actor("dancer-start")
dancer.pos = CENTER_X + 5, CENTER_Y - 40

# Create and position the arrow direction buttons around the dancer.
up = Actor("up")
up.pos = CENTER_X, CENTER_Y + 110
right = Actor("right")
right.pos = CENTER_X + 60, CENTER_Y + 170
down = Actor("down")
down.pos = CENTER_X, CENTER_Y + 230
left = Actor("left")
left.pos = CENTER_X - 60, CENTER_Y + 170

def draw():
    # Define which global variables to use in this function.
    global game_over, score, say_dance
    global count, show_countdown
    
    # If the game is not over, render the game screen.
    if not game_over:
        screen.clear()  # Clear previous frames on the screen.
        screen.blit("stage", (0, 0))  # Draw the background.
        dancer.draw()  # Draw the dancer.
        up.draw()  # Draw the up button.
        down.draw()  # Draw the down button.
        right.draw()  # Draw the right button.
        left.draw()  # Draw the left button.
        
        # Display both players' scores.
        screen.draw.text("Player 1 Score: " + str(score_player1), color="black", topleft=(10, 10))
        screen.draw.text("Player 2 Score: " + str(score_player2), color="black", topright=(WIDTH - 10, 10))
        
        # Display the current player who needs to play next.
        if current_player == 1:
            screen.draw.text("Player 1's Turn", color="black", topleft=(CENTER_X - 90, 110), fontsize=40)
        else:
            screen.draw.text("Player 2's Turn", color="black", topleft=(CENTER_X - 90, 110), fontsize=40)
            
        # If say_dance is True, display the "Dance!" text in the middle of the screen.
        if say_dance:
            screen.draw.text("Dance!", color="black", topleft=(CENTER_X - 65, 150), fontsize=60)
                
        # If show_countdown is True, display the countdown number.
        if show_countdown:
            screen.draw.text(str(count), color="black", topleft=(CENTER_X - 8, 150), fontsize=60)
        
    # If game_over is True, display a game-over message.
    else:
        screen.clear()
        screen.blit("stage", (0, 0))  # Draw background again.
        screen.draw.text("Player 1 Score: " + str(score_player1), color="black", topleft=(10, 10))
        screen.draw.text("Player 2 Score: " + str(score_player2), color="black", topright=(WIDTH - 10, 10))
        screen.draw.text("GAME OVER!", color="black", topleft=(CENTER_X - 130, 150), fontsize=60)  # Game over message.
        screen.draw.text("BGM: Funky-Elegant-Rhythmic", color="black", topleft=(CENTER_X - 210, 200), fontsize=40)
        screen.draw.text("Creator: Olezha Chopalish", color="black", topleft=(CENTER_X - 180, 240), fontsize=40)
        screen.draw.text("From: Jamendo", color="black", topleft=(CENTER_X - 110, 280), fontsize=40)
    return

def reset_dancer():
    # Reset the dancer and direction buttons to their initial states.
    global game_over
    if not game_over:
        dancer.image = "dancer-start"
        up.image = "up"
        right.image = "right"
        down.image = "down"
        left.image = "left"
    return

def update_dancer(move):
    # Update the dancer's position and image to match the selected move.
    global game_over
    if not game_over:
        # Perform the move based on the passed value (0 = Up, 1 = Right, 2 = Down, 3 = Left).
        if move == 0:
            up.image = "up-lit"  # Highlight the Up button.
            dancer.image = "dancer-up"  # Change dancer's pose to Up.
            clock.schedule(reset_dancer, 0.5)  # Reset the dancer after half a second.
        elif move == 1:
            right.image = "right-lit"  # Highlight the Right button.
            dancer.image = "dancer-right"  # Change dancer's pose to Right.
            clock.schedule(reset_dancer, 0.5)
        elif move == 2:
            down.image = "down-lit"  # Highlight the Down button.
            dancer.image = "dancer-down"  # Change dancer's pose to Down.
            clock.schedule(reset_dancer, 0.5)
        else:
            left.image = "left-lit"  # Highlight the Left button.
            dancer.image = "dancer-left"  # Change dancer's pose to Left.
            clock.schedule(reset_dancer, 0.5)
    return

def display_moves():
    # Display the generated dance moves sequence to the player.
    global move_list, display_list, dance_length
    global say_dance, show_countdown, current_move
    
    # Check if there are moves to display.
    if display_list:
        this_move = display_list[0]  # Get the first move from the list.
        display_list = display_list[1:]  # Remove the displayed move.
        
        # Perform the corresponding move.
        if this_move == 0:
            update_dancer(0)
            clock.schedule(display_moves, 1)  # Schedule the next move after 1 second.
        elif this_move == 1:
            update_dancer(1)
            clock.schedule(display_moves, 1)
        elif this_move == 2:
            update_dancer(2)
            clock.schedule(display_moves, 1)
        else:
            update_dancer(3)
            clock.schedule(display_moves, 1)
    else:
        # Once all moves are displayed, show "Dance!" on the screen.
        say_dance = True
        show_countdown = False  # Stop the countdown display.
    return

def generate_moves():
    # Generate a random sequence of dance moves.
    global move_list, dance_length, count
    global show_countdown, say_dance, current_player
    count = 4  # Reset countdown timer.
    move_list = []  # Clear move list.
    say_dance = False  # Reset "Dance!" message flag.

    for move in range(0, dance_length):
        rand_move = randint(0, 3)  # Generate a random move (0-3).
        move_list.append(rand_move)  # Add move to list.
        display_list.append(rand_move)  # Add move to display list.

    show_countdown = True  # Start countdown.
    countdown()  # Start countdown sequence.

    # Alternate the player turn after the moves are generated.
    current_player = 1 if current_player == 2 else 2
    return

def countdown():
    # Handle the countdown before the dance sequence starts.
    global count, game_over, show_countdown
    if count > 1:
        count -= 1  # Decrease the countdown by 1.
        clock.schedule(countdown, 1)  # Schedule the next countdown tick.
    else:
        show_countdown = False  # Stop the countdown display.
        display_moves()  # Start displaying the moves.
    return

def next_move():
    # Move to the next dance move in the sequence.
    global dance_length, current_move, moves_complete
    if current_move < dance_length - 1:
        current_move += 1  # Increment the move index.
    else:
        moves_complete = True  # All moves are completed.
    return

def on_key_up(key):
    # Handle the player’s input and check if it matches the current move.
    global score_player1, score_player2, game_over, move_list, current_move, current_player
    
    if current_player == 1:  # Player 1 uses W, A, S, D keys
        if key == keys.W:
            update_dancer(0)
            if move_list[current_move] == 0:
                score_player1 += 1
                next_move()
            else:
                game_over = True
        elif key == keys.A:
            update_dancer(3)
            if move_list[current_move] == 3:
                score_player1 += 1
                next_move()
            else:
                game_over = True
        elif key == keys.S:
            update_dancer(2)
            if move_list[current_move] == 2:
                score_player1 += 1
                next_move()
            else:
                game_over = True
        elif key == keys.D:
            update_dancer(1)
            if move_list[current_move] == 1:
                score_player1 += 1
                next_move()
            else:
                game_over = True

    elif current_player == 2:  # Player 2 uses arrow keys
        if key == keys.UP:
            update_dancer(0)
            if move_list[current_move] == 0:
                score_player2 += 1
                next_move()
            else:
                game_over = True
        elif key == keys.LEFT:
            update_dancer(3)
            if move_list[current_move] == 3:
                score_player2 += 1
                next_move()
            else:
                game_over = True
        elif key == keys.DOWN:
            update_dancer(2)
            if move_list[current_move] == 2:
                score_player2 += 1
                next_move()
            else:
                game_over = True
        elif key == keys.RIGHT:
            update_dancer(1)
            if move_list[current_move] == 1:
                score_player2 += 1
                next_move()
            else:
                game_over = True
    return


# Generate an initial sequence of moves and play the background music.
generate_moves()
music.play("funky-elegant-rhythmic")

def update():
    # Main game update loop.
    global game_over, current_move, moves_complete
    if not game_over:
        if moves_complete:  # If all moves in the sequence are complete.
            generate_moves()  # Generate a new sequence of moves.
            moves_complete = False
            current_move = 0  # Reset current move to the first one.
    else:
        music.stop()  # Stop the music when the game is over.
