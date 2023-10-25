import tkinter as tk
import pygame
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.player = "X"
        self.score_x = 0
        self.score_o = 0
        self.round = 1  # Initialize the round as 1

        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text=" ", font=("normal", 30), width=5, height=2, command=lambda i=i, j=j: self.play(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        self.score_label = tk.Label(self.window, text="Score: X - 0 | O - 0")
        self.score_label.grid(row=3, column=0, columnspan=3)

        self.restart_button = tk.Button(self.window, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=4, column=0, columnspan=3)

        # Background music setup
        pygame.init()
        pygame.mixer.music.load("background_music.mp3")
        pygame.mixer.music.play(-1)  # -1 means continuous play

        # Dark blue background setup
        self.window.configure(bg="#00008B")

    def play(self, i, j):
        if self.buttons[i][j]["text"] == " ":
            self.buttons[i][j]["text"] = self.player
            if self.check_victory():
                self.show_victory()
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_victory(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != " ":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != " ":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != " ":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != " ":
            return True
        return False

    def show_victory(self):
        winner = self.player
        message = f"Player {winner} wins round {self.round}!"
        tk.messagebox.showinfo("Game Over", message)
        
        if winner == "X":
            self.score_x += 1
        else:
            self.score_o += 1

        self.update_score()
        
        self.round += 1
        if self.round > 12:
            self.end_game()
        else:
            self.restart_game()

    def restart_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = " "
        self.player = "X"
    
    def update_score(self):
        self.score_label.config(text=f"Score: X - {self.score_x} | O - {self.score_o}")

    def end_game(self):
        winner = "X" if self.score_x > self.score_o else "O"
        message = f"Game Over! Player {winner} wins the match."
        tk.messagebox.showinfo("Game Over", message)
        self.window.quit()

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeGame()
    game.start()
