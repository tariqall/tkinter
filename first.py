from tkinter import *

window = Tk() # Instantiating an instance of window
window.geometry("600x400")
window.title("Ceen Food")
icon = PhotoImage(file='ceenfood.png')

window.iconphoto(True,icon)
window.config(background="#f5b942")

label = Label(window, text="Ceen Food", font=('Arial', 40, 'bold'), fg='black', bg='#f5b942')
label.pack()
window.mainloop()