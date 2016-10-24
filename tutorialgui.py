from Tkinter import *

# ------------------------------------------------------------------------------
# root = Tk()
#
# mycolor = '#%02x%02x%02x' % (230, 230, 230)
#
# root.configure(bg=mycolor)
#
# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# button1 = Button(topFrame, text="Click me!")
# button2 = Button(topFrame, text="Click me!")
# button3 = Button(bottomFrame, text="Click me!")
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=BOTTOM)
#
# root.mainloop()
# ------------------------------------------------------------------------------
# root = Tk()
#
# bgcolor = '#%02x%02x%02x' % (230, 230, 230)
# root.configure(bg=bgcolor)
#
#
#
# one = Label(root, text = "one", bg="red", fg="black")
# one.pack(fill=Y)
# two = Label(root, text = "one", bg="blue", fg="green")
# two.pack(fill=X)
# three = Label(root, text = "three", bg="black", fg="green")
# three.pack(fill=Y, side=LEFT)
#
# root.mainloop()
# ------------------------------------------------------------------------------
# Entry met columns!
# root = Tk()
#
# label_0 = Label(root, text="Name:")
# label_1 = Label(root, text="Password:")
# entry_0 = Entry(root)
# entry_1 = Entry(root)
# check_0 = Checkbutton(root, text="Keep me logged in")
#
# label_0.grid(row=0, sticky=E)
# label_1.grid(row=1, sticky=E)
# entry_0.grid(row=0, column=1)
# entry_1.grid(row=1, column=1)
# check_0.grid(columnspan=2)
#
# root.mainloop()
# ------------------------------------------------------------------------------
# root = Tk()
#
# def printName() :
#     print "YEAAH NIGGAH"
#
# # def printName(event) : # Werkt minder goed....
# #     print "YEAAH NIGGAH"
#
# button_0 = Button(root, command=printName, text="Press me for print")
# # button_0 = Button(root, command=printName, text="Press me for print") # Werkt minder goed...
# # button_0.bind("<Button>", printName) # Werkt minder goed...
#
# button_0.grid()
#
# root.mainloop()
# ------------------------------------------------------------------------------
# root = Tk()
#
# def leftClick(event) :
#     print "Left Click!"
#
# def rightClick(event) :
#     print "Right Click!"
#
# frame = Frame(root, width=300, height=250)
# frame.bind("<Button-1>", leftClick)
# frame.bind("<Button-3>", rightClick)
#
# frame.pack()
#
# # Test dit met een muis...
#
# root.mainloop()
# ------------------------------------------------------------------------------
# class GUI:
#     def __init__(self, master) :
#         frame = Frame(master)
#         frame.pack()
#
#         self.printButton = Button(frame, text="YEAH NIGGAH", command=self.printMessage)
#         self.printButton.pack(side=LEFT)
#
#         self.quitButton = Button(frame, text="QUIT", command=frame.quit)
#         self.quitButton.pack(side=LEFT)
#
#     def printMessage(self) :
#         print "YEAH NIGGAH"
#
# root = Tk()
# g = GUI(root)
# root.mainloop()
# ------------------------------------------------------------------------------
class GUIclass :
    def __init__(self, master) :
        mainFrame = Frame(master)

        self.menu = Menu(mainFrame)
        self.config(menu=self.menu)

root = Tk()
gui = GUIclass(root)
root.mainloop()
