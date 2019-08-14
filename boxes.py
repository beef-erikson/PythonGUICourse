from guizero import App, Box, PushButton, TextBox, ListBox, Picture, Text
import PIL

app = App()
app.title = "Boxes example - Retro Style"

box1 = Box(app, align='bottom', height='50', border=1, width='fill')
box2 = Box(app, align='left', height='fill', width=150, border=2)
box3 = Box(app, align='right', height='fill', width='fill', border=2)

text_bottom = Text(box1, text='August 6, 2019', align='right')
listbox_left = ListBox(box2, items={'SNES', 'Genesis', 'NES', 'Gameboy', 'Gameboy Advance', 'Game Gear'}, height='fill',
    selected='SNES')
pic_right = Picture(box3, image='SNES.png', height=200, width=200)
textbox_right = TextBox(box3,text='The Super Nintendo Entertainment System is a 16-bit home video game console' + 
    ' developed by Nintendo that was released in 1990 in Japan and South Korea, 1991 in North America, 1992' +
    ' in Europe and Australasia, and 1993 in South America. In Japan, the system is called the Super Famicom,' +
    ' or SFC for short.', height='fill', width='fill', multiline=True)
textbox_right.tk['wrap'] = 'word'

app.display()