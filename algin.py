from guizero import App, Text, Box

app = App(title="Align")
box = Box(app, width='fill', height='fill')

top_text = Text(app, text='at the top', align='bottom', height='fill')
bottom_text = Text(app, text='at the bottom', align='top')
left_text = Text(app, text='at the left', align='right', width='fill')
left_text1 = Text(box, text='at the left again', align='right', width='fill')
right_text = Text(app, text='at the right', align='left')

app.display()
