import tkinter as tk
from tkinter import messagebox
import random


class GameWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Game of Nim")
        self.window.geometry("800x600")
        self.window.configure(bg="#e8ede9")
        self.canvas = tk.Canvas(self.window, width=600, height=300, bg="#faf5fa")
        self.canvas.pack(side=tk.LEFT, padx=5, pady=5)
        self.font_default = ("Helvetica", 12)
        self.font_title = ("Helvetica", 20)

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
        tk.Label(self.window, text="NIM WARS", font=("Helvetica", 20), bg="#e8ede9", fg="#440c57").pack(pady=20)
        self.score_label = tk.Label(self.window, text="Score:\nUser - 0\nComputer - 0", bg="#e8ede9", fg="#440c57")
        self.score_label.pack(pady=10)
        self.balls_entry = tk.Entry(self.window, font=("Helvetica", 12))
        self.balls_entry.pack(pady=10)
        tk.Button(self.window, text="Start Game", command=self.start_game, bg="#440c57", fg="white").pack(pady=5)
        tk.Button(self.window, text="reset Game", command=self.reset_game, bg="#440c57", fg="white").pack(pady=5)
        tk.Button(self.window, text="Instructions", command=self.show_instructions, bg="#440c57", fg="white").pack(
            pady=5)

    def show_instructions(self):
        messagebox.showinfo("How to Play", "Remove 1-4 balls per turn. Avoid removing the last ball!")

    def reset_game(self):
        self.remaining_balls = 0
        self.canvas.delete("balls")
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score:\nUser - {self.user_score}\ncomputer - {self.computer_score}")

    def start_game(self):
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
                if not (1 <= user_input <= 4):
                    raise ValueError
                self.remaining_balls -= user_input
                turn_window.destroy()
                self.update_game()
                if self.remaining_balls > 0:
                    self.computer_turn()  # Computer's turn follows user's turn
            except ValueError:
                messagebox.showerror("Error", "Entry number between 1 and 4.")

        turn_window = tk.Toplevel(self.window)
        turn_window.title("Your Turn")
        tk.Label(turn_window, text="How many balls to remove (1-4)?").pack(pady=5)
        user_input_entry = tk.Entry(turn_window)
        user_input_entry.pack(pady=5)
        tk.Button(turn_window, text="Submit", command=handle_turn).pack(pady=5)

    def computer_turn(self):
        balls_to_remove = min(self.remaining_balls, self.remaining_balls % 5 or random.randint(1, 4))
        self.remaining_balls -= balls_to_remove
        messagebox.showinfo("computer's Turn", f"computer removed{balls_to_remove}balls.")
        if self.remaining_balls <= 0:
            self.computer_score += 1
            self.update_score()
            Balls(self.canvas, self.remaining_balls).draw()
            messagebox.showinfo("Game Over", "Computer wins!")
            return
        self.update_game()
        self.user_turn()

    def update_game(self):
        Balls(self.canvas, self.remaining_balls).draw()
        if self.remaining_balls <= 0:
            if self.remaining_balls % 5:
                self.user_score += 1
                winner = "User"
            else:
                self.computer_score += 1
                winner = "Computer"
            self.update_score()
            messagebox.showinfo("Game Over", f"{winner} wins!")
            return


class Balls:
    def __init__(self, canvas, total_balls):
        self.canvas = canvas
        self.total_balls = total_balls

    def draw(self):
        self.canvas.delete("balls")
        for i in range(self.total_balls):
            x = 20 + (i % 15) * 30
            y = 20 + (i // 15) * 30
            self.canvas.create_oval(x, y, x + 20, y + 20, fill="#440c57", tags="balls")


if __name__ == "__main__":
    game_window = GameWindow()
    game_ui = GameUI(game_window)
    game_window.start()
