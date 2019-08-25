from guizero import App, TextBox, Text, ButtonGroup, PushButton, Combo, CheckBox, ListBox, Picture, Box
import PIL

# Sets up app
app = App(title="Hero-o-matic")
app.height=400
app.width=400
app.bg = 'black'

box1 = Box(app, align='left')
box1.bg = 'dark slate gray'
box2 = Box(app, border=1)
box2.bg = 'slategray3'
box3 = Box(app)
box3.bg = 'dark slate gray'
box4 = Box(app, width='fill')
box4.bg = 'green'
box4.font = 'New Times Roman'

"""Event functions"""
def make_hero_name():
    adjective = cmb_adjective.value
    colour = txt_colour.value
    animal = cmb_animal.value
    surname = lst_surname.value
    hero = adjective + ' ' + colour + ' ' + animal + ' ' + surname
    if (chk_power1.value):
        power = chk_power1.text
    if (chk_power2.value):
        power = chk_power2.text
    if (chk_power3.value):
        power = chk_power3.text
    lbl_output.value = "You are... The " + hero + " that " + power + "."


"""Enable dark mode"""
def make_darkmode():
    app.bg = "Black"
    app.text_color = "White"

# GUI Widgets
Picture(box2, image="./GUICourse/me.png", height=50, width=50)

chk_darkmode = CheckBox(box2, text="Dark Mode", command=make_darkmode) 

message1 = Text(box3, text="Choose an adjective...")
cmb_adjective = Combo(box3, options=["Amazing", "Bonny", "Charming", "Delightful", "Sad", "Spectacular", "Happy"], 
    selected="Amazing")

message2 = Text(box3, text="Enter a colour")
txt_colour = TextBox(box3)

message3 = Text(box3, text="Pick an animal")
cmb_animal = Combo(box3, options=["Aardvark", "Badger", "Cat", "Dolphin", "Velociraptor", "Dog", "Elephant", "Lizard"],
    selected="Aardvark")

message4 = Text(box3, text="Add a super-power")
chk_power1 = CheckBox(box3, text="can fly",)
chk_power2 = CheckBox(box3, text="has x-ray vision")
chk_power3 = CheckBox(box3, text="reads minds")

message5 = Text(box1, text="Choose a surname")
lst_surname = ListBox(box1, items=["the First", "the Second", "the Third", "the Fourth", "the Fifth",
 "the Sixth", "the Seventh", "the Eigth", "the Ninth"], selected="the First", height='fill', width='fill')

btn_make_name = PushButton(box4, text="Make me a hero name", command=make_hero_name)
lbl_output = Text(box4, text="A hero name will appear here")

# Sets up display and listener
app.display()
