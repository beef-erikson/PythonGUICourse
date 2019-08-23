import os
from random import shuffle
from guizero import App, Box, Picture, PushButton, Text, warn, info, Window
from random import randint
from operator import itemgetter
import pickle

# fields
game_timer = 20
rounds = 1
correct_guesses = 0
bonus_time = 10
player = "One"
high_scores = [
    ("Bob", 12),
    ("Mike", 2),
    ("Joe", 13),
    ("Jane", 3),
    ("Bill", 4),
    ("Joe", 4), 
    ("Michelle", 5),
    ("Slick", 15),
    ("Marie", 7),
    ("Sally", 9),
]


# TODO define players
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
        global high_scores

        # insert scores into file
        high_scores.append((player, int(score.value)))
        high_scores = sorted(high_scores, key=itemgetter(1), reverse=True)[:10]

        with open('highscores.txt', 'wb') as f:
            pickle.dump(high_scores, f)

        # change player turn
        change_player()
        
        # TODO change this to reflect player's name correctly
        # stops timer and shows game over
        timer.cancel(counter)
        result.text_color = "black"
        result.value = "Game Over"
        warn("Game Over", "You have ran out of time!\nFinal Score: " + score.value + 
            "\n\nPlayer " + player + "'s turn.")
        
        # shows leaderboard
        leaderboard_display()

# populates list of emojis and shuffles them
def emoji_list():
    global emojis
    emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]
    shuffle(emojis)


# leaderboard closed, starts new game
def leaderboard_closed():
    leaderboard.hide()
    new_game()


# leaderboard window at game end
def leaderboard_display():
    # loads and displays high scores
    high_scores = []
    leaderboard.show(wait=True)

    with open('highscores.txt', 'rb') as f:
        high_scores = pickle.load(f)
    
    for high_score in high_scores:
        Text(leaderboard, high_score)
    
    # starts a new game by hitting the button
    PushButton(leaderboard, text="Next Player", command=new_game)

    # closes everything if closed button is hit
    leaderboard.when_closed = leaderboard_closed


# sets result/score values if correct answer or not and creates a new round
def match_emoji(matched):
    global correct_guesses
    
    #  resets score bonus text
    score_bonus.value = ""

    # displays correct and increases score
    if matched:
        result.text_color = "green"
        result.value = "correct"
        score.value = int(score.value) + 1
        correct_guesses += 1

        # bonus time for 3 correct guesses in a row
        if correct_guesses == 3:
            global game_timer
            timer.value = int(timer.value) + bonus_time
            score_bonus.value = "BONUS - 3 correct in a row! " + str(bonus_time) + " seconds added to timer!"
            correct_guesses = 0

    # displays incorrect and reduces score
    else:
        result.text_color = "red"
        result.value = "incorrect"
        score.value = int(score.value) - 1
        correct_guesses = 0
    
    # resets board
    setup_round()


def new_game():
    global game_timer
    global rounds
    global correct_guesses
    global leaderboard

    # destroys and creates leaderboard window
    leaderboard.destroy()
    leaderboard = Window(app, title="High Scores")
    leaderboard.hide()

    # resets variable values
    timer.value = game_timer
    result.value = ""
    score.value = "0"      
    correct_guesses = 0
    game_timer = 20
    score_bonus.value = ""
    
    # adds to round count
    rounds += 1
    
    # restarts game
    setup_round()
    
    # starts new timer
    timer.repeat(1000, counter)


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

# leader board window setup
leaderboard = Window(app, title="High Scores")
leaderboard.hide()

# setup for emoji directory and creates empty list to populate
emojis_dir = "emojis"
emojis = []

# TODO change this to reflect players name
# displays player's turn
info("Player Turn", "Player " + player + "'s turn.")

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
