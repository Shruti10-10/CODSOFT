import tkinter as tk
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x400")
        self.root.config(bg="#f0f0f0")

        self.user_score = 0
        self.comp_score = 0

        self.title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#f0f0f0")
        self.title.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Arial", 16), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text="You: 0  Computer: 0", font=("Arial", 14), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=20)

        self.rock_button = tk.Button(self.button_frame, text="Rock", font=("Arial", 14), width=10, command=lambda: self.play("Rock"))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", font=("Arial", 14), width=10, command=lambda: self.play("Paper"))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", font=("Arial", 14), width=10, command=lambda: self.play("Scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 12), bg="red", fg="white", command=self.reset_scores)
        self.reset_button.pack(pady=10)

    def play(self, user_choice):
        comp_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = ""

        if user_choice == comp_choice:
            result = f"Both chose {user_choice}. It's a tie!"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            result = f"You win! {user_choice} beats {comp_choice}"
            self.user_score += 1
        else:
            result = f"You lose! {comp_choice} beats {user_choice}"
            self.comp_score += 1

        self.result_label.config(text=result)
        self.score_label.config(text=f"You: {self.user_score}  Computer: {self.comp_score}")

    def reset_scores(self):
        self.user_score = 0
        self.comp_score = 0
        self.result_label.config(text="")
        self.score_label.config(text="You: 0  Computer: 0")

if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()
