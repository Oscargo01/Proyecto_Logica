from Tkinter import *  # or tkinter if you use Python3

root = Tk()

label_1 = Label(master=root, text='Name 1')
label_2 = Label(master=root, text='Name 2')
label_3 = Label(master=root, text='Name 3')
label_4 = Label(master=root, text='Name 4')

label_1.grid(row=0)
label_2.grid(row=1)
label_3.grid(row=2)  # this is the 2nd
label_4.grid(row=4)  # this is the 4th

root.rowconfigure(index=3, weight=1)  # add weight to the 3rd!
root.mainloop()