import os
from random import shuffle, randint
from guizero import App, Box, Picture, PushButton, Text, TextBox, warn, info, Window
from operator import itemgetter
import pickle

"""Fields"""
game_timer = 20
rounds = 1
correct_guesses = 0
bonus_time = 10
player_one = ""
player_two = ""
current_player = ""
pictures = []
buttons = []
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


"""Changes player"""
def change_player():
    global current_player

    if current_player == player_one:
        current_player = player_two
    else:
        current_player = player_one


"""Timer countdown / game over"""
def counter():
    timer.value = int(timer.value) - 1
    if int(timer.value) == 0:
        # saves leaderboard
        leaderboard_save()
        
        # change player turn
        change_player()
        
        # stops timer
        timer.cancel(counter)
        result.text_color = "black"
        result.value = "Game Over"
        
        # shows leaderboard
        leaderboard_display()


""" Populates list of emojis and shuffles them"""
def emoji_list():
    global emojis
    emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]
    shuffle(emojis)


"""Leaderboard closed, starts new game"""
def leaderboard_closed():
    leaderboard.hide()
    new_game()


"""leaderboard window at game end"""
def leaderboard_display():
    # loads and displays high scores
    high_scores = []
    leaderboard.show(wait=True)

    # header text
    Text(leaderboard, "You have ran out of time!\nFinal Score: " + score.value + "\n", size=18)
    Text(leaderboard, "High Scores")
    Text(leaderboard, "-----------")

    # reads and displays leaderboard
    with open('highscores.txt', 'rb') as f:
        high_scores = pickle.load(f)
    
    for high_score in high_scores:
        Text(leaderboard, high_score)
    
    # starts a new game by hitting the button
    PushButton(leaderboard, text="Next Player", command=new_game)

    # starts new game if closed button is hit
    leaderboard.when_closed = leaderboard_closed


"""Saves leaderboard scores"""
def leaderboard_save():
    global high_scores

    high_scores.append((current_player, int(score.value)))
    high_scores = sorted(high_scores, key=itemgetter(1), reverse=True)[:10]

    with open('highscores.txt', 'wb') as f:
        pickle.dump(high_scores, f)


"""Sets result/score values if correct answer or not and creates a new round"""
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


"""Starts a new game"""
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

    # displays player's turn
    info("Player Turn", current_player + "'s turn.")
    
    # restarts game
    setup_round()
    
    # starts new timer
    timer.repeat(1000, counter)


"""Sets up grids"""
def set_grids():
    global pictures
    global buttons

    # creates grids
    for x in range(0,3):
        for y in range(0,3):
            picture = Picture(pictures_box, grid=[x,y])
            pictures.append(picture)

            button = PushButton(buttons_box, grid=[x,y])
            buttons.append(button)


"""Sets names and starts game"""
def set_names():
    global player_one
    global player_two
    global player_one_name
    global player_two_name
    global current_player

    player_one = player_one_name.value
    player_two = player_two_name.value

    random_player = randint(1,2)
    if random_player == 1:
        current_player = player_one
    else:
        current_player = player_two

    player_name_window.hide()

    # displays player's turn
    info("Player Turn", current_player + "'s turn.")

    # sets up grids
    set_grids()

    # starts timer and sets round up
    timer.value = game_timer
    timer.repeat(1000, counter)
    setup_round()


"""Sets a round up"""
def setup_round():
    global pictures
    global buttons

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


app = App("emoji match", width=420, height=574)

# leader board window setup
leaderboard = Window(app, title="High Scores")
leaderboard.hide()

# sets up widgets for player name entry and displays rules
player_name_window = Window(app, title="Enter player names")
Text(player_name_window, "\n")
player_box = Box(player_name_window)
player_one_label = Text(player_box, text="Player one: ", align="left")
player_one_name = TextBox(player_box, align="left")
player_two_label = Text(player_box, text="  Player two: ", align="left")
player_two_name = TextBox(player_box, align="left")
Text(player_name_window, "\n")
PushButton(player_name_window, text="Start Game", command=set_names)
Text(player_name_window, "\n\nEmoji Matching Game Rules", size=18)
Text(player_name_window, "- There is exactly one emoji that is in both top and bottom grids")
Text(player_name_window, "- Click on the button in the bottom grid that matches")
Text(player_name_window, "- Correct responses grant you one point")
Text(player_name_window, "- Incorrect responses take away one point")
Text(player_name_window, "- 3 correct answers in a row awards bonus time of 10 seconds")
Text(player_name_window, "- The game ends when your time runs out and the next player goes")
Text(player_name_window, "\n\nCreated by Troy Martin - 2019")
Text(player_name_window, "beef.erikson.studios@gmail.com")

# sets up game widgets
rounds_played = Text(app, text="Rounds played: " + str(rounds))
result = Text(app)
game_box = Box(app)
pictures_box = Box(game_box, layout="grid")
buttons_box = Box(game_box, layout="grid")

# setup for emoji directory and creates empty list to populate
emojis_dir = "emojis"
emojis = []

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

# starts app
app.display()
