from habit_classes import Habit, HabitTracker, Storage
import customtkinter as ctk


app = ctk.CTk()

def add_habit():
    add_frame.pack(pady=10)

add_frame = ctk.CTkFrame(app)
name_entry = ctk.CTkEntry(
    add_frame,
    placeholder_text="Habit name"
)
name_entry.pack(padx=20, pady=10)

goal_entry = ctk.CTkEntry(
    add_frame,
    placeholder_text="Goal streak"
)
goal_entry.pack(padx=20, pady=10)

def cancel_add():
    add_frame.pack_forget()
cancel_button = ctk.CTkButton(
    add_frame,
    text="Cancel",
    command=cancel_add
)
cancel_button.pack(pady=10)

app.title("Habit Garden")
app.geometry("900x600")
title = ctk.CTkLabel(
    app,
    text="🌱 Habit Garden",
    font=("Arial", 32, "bold")
)

title.pack(pady=30)
add_habit_button = ctk.CTkButton(
    app,
    text="Add Habit",
    font=("Arial", 20),
    command=add_habit
)
add_habit_button.pack(pady=20)

app.mainloop()