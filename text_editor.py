from guizero import App, TextBox, PushButton, Box, Combo, Slider, Text, MenuBar

# Properties
is_edited = False


"""Opens file"""
def open_file():
    with open(file_name.value, "r") as file:
        editor.value = file.read()


"""Saves file"""
def save_file():
    with open(file_name.value, "w") as file:
        file.write(editor.value)
    global is_edited
    is_edited = False


"""Text has been edited"""
def text_edited():
    global is_edited
    is_edited = True

"""Exits program"""
def exit_app():
    if is_edited:
        if app.yesno("Close", "File has not been saved, are you sure you want to quit?"):
            app.destroy()
    else:
        app.destroy()


"""Changes font"""
def change_font():
    editor.font = font.value


"""Changes font size"""
def change_font_size():
    editor.text_size = size.value
    editor.resize(1, 1)
    editor.resize('fill', 'fill')
        

"""Changes font color"""
def change_font_color():
    editor.text_color = color.value


"""Change background color"""
def change_background_color():
    editor.bg = color_background.value


"""Enables Dark Mode"""
def dark_mode():
    app.bg = 'black'
    app.text_color = 'white'
 

# Initializations
app = App(title="Simple Text Editor")
app.width = 800

# Menu Bar
menubar = MenuBar(app,
    toplevel=['File','Edit'],
    options=[
        [ ["Open", open_file], ["Save", save_file], ["Close", exit_app] ],
        [ ["Set Background Color", change_background_color], ["Enable dark mode", dark_mode] ]
    ])

# Top panel for file management
file_operations = Box(app, align='top', width='fill', border=True)
file_name = TextBox(file_operations, text='text_file.txt', width=50, align='left')

# Textbox for displaying/editing text
editor = TextBox(app, multiline=True, height='fill', width='fill', command=text_edited)

# Bottom panel for preferences
preferences_controls = Box(app, align='bottom', width='fill', border=True)

font = Combo(preferences_controls, options=['Courier', 'Times New Roman', 'Verdana'], align='left', command=change_font)
color = Combo(preferences_controls, options=['red', 'black', 'green', 'yellow', 'blue', 'purple', 'pink', 'white'], 
    align='left', selected='black', command=change_font_color)
text_size = Text(preferences_controls, align='left', text='  Font Size: ')
size = Slider(preferences_controls, align='left', command=change_font_size, start=10, end=22)

color_background = Combo(preferences_controls, align='right', selected='white',
    options=['red', 'black', 'green', 'yellow', 'blue', 'purple', 'pink', 'white'])
text_background = Text(preferences_controls, align='right', text='  Background Color: ')


# Initializes display
app.display()   
