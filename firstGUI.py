from guizero import App, Text
app = App(title="This is my fist GUI")

firstmessage = Text(app, text="This is big text")
secondmessage = Text(app, text="This is green")
thirdmessage = Text(app, text="This is red")

firstmessage.text_size = 40
secondmessage.bg = "green"
thirdmessage.bg = "red"
thirdmessage.font = "Courier"

app.display()