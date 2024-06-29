# install all libraries needed
from barcode import EAN13

from barcode.writer import ImageWriter

import random

from tkinter import *

import tkinter as tk

import tkinter.messagebox


# set up the number generator and description messagebox
root = tk.Tk()

root.title("EMS: Enventory Management System")

# declare a string variable for the item description
item = tk.StringVar()


def onClick():

    # generate a random number
    number = str(random.randint(100000000000, 999999999999))

    # open the text file where the data is stored for reading and writing
    file1 = open("barcode_numbers.txt", "a+")
    file2 = open("item_title.txt", "a+")
    # do not repeat numbers
    file1.seek(0)
    if number not in file1.read():
        # have a success message show up with the barcode number
        tkinter.messagebox.showinfo("Success!", number)
        # write the number to a new line in its text file
        file1.write(number + "\n")
        # generate a barcode
        new_code = EAN13(number, writer=ImageWriter())
        # save barcode as a png with associated number
        new_code.save(number)
        # save the item description to a new line in its text file
        file2.write(number + " : " + item.get() + "\n")
    # if the number repeats, offer a messagebox error
    else:
        tkinter.messagebox.askretrycancel("ERROR", "Duplicate barcode generated. Quit or try again.")
    # close the text file
    file1.close()
    file2.close()


# window size
root.geometry('500x300')


# Item title entry box
entry = tk.Entry(root, textvariable=item, font=('calibri', 10, 'normal'))
# button that will generate the barcode and submit description
button = tk.Button(root, text="Submit and get barcode", command=onClick)



# place the button
button.pack()

# place the item description text entry box
entry.pack()

# execute the application
root.mainloop()




