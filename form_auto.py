from guizero import App, Box, Text, TextBox

app = App()

box_fname = Box(app, width="fill")
lbl_fname = Text(box_fname, text="First name", align="left", width=10)
txt_fname = TextBox(box_fname, align="left")

box_sname = Box(app, width="fill")
lbl_sname = Text(box_sname, text="Surname", align="left", width=10)
txt_snmae = TextBox(box_sname, align="left")

box_dob = Box(app, width="fill")
lbl_dob = Text(box_dob, text="Date of birth", align="left", width=10)
txt_dob = TextBox(box_dob, align="left")

app.display()
