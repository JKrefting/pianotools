import random as rdm
from tkinter import *

maj_chords = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']

chords = maj_chords
intervall = 6000


# Define a counter that refreshes label after x secs
def refresh_label(label):
    def refresh():
        number = rdm.randrange(1, len(chords), 1)
        label.config(text=chords[number],
                     font="Helvetica 240 bold italic"
                     )
        label.pack()
        label.after(intervall, refresh)

    refresh()


# Initialise root widget
root = Tk()
root.geometry("500x500")

# Initial label
number = rdm.randrange(1, len(chords), 1)
label = Label(root,
              text=chords[number],
              font="Helvetica 240 bold italic"
              )
label.pack()

# refresh will run as soon as the mainloop starts
root.after(0, refresh_label(label))
# Start event loop
root.mainloop()
