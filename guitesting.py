# ------------------------------------------------------------------------------
# from Tkinter import *           # Importing the Tkinter (tool box) library
# root = Tk()                     # Create a background window
#                                 # Create a list
# li = 'Variable3 Variable2 Variable1'.split()
# listb = Listbox(root)           # Create a listbox widget
# for item in li:                 # Insert each item within li into the listbox
#     listb.insert(0,item)
#
# listb.pack()                    # Pack listbox widget
# root.mainloop()                 # Execute the main event handler
# ------------------------------------------------------------------------------
# from Tkinter import *           # Import the Tkinter library
# root = Tk()                    # Create a background window object
#                                 # A simple way to create 2 lists
# li     = ['Carl','Patrick','Lindsay','Helmut','Chris','Gwen']
# movie  = ['God Father','Beauty and the Beast','Brave heart']
# listb  = Listbox(root)          # Create 2 listbox widgets
# listb2 = Listbox(root)
# for item in li:                 # Insert each item inside li into the listb
#     listb.insert(0,item)
#
# for item in movie:              # Do the same for the second listbox
#     listb2.insert(0,item)
#
# listb.pack()                    # Pack each listbox into the main window
# listb2.pack()
# root.mainloop()                 # Invoke the main event handling loop
# ------------------------------------------------------------------------------
# from Tkinter import *
#
# def Pressed():                          #function
#         print 'buttons are cool'
#
# root = Tk()                             #main window
# button = Button(root, text = 'Press', command = Pressed)
# button.pack(pady=50, padx = 50)
# root.mainloop()
# ------------------------------------------------------------------------------
#                             #Souce section   1
#
# #mandatory for unix and linux
# #---------------------------------------------------------------
#
# from Tkinter import *       #This library give us windows and buttons
# from random import *        #This library allows us to generate random numbers
#                             #import library section   2
#
# #
# #What not to use???
# #---------------------------------------------------------------
#
# def one_to_ten():
#     ran = uniform(1,10)
#     print ran
#
# def GoWork():           # def starts a function, or define a function
#     sum = 3*5
#     print sum               #Function section   3
#
# #----------------------------------------------------------------
#
#
#
#                             #Code section    4
#
# window = Tk()      #i am the parent, button = child
#
# stacy = Button(window, text = 'yoyo', command = one_to_ten)
# #A rose with any other name would be just as sweet
#
#
# stacy.pack()        #you can name it after your fish (ignored)
# window.mainloop()         #you can use your fish's name
# ------------------------------------------------------------------------------
# from Tkinter import *
#
# def Call():
#         # lab= Label(root, text = 'You pressed\nthe button')
#         lab= Label(root, text = 'You pressed the button')
#         lab.pack()
#         button['bg'] = 'blue'
#         button['fg'] = 'white'
#
# root = Tk()
# root.geometry('100x110+350+70')
# button = Button(root, text = 'Press me', command = Call)
# button.pack()
#
# root.mainloop()
# ------------------------------------------------------------------------------
# from Tkinter import *           #This interface allow us to draw windows
#
#
# def DrawList():
#         plist = ['Liz','Tom','Chi']
#
#         for item in plist:
#                 listbox.insert(END,item);
#
#
# root = Tk()                     #This creates a window, but it won't show up
#
# listbox = Listbox(root)
# button = Button(root,text = "press me",command = DrawList)
#
# button.pack()
# listbox.pack()                  #this tells the listbox to come out
# root.mainloop()                 #This command will tell the window come out
# ------------------------------------------------------------------------------
# from WCK import Widget
#
# class CheckerboardWidget(Widget):
#
#     def ui_handle_clear(self, draw, x0, y0, x1, y1):
#         pass # ui_handle_repair updates the entire widget
#
#     def ui_handle_repair(self, draw, x0, y0, x1, y1):
#         # draw a 2x2 checkerboard pattern
#
#         # calculate widget center
#         cx = (x0 + x1) / 2; cy = (y0 + y1) / 2
#
#         # allocate brushes
#         white = self.ui_brush("white")
#         black = self.ui_brush("black")
#
#         # draw tiles
#         draw.rectangle((x0, y0, cx, cy), white)
#         draw.rectangle((cx, y0, x1, cy), black)
#         draw.rectangle((x0, cy, cx, y1), black)
#         draw.rectangle((cx, cy, x1, y1), white)
#
# from Tkinter import *
#
# root = Tk()
#
# w = CheckerboardWidget(root)
# w.pack(fill=BOTH, expand=1)
#
# root.mainloop()
# ------------------------------------------------------------------------------
