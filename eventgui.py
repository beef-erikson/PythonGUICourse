from guizero import App, TextBox, PushButton, Text, info
app = App()

def btn_go_clicked():
    info("Greetings","Hello, your name is " + txt_name.value + " and you like " + txt_animal.value + ".")

def btn_hello_clicked():
    info("Hello","Hey there! Hope your day is going well!")

lbl_name = Text(app, text="Hello. What's your name?")
txt_name = TextBox(app)
lbl_animal = Text(app, text="What's your favorite animal?")
txt_animal = TextBox(app)

btn_go = PushButton(app, command=btn_go_clicked, text="Done")
btn_hello = PushButton(app, command=btn_hello_clicked, text="Hello Computer")

app.display()
