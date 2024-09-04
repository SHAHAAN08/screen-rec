from tkinter import *
import pyscreenrec

# Create the main window
root = Tk()
root.geometry("400x600")
root.title("Screen Recorder")
root.config(bg="#fff")
root.resizable(False, False)

# Initialize the screen recorder
rec = pyscreenrec.ScreenRecorder()

# Set window icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

# Background images
image1 = PhotoImage(file="yellow.png")
Label(root, image=image1, bg="#fff").place(x=-2, y=35)
image2 = PhotoImage(file="blue.png")
Label(root, image=image2, bg="#fff").place(x=223, y=200)

# Title label
lbl = Label(root, text="Screen Recorder", bg="#fff", font="arial 15 bold")
lbl.pack(pady=20)

# Recording image
image3 = PhotoImage(file="recording.png")
Label(root, image=image3, bd=0).pack(pady=30)

# Functions to control the screen recorder
def start_recording():
    rec.start_recording("my_recording.mp4", 23)  # Set to 60 FPS for higher quality recording

def pause_recording():
    rec.pause_recording()

def resume_recording():
    rec.resume_recording()

def stop_recording():
    rec.stop_recording()

# Buttons
start = Button(root, text="Start", font="arial 22", bd=0, command=start_recording)
start.place(x=140, y=250)

image4 = PhotoImage(file="pause.png")
pause = Button(root, image=image4, bd=0, bg="#fff", command=pause_recording)
pause.place(x=50, y=450)

image5 = PhotoImage(file="resume.png")
resume = Button(root, image=image5, bd=0, bg="#fff", command=resume_recording)
resume.place(x=150, y=450)

image6 = PhotoImage(file="stop.png")
stop = Button(root, image=image6, bd=0, bg="#fff", command=stop_recording)
stop.place(x=250, y=450)

# Run the application
root.mainloop()
