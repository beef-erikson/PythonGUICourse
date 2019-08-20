from guizero import App, Text, TextBox

app = App(layout="grid")

lbl_fname = Text(app, text="First name", grid=[0,0])
txt_fname = TextBox(app, grid=[1,0])

lbl_sname = Text(app, text="Surname", grid=[0,1])
txt_sname = TextBox(app, grid=[1,1])

lbl_dob = Text(app, text="Date of birth", grid=[0,2])
txt_dob = TextBox(app, grid=[1,2])

app.display()
