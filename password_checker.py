import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(event=None):
    password = password_entry.get()
    strength = 0
    remarks = ""
    percentage = 0
    
    # Conditions for password strength
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    
    percentage = (strength / 5) * 100
    
    # Assigning strength levels
    if strength == 5:
        remarks = "Excellent 🔥"
        color = "green"
    elif strength == 4:
        remarks = "Strong ✅"
        color = "blue"
    elif strength == 3:
        remarks = "Moderate ⚠️"
        color = "orange"
    elif strength == 2:
        remarks = "Weak ❌"
        color = "red"
    else:
        remarks = "Very Weak ❌❌"
        color = "darkred"
    
    strength_label.config(text=f"{remarks} ({percentage:.0f}%)", fg=color)
    
    if percentage == 100:
        message_label.config(text="🎉 Congrats! Your password is strong!", fg="green")
    else:
        message_label.config(text="")

def clear_fields():
    password_entry.delete(0, tk.END)
    strength_label.config(text="")
    message_label.config(text="")

# GUI Setup
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x350")
root.configure(bg="white")

heading = tk.Label(root, text="🔒 Password Strength Checker 🔒", font=("Arial", 16, "bold"), bg="white", fg="black")
heading.pack(pady=10)

frame = tk.Frame(root, bg="white")
frame.pack(pady=10)

label = tk.Label(frame, text="Enter Password:", font=("Arial", 12), bg="white", fg="black")
label.pack()

password_entry = tk.Entry(frame, font=("Arial", 14), show="", width=25)  # Password visible
password_entry.pack(pady=5)
password_entry.bind("<KeyRelease>", check_password_strength)  # Real-time checking

strength_label = tk.Label(frame, text="", font=("Arial", 14, "bold"), bg="white")
strength_label.pack()

message_label = tk.Label(frame, text="", font=("Arial", 12, "bold"), bg="white")
message_label.pack()

clear_btn = tk.Button(frame, text="Clear", command=clear_fields, font=("Arial", 12), bg="#D3D3D3", fg="black", padx=10, pady=5)
clear_btn.pack(pady=5)

root.mainloop()
