import random as rdm
from tkinter import *
from queue import *

# -------------------------------------------------------------------------------------------------------------------
# Indicates a random chord repeatedly after a certain interval. Chords just displayed can be delayed for further
# display for a certain amount of time.
# -------------------------------------------------------------------------------------------------------------------

maj_chords = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']

chords = maj_chords
# Interval after which new chord is shown (ms)
interval = 8000
# Iterations a shown chord should be skipped
delay_iter = 5

# Chords to be temporarily exempted
delayed_chords = Queue(maxsize=delay_iter)

# Define a counter that refreshes label after x secs
def refresh_label(label):
    def refresh():
        # Show a random chord in label
        number = rdm.randrange(1, len(chords), 1)
        label.config(text=chords[number],
                     font="Helvetica 240 bold italic"
                     )
        label.pack()

        # Manage delayed chords
        delayed_chords.put(chords.pop(number))
        if delayed_chords.full():
            chords.append(delayed_chords.get())

        label.after(interval, refresh)

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
