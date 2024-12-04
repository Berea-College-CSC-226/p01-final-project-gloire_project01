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
        messagebox.showinfo("How to Play", "Remove 1-4 balls per turn. Avoid removing the last ball!")

    def reset_game(self):
        self.remaining_balls = 0
        self.canvas.delete("balls")
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score:\nUser - {self.user_score}\ncomputer - {self.computer_score}")

    def start_game(selfself):
        try:
            self.remaining_balls = int(self.balls_entry.get())
            if self.remaining_balls < 15:
                raise ValueError
            Balls(self.canvas, self.remaining_balls).draw()
            self.user_turn()
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number(15 or higher).")

    def user_turn(self):
        def handle_turn():
            try:
                user_input = int(user_input_entry.get())
                if not (1 <= user_input <=4):
                    raise ValueError
                self.remaining_balls -= user_input
                turn_window.destroy()
                self.update_game()
            except ValueError:
                messagebox.showerror("Error","Entry number between 1 and 4.")

        turn_window = tk.Toplevel(self.window)
        turn_window.title("Your Turn")
        tk.Lebel(turn_window, text="How many balls to remove (1-4)?").pack(pady=5)
        user_input_entry = tk.Entry(turn_window)
        user_input_entry.pack(pady=5)
        tk.Button(turn_window, text="Submit", command=handle_turn).pack(pady=5)

    def computer_turn(self):
        balls_to_remove = self.remaining_balls % 5 or random.radint(1, 4)
        self.remaining_balls -= balls_to_remove
        messagebox.showinfo("computer's Turn", f"computer removed{balls_to_remove}balls.")
        self.update_game()











