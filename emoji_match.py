import os
from random import shuffle
from guizero import App, Box, Picture, PushButton, Text, warn
from random import randint

# fields
gameTimer = 20
rounds = 0

# timer countdown - ends game when time runs out
def counter():
    timer.value = int(timer.value) - 1
    if int(timer.value) == 0:
        # stops timer and shows game over
        timer.cancel(counter)
        result.text_color = "black"
        result.value = "Game Over"
        warn("Time Over", "You have ran out of time")
        # resets timer/text, restarts game, and starts new timer
        timer.value = gameTimer
        result.value = ""
        setup_round()
        timer.repeat(1000, counter)


# populates list of emojis and shuffles them
def emoji_list():
    global emojis
    emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]
    shuffle(emojis)

# sets result value if correct answer or not and creates a new round
def match_emoji(matched):
    if matched:
        result.text_color = "green"
        result.value = "correct"
    else:
        result.text_color = "red"
        result.value = "incorrect"
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

    # adds to round played
    global rounds
    rounds += 1
    rounds_played.value = "Rounds played: " + str(rounds)


# sets up widgets
app = App("emoji match", width=320, height=530)
rounds_played = Text(app, text="Rounds played: " + str(rounds))
result = Text(app)
game_box = Box(app)
pictures_box = Box(game_box, layout="grid")
buttons_box = Box(game_box, layout="grid")

# setup for emoji directory and creates empty list to populate
emojis_dir = "emojis"
emojis = []

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
timer = Text(extra_features, text="Get Ready")

# sets up a round
setup_round()

# starts timer
timer.value = gameTimer
timer.repeat(1000, counter)

# starts app
app.display()