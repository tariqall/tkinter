from tkinter import *

def submit():
  username = entry.get()
  print("Hello: " + username)
  entry.config(state=DISABLED)

# In Delete Function, 0 means start of index and END means Last Character. So Entire Content Will Delete
def delete():
  entry.delete(0,END)

#The Entire Length Is Taken And -1 Cause The Second Last Character Of String To Be The Extent Upto Available For Deletation
def backspace():
  entry.delete(len(entry.get())-1, END)

def display():
  if(x.get() == 1):
    print('You Agreed.... :)')
  else:
    print('You Disagree... :(')

window = Tk()

ceenfood = PhotoImage(file='ceenfood_rs.png')

x = IntVar()
# x = BooleanVar()

entry = Entry(window, 
              font=('Arial', 50),
              show="*",
              fg='#00FF00',
              bg='black'
             )
entry.insert(0,'Pakistan')
#entry.config(state=DISABLED)
#entry.config(show='X')

entry.pack(side=LEFT)

checkbox_button = Checkbutton(window,
                              text="Do You Agree? ",
                              font=('Arial', 10),
                              variable=x,
                              command=display,
                              fg='black',
                              bg='white',
                              onvalue=1,
                              offvalue=0,
                              activeforeground='black',
                              activebackground='white',
                              padx=25,
                              pady=10,
                              image=ceenfood,
                              compound='left'
                             )
checkbox_button.pack()

submit_button = Button(window, text='Submit', command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text='Delete', command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text='Back Space', command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()