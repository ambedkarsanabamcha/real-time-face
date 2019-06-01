from tkinter import *
import os
root = Tk()
root.geometry("600x300+300+200")
frame = Frame(root, width=300, height=250)

thelabel = Label(frame, text="Hi this is new")
thelabel.pack()

def recog():
    execfile("face_recognition.py")


button1 = Button(frame, text="Capture the fAcE")
button2 = Button(frame, text="Train the Image")
button3 = Button(frame, text="Recognize FACE", command=recog)
button4 = Button(frame, text="QUIT", command=root.quit)

button1.pack()
button2.pack()
button3.pack()
button4.pack()
frame.pack()
root.mainloop()
