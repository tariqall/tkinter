from tkinter import *
def Order():
  print("Your Order Place Successfully")

window = Tk() # Instantiating an instance of window
window.geometry("600x400")
window.title("Ceen Food")
icon = PhotoImage(file='ceenfood_rs.png')
photo = PhotoImage(file='ceenfood_rs.png')
window.iconphoto(True,icon)
window.config(background="#f5b942")
button = Button(
                window,
                text='Order Here',
                command=Order,
                font=("Arial", 12, "bold"),
                fg="#f5b942",
                bg="black",
                activeforeground="black",
                activebackground="#f5b942",
                state=ACTIVE
                )
label = Label(window, text="Ceen Food", font=(
                                              'Arial', 40, 'bold'), 
                                              fg='black', 
                                              bg='#f5b942',
                                              relief=RAISED,
                                              bd=10,
                                              padx=20,
                                              pady=10,
                                              image=photo,
                                              compound='top'
                                              )
label.pack()
button.pack()
window.mainloop()