import tkinter as tk
from tkinter import messagebox
import random


class GameWindow:

    def __init__(self):
        self.window = tk.Tk
        self.window.title("Game of Nim")
        self.window.geometry("800x600")
        self.window.configure(bg="#e8ede9")
        self.canvas = tk.canvas(self.window, width=600, height=300, bg="#faf5fa")

    def start(self):
        self.window.mainloop()
class GameUI:
    def __init__(self, game_window):
        self.window = game_window.window
        self.canvas = game_window.canvas
        self.user_score = 0
        self.computer_score = 0
        self.remaining_balls = 0
        self.setup_ui()
    def setup_ui(self):
        tk.Label(self.window, text="NIM WARS", font=("Helvetica", 20),bg="#e8ede9", fg="#440c57"). pack(pady=20)
        self.score_label = tk.Label(self.window, text="Score:\nUser - 0\nComputer - 0", bg="#e8ede9", fg="#440c57")
        self.score_label.pack(pady=10)
        self.balls_entry = tk.Entry(self.window, font=("Helvetica", 12))
        self.score_label.pack(pady=10)
        tk.Button(self.window, text="Start Game", command=self.start_game, bg="#440c57", fg="white").pack(pady=5)
        tk.Button(self.window, text="reset Game", command=self.reset_game, bg="#440c57", fg="white").pack(pady=5)
        tk.Button(self.window, text="Instructions", command=self.show_instructions, bg="#440c57", fg="white").pack(pady=5)

    def show_instructions(self):






