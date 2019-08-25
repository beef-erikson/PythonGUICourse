from guizero import App, Text, PushButton

counter = 120

"""Counts down and changes background color of the button every second"""
def countdown():
    global counter
    counter -= 1
    
    if not counter <= 0:
        text.value = str(int(counter / 60)) + " minutes " + str(counter % 60) + " seconds"
    else:
        text.value = "Game Over"

    if button.bg == "black":
        button.bg = "white"
    else:
        button.bg = "black"

app = App("Text size")

text = Text(app, str(int(counter / 60)) + " minutes " + str(counter % 60) + " seconds")
button = PushButton(app, text="")
button.bg = "black"

text.repeat(1000, countdown)

app.display()