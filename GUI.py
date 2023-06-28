import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
import subprocess

def capture_faces(person_name):
    subprocess.run(["python", "D:\\LaSalle\Computer architecture\Project\FaceCaptureV2.py",person_name])

def train_model():
    subprocess.run(["python", "D:\\LaSalle\Computer architecture\Project\TrainingRF.py"])

def recognize_faces():
    subprocess.run(["python", "D:\\LaSalle\Computer architecture\Project\FacialRecognition.py"])

def create_user():
    person_name = entry.get()
    if person_name:
        capture_faces(person_name)
    else:
        show_message("Please enter a valid name.")
    

def show_message(message):
    messagebox.showinfo("Message", message)

window = tk.Tk()
window.title("Face Recognition System")
window.configure(bg="black") 

title_font = tkfont.Font(family="Arial", size=20, weight="bold")

label = tk.Label(window, text="Security System", fg="white", bg="black", font=title_font)
label.pack(pady=10)

entry = tk.Entry(window, justify="center", width=20, bg="white", fg="black")
entry.pack(pady=5)

button_frame = tk.Frame(window, bg="black")
button_frame.pack(pady=10)

create_user_button = tk.Button(window, text="Create User", command=create_user, fg="black", bg="white")
train_button = tk.Button(window, text="Train Model", command=train_model, fg="black", bg="white")
recognize_button = tk.Button(window, text="Recognize Faces", command=recognize_faces, fg="black", bg="white")
quit_button = tk.Button(window, text="Quit", command=window.quit, fg="black", bg="white")

create_user_button.pack(pady=10)
train_button.pack(pady=10)
recognize_button.pack(pady=10)
quit_button.pack(pady=10)

window.mainloop()
