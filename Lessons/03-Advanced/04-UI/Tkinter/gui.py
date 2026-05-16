
from tkinter import *

root = Tk()	# creates a blank window

# ----- EXAMPLE 1 -----
# theLabel = Label(root, text="Hello World")	# creates a label inside the root window
# theLabel.pack()	# packs the label into the window wherever it fits


# ----- EXAMPLE 2 -----
# def printText():
# 	print("Button clicked")

# topFrame = Frame(root)	# makes a container in the root window
# topFrame.pack() 	# place the top frame
# bottomFrame = Frame(root)	# makes a container that goes below the top frame
# bottomFrame.pack(side=BOTTOM)	# place the bottom frame below the top frame

# button1 = Button(topFrame, text="Button 1", fg="black", width=10, height=2, command=printText)	# creates a button in the top frame 
# button2 = Button(topFrame, text="Button 2", fg="blue")	# creates a button in the top frame 
# button3 = Button(bottomFrame, text="Button 3", fg="black")	# creates a button in the bottom frame 
# button4 = Button(bottomFrame, text="Button 4", fg="red")	# creates a button in the bottom frame
# button1.pack(side=LEFT)
# button2.pack(side=RIGHT)
# button3.pack(side=LEFT)
# button4.pack(side=RIGHT)


# ----- EXAMPLE 3 -----
# button1 = Button(root, text="Button 1", fg="black", width=10, height=2, command=printText)	# creates a button in the top frame 
# button2 = Button(root, text="Button 2", fg="blue")	# creates a button in the top frame 
# button1.pack(fill=X) 	# fill X fills the X axis 
# button2.pack(side=LEFT, fill=Y) # fill Y fills the Y axis 


# ----- EXAMPLE 4 -----
# title = Label(root, text="Login")
# usernameLabel = Label(root, text="Username")
# passwordLabel = Label(root, text="Password")
# nameEntry = Entry(root)
# passwordEntry = Entry(root)
# check = Checkbutton(root, text="Remember my login")

# title.grid(columnspan=2, row=0)
# usernameLabel.grid(row=1, column=0, sticky=E)	# places the label in the first row and column of the grid (column is optional)
# 	# sticky takes N,E,S,W instead of right or left align 
# passwordLabel.grid(row=2, sticky=E)	# column 0 is assumed if not specified
# nameEntry.grid(row=1,column=1)
# passwordEntry.grid(row=2,column=1)
# check.grid(columnspan=2, row=3)


# ----- EXAMPLE 5 -----
# def printLeft(event):
# 	print("Left clicked")

# def printRight(event):
# 	print("Right clicked")

# def printMiddle(event):
# 	print("Scrollwheel clicked")

# button1 = Button(root, text="Print", width=10, heigh=3)
# button1.bind("<Button-1>", printLeft)	#button-1 is left mouse click, printLeft runs when button is left clicked
# button1.bind("<Button-2>", printRight)	#button-2 is right mouse click, printRight runs when button is right clicked
# button1.bind("<Button-3>", printMiddle)	#button-3 is scrollwheel click, printMiddle runs when button is scrollwheel clicked
# button1.pack()


# ----- EXAMPLE 6 -----
# class windowButtons:
# 	def __init__(self, master):
# 		frame = Frame(master)
# 		frame.pack()

# 		self.printButton = Button(frame, text="Print Message", width = 15, height = 3, command=self.printMessage)	# prints to the console
# 		self.printButton.pack(side=LEFT)

# 		self.quitButton = Button(frame, text="Quit", width = 5, height = 3, command=frame.quit)	# closing the window
# 		self.quitButton.pack(side=LEFT)

# 	def printMessage(self):
# 		print("button clicked")

# b = windowButtons(root)	# creates an object of the class and creates the window


root.mainloop()	# runs the GUI until closed out of