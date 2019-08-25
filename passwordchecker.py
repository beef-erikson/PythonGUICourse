from guizero import App, Text, TextBox, PushButton, info

app = App()
app.title = "Password Verification"


"""Checks password"""
def btn_checkpass_clicked():
    if (txt_firstpass.value == txt_secondpass.value):
        info("Match","The passwords match!")
    else:
        info("Not a Match","The passwords do not match.")

Text(app, text="")
lbl_firstpass = Text(app, text="Enter password:")
txt_firstpass = TextBox(app)
lbl_secondpass = Text(app, text="Enter password again:")
txt_secondpass = TextBox(app)
Text(app, text="")

btn_checkpass = PushButton(app, command=btn_checkpass_clicked, text="Check Password")

app.display()