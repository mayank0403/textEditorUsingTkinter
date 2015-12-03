from Tkinter import *
import tkFileDialog
from ScrolledText import *

def donothing():
    print "yeah"

def closeIt():
    root.destroy()

def about():
    newWin = Toplevel(root)
    l = Label(newWin, text = "Made by Mayank Rathee, Indian Institute of Technology (BHU), Varanasi")
    l.pack()

def openFile():
    open = tkFileDialog.askopenfile(parent=root, mode='r', title = "Open a file")
    namestr = str(open)
    print namestr
    cnt = 0
    count = 0
    i=0
    global name
    #name = ''
    while count<2:
        if namestr[i] is chr(39):
            print i
            count = count+1
            i = i+1
            continue
        if count >= 1 and count<2:
            name = name + namestr[i]
        i=i+1
    print name
    contents = open.read()
    textBox.insert('1.0', contents)
    open.close()
    #return name

def saveasfile():
    open = tkFileDialog.asksaveasfile(parent = root, mode= 'w')
    contents = textBox.get('0.0', END)
    open.write(contents)
    open.close()

def savefile():
    ope = open(name, mode = 'w')
    contents = textBox.get('0.0', END)
    ope.write(contents)
    ope.close()


root = Tk()
global name
name = ''
#print name
textBox = ScrolledText(root)
textBox.pack()
menubar = Menu(root)

filemenu = Menu(menubar, tearoff = 1)
filemenu.add_command(label = "Open", command = openFile)
filemenu.add_cascade(label = "Save", command = savefile)
filemenu.add_cascade(label = "Save As", command = saveasfile)
filemenu.add_cascade(label = "About", command = about)
filemenu.add_cascade(label = "Exit", command = closeIt)

menubar.add_cascade(label = "Menu", menu = filemenu)
root.config(menu=menubar)
root.mainloop()
