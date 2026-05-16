from tkinter import *
import tkinter.messagebox

def doNothing():
	print("Nothing")

def quitMessage():
	#tkinter.messagebox.showinfo('Exit warning', "Are you sure you want to quit?")
	userQuitResponse = tkinter.messagebox.askquestion('Exitting Application', 'Are you sure you want to quit?') 

	if userQuitResponse == 'yes':
		root.destroy()

root = Tk()

root.protocol('WM_DELETE_WINDOW', quitMessage)	# override pressing the x button to close the window

# ----- Menu -----

menuHead = Menu(root)
root.config(menu=menuHead)

fileMenu = Menu(menuHead)
menuHead.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Document", command=doNothing)
fileMenu.add_command(label="New from Template", command=doNothing)
fileMenu.add_command(label="Open", command=doNothing)
fileMenu.add_command(label="Open Recent", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=doNothing)
fileMenu.add_command(label="Save", command=doNothing)
fileMenu.add_command(label="Save As", command=doNothing)
fileMenu.add_command(label="Save as Template", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Print", command=doNothing)
fileMenu.add_command(label="Share", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quitMessage)

editMenu = Menu(menuHead)
menuHead.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=doNothing)
editMenu.add_command(label="Copy", command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Paste", command=doNothing)
editMenu.add_command(label="Paste Special", command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Clear", command=doNothing)
editMenu.add_command(label="Select All", command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Find", command=doNothing)


# ----- Toolbar -----

toolbar = Frame(root)

fileButton = Button(toolbar, text="New File", command=doNothing)
fileButton.pack(side=LEFT, padx=2, pady=2)
exportButton = Button (toolbar, text="Export Project", command=doNothing)
exportButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)


# ----- Status Bar -----

status = Label(root, text="Preparing to do nothing...", bd = 1, relief = SUNKEN, anchor = W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()