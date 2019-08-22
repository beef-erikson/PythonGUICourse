import os
from random import shuffle
from guizero import App, Box, Picture, PushButton, Text, warn, info
from random import randint

# fields
game_timer = 20
rounds = 1
correct_guesses = 0
bonus_time = 10
player = "One"
leaderboard = []


# changes player
def change_player():
    global player
    if player == "One":
        player = "Two"
    else:
        player = "One"


# timer countdown / game over
def counter():
    timer.value = int(timer.value) - 1
    if int(timer.value) == 0:
        global game_timer
        global correct_guesses
        global rounds

        # stops timer and shows game over
        timer.cancel(counter)
        result.text_color = "black"
        result.value = "Game Over"
        warn("Game Over", "You have ran out of time!\nFinal Score: " + score.value + 
            "\n\nPlayer " + str(player) + "'s turn.")
        
        # resets variable values
        timer.value = game_timer
        result.value = ""
        score.value = "0"      
        correct_guesses = 0
        game_timer = 20
        score_bonus.value = ""
        
        # adds to round count
        rounds += 1
        
        # change player turn
        change_player()
        
        # restarts game
        setup_round()
        
        # starts new timer
        timer.repeat(1000, counter)
        

# populates list of emojis and shuffles them
def emoji_list():
    global emojis
    emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]
    shuffle(emojis)


# displays leaderboard
def leaderboard_display():
    global leaderboard


# sets result/score values if correct answer or not and creates a new round
def match_emoji(matched):
    global correct_guesses
    
    #  resets score bonus text
    score_bonus.value = ""
    if matched:
        result.text_color = "green"
        result.value = "correct"
        score.value = int(score.value) + 1
        
        # bonus point for 3 correct guesses in a row
        correct_guesses += 1
        if correct_guesses == 3:
            global game_timer
            timer.value = int(timer.value) + bonus_time
            score_bonus.value = "BONUS - 3 correct in a row! " + str(bonus_time) + " seconds added to timer!"
            correct_guesses = 0
    else:
        result.text_color = "red"
        result.value = "incorrect"
        score.value = int(score.value) - 1
        correct_guesses = 0
    
    # resets board
    setup_round()


# sets a round up
def setup_round():
    # makes a list of emojis
    emoji_list()

    # sets pictures for each grid
    for picture in pictures:
        picture.image = emojis.pop()

    for button in buttons:
        button.image = emojis.pop()
        button.update_command(match_emoji, [False])

    # choses a new emoji to be matched and sets to a random cell in each grid
    matched_emoji = emojis.pop()

    random_picture = randint(0,8)
    pictures[random_picture].image = matched_emoji

    random_button = randint(0,8)
    buttons[random_button].image = matched_emoji

    # sets the correct button to report true (the matched cell)
    buttons[random_button].update_command(match_emoji, [True])

    # Displays rounds played
    rounds_played.value = "Rounds played: " + str(rounds)


# sets up widgets
app = App("emoji match", width=420, height=574)
rounds_played = Text(app, text="Rounds played: " + str(rounds))
result = Text(app)
game_box = Box(app)
pictures_box = Box(game_box, layout="grid")
buttons_box = Box(game_box, layout="grid")

# setup for emoji directory and creates empty list to populate
emojis_dir = "emojis"
emojis = []

# displays player's turn and changes to other player
info("Player Turn", "Player " + str(player) + "'s turn.")
change_player()

# creates the two grids using a list
pictures = []
buttons = []

for x in range(0,3):
    for y in range(0,3):
        picture = Picture(pictures_box, grid=[x,y])
        pictures.append(picture)

        button = PushButton(buttons_box, grid=[x,y])
        buttons.append(button)

# sets timer text
extra_features = Box(app)
timerlabel = Text(extra_features, text="Time Left: ", align="left")
timer = Text(extra_features, text="Get Ready", align="left")

# sets score and bonus texts
scoreboard = Box(app)
label = Text(scoreboard, text="Score: ", align="left")
score = Text(scoreboard, text="0", align="left")
bonus = Box(app)
score_bonus = Text(bonus, text="", color="green")

# sets up a round
setup_round()

# starts timer
timer.value = game_timer
timer.repeat(1000, counter)

# starts app
app.display()
