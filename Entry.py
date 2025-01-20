from tkinter import *
def submit():
  username = entry.get()
  print("Hello: "+username)
window = Tk()
entry = Entry(window, font=('Arial', 50))
entry.pack(side=LEFT)
submit_button = Button(window, text='Submit', command=submit)
submit_button.pack(side=RIGHT)
window.mainloop()