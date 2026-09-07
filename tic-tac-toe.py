import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("520x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#121212")

        # Game variables
        self.board = [""] * 9
        self.current_player = "X"
        self.game_over = False

        self.x_score = 0
        self.o_score = 0
        self.draw_score = 0

        self.mode = "Player vs Computer"
        self.difficulty = "Medium"

        # Colors
        self.bg = "#121212"
        self.card = "#1E1E1E"
        self.button_bg = "#292929"
        self.x_color = "#00BFFF"
        self.o_color = "#FF4F81"
        self.text_color = "#FFFFFF"
        self.muted = "#AAAAAA"
        self.win_color = "#3DDC84"

        self.create_ui()

    # --------------------------------------------------
    # USER INTERFACE
    # --------------------------------------------------

    def create_ui(self):

        # Title
        title = tk.Label(
            self.root,
            text="TIC-TAC-TOE",
            font=("Arial", 28, "bold"),
            bg=self.bg,
            fg=self.text_color
        )
        title.pack(pady=(25, 5))

        subtitle = tk.Label(
            self.root,
            text="Classic strategy game",
            font=("Arial", 11),
            bg=self.bg,
            fg=self.muted
        )
        subtitle.pack()

        # Scoreboard
        score_frame = tk.Frame(
            self.root,
            bg=self.card
        )
        score_frame.pack(
            padx=35,
            pady=20,
            fill="x"
        )

        self.x_score_label = tk.Label(
            score_frame,
            text="X\n0",
            font=("Arial", 18, "bold"),
            bg=self.card,
            fg=self.x_color
        )
        self.x_score_label.pack(
            side="left",
            expand=True,
            pady=12
        )

        self.draw_score_label = tk.Label(
            score_frame,
            text="DRAW\n0",
            font=("Arial", 15, "bold"),
            bg=self.card,
            fg=self.text_color
        )
        self.draw_score_label.pack(
            side="left",
            expand=True
        )

        self.o_score_label = tk.Label(
            score_frame,
            text="O\n0",
            font=("Arial", 18, "bold"),
            bg=self.card,
            fg=self.o_color
        )
        self.o_score_label.pack(
            side="left",
            expand=True
        )

        # Turn display
        self.status_label = tk.Label(
            self.root,
            text="Player X's Turn",
            font=("Arial", 16, "bold"),
            bg=self.bg,
            fg=self.text_color
        )
        self.status_label.pack(pady=(5, 15))

        # Board
        board_frame = tk.Frame(
            self.root,
            bg=self.bg
        )
        board_frame.pack()

        self.buttons = []

        for i in range(9):
            button = tk.Button(
                board_frame,
                text="",
                font=("Arial", 32, "bold"),
                width=4,
                height=2,
                bg=self.button_bg,
                fg=self.text_color,
                activebackground="#383838",
                activeforeground=self.text_color,
                relief="flat",
                borderwidth=0,
                command=lambda index=i: self.make_move(index)
            )

            row = i // 3
            col = i % 3

            button.grid(
                row=row,
                column=col,
                padx=5,
                pady=5
            )

            self.buttons.append(button)

        # Controls
        controls = tk.Frame(
            self.root,
            bg=self.bg
        )
        controls.pack(pady=25)

        # Mode button
        mode_button = tk.Button(
            controls,
            text="Player vs Computer",
            font=("Arial", 11, "bold"),
            bg="#333333",
            fg="white",
            activebackground="#444444",
            relief="flat",
            padx=15,
            pady=8,
            command=self.change_mode
        )
        mode_button.pack(side="left", padx=5)

        self.mode_button = mode_button

        # Difficulty button
        difficulty_button = tk.Button(
            controls,
            text="Medium",
            font=("Arial", 11, "bold"),
            bg="#333333",
            fg="white",
            activebackground="#444444",
            relief="flat",
            padx=15,
            pady=8,
            command=self.change_difficulty
        )
        difficulty_button.pack(side="left", padx=5)

        self.difficulty_button = difficulty_button

        # New game button
        new_game_button = tk.Button(
            self.root,
            text="NEW GAME",
            font=("Arial", 13, "bold"),
            bg="#00BFFF",
            fg="#000000",
            activebackground="#0099CC",
            relief="flat",
            padx=35,
            pady=10,
            command=self.new_game
        )
        new_game_button.pack()

        # Reset score
        reset_button = tk.Button(
            self.root,
            text="Reset Score",
            font=("Arial", 10),
            bg=self.bg,
            fg=self.muted,
            activebackground=self.bg,
            activeforeground="white",
            relief="flat",
            command=self.reset_score
        )
        reset_button.pack(pady=12)

    # --------------------------------------------------
    # GAME LOGIC
    # --------------------------------------------------

    def make_move(self, index):

        # Don't allow moves after game ends
        if self.game_over:
            return

        # Don't allow occupied cells
        if self.board[index] != "":
            return

        # Computer's turn
        if self.mode == "Player vs Computer" and self.current_player == "O":
            return

        self.board[index] = self.current_player

        self.update_board()

        result = self.check_game()

        if result:
            return

        self.switch_player()

        # Computer move
        if (
            self.mode == "Player vs Computer"
            and self.current_player == "O"
            and not self.game_over
        ):
            self.status_label.config(
                text="Computer is thinking..."
            )

            self.root.after(
                400,
                self.computer_move
            )

    # --------------------------------------------------
    # COMPUTER AI
    # --------------------------------------------------

    def computer_move(self):

        if self.game_over:
            return

        if self.difficulty == "Easy":
            move = self.random_move()

        elif self.difficulty == "Medium":
            move = self.medium_move()

        else:
            move = self.best_move()

        if move is not None:
            self.board[move] = "O"

        self.update_board()

        result = self.check_game()

        if result:
            return

        self.switch_player()

    # Easy AI
    def random_move(self):
        empty_cells = [
            i for i in range(9)
            if self.board[i] == ""
        ]

        if empty_cells:
            return random.choice(empty_cells)

        return None

    # Medium AI
    def medium_move(self):

        # First try to win
        for i in range(9):

            if self.board[i] == "":
                self.board[i] = "O"

                if self.get_winner() == "O":
                    self.board[i] = ""
                    return i

                self.board[i] = ""

        # Then block player
        for i in range(9):

            if self.board[i] == "":
                self.board[i] = "X"

                if self.get_winner() == "X":
                    self.board[i] = ""
                    return i

                self.board[i] = ""

        # Prefer center
        if self.board[4] == "":
            return 4

        # Then corners
        corners = [0, 2, 6, 8]
        available_corners = [
            i for i in corners
            if self.board[i] == ""
        ]

        if available_corners:
            return random.choice(available_corners)

        return self.random_move()

    # Hard AI using Minimax
    def best_move(self):

        best_score = -float("inf")
        move = None

        for i in range(9):

            if self.board[i] == "":
                self.board[i] = "O"

                score = self.minimax(
                    self.board,
                    False
                )

                self.board[i] = ""

                if score > best_score:
                    best_score = score
                    move = i

        return move

    def minimax(self, board, maximizing):

        winner = self.get_winner()

        if winner == "O":
            return 1

        if winner == "X":
            return -1

        if "" not in board:
            return 0

        if maximizing:

            best_score = -float("inf")

            for i in range(9):

                if board[i] == "":
                    board[i] = "O"

                    score = self.minimax(
                        board,
                        False
                    )

                    board[i] = ""

                    best_score = max(
                        best_score,
                        score
                    )

            return best_score

        else:

            best_score = float("inf")

            for i in range(9):

                if board[i] == "":
                    board[i] = "X"

                    score = self.minimax(
                        board,
                        True
                    )

                    board[i] = ""

                    best_score = min(
                        best_score,
                        score
                    )

            return best_score

    # --------------------------------------------------
    # BOARD
    # --------------------------------------------------

    def update_board(self):

        for i in range(9):

            symbol = self.board[i]

            if symbol == "X":

                self.buttons[i].config(
                    text="X",
                    fg=self.x_color
                )

            elif symbol == "O":

                self.buttons[i].config(
                    text="O",
                    fg=self.o_color
                )

            else:

                self.buttons[i].config(
                    text="",
                    fg=self.text_color
                )

    # --------------------------------------------------
    # WIN / DRAW
    # --------------------------------------------------

    def get_winner(self):

        winning_combinations = [

            # Rows
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),

            # Columns
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),

            # Diagonals
            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in winning_combinations:

            if (
                self.board[a] != ""
                and self.board[a] == self.board[b]
                and self.board[a] == self.board[c]
            ):
                return self.board[a]

        return None

    def get_winning_combination(self):

        winning_combinations = [

            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),

            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),

            (0, 4, 8),
            (2, 4, 6)
        ]

        for combination in winning_combinations:

            a, b, c = combination

            if (
                self.board[a] != ""
                and self.board[a] == self.board[b]
                and self.board[a] == self.board[c]
            ):
                return combination

        return None

    def check_game(self):

        winner = self.get_winner()

        if winner:

            self.game_over = True

            winning_cells = self.get_winning_combination()

            for cell in winning_cells:
                self.buttons[cell].config(
                    bg=self.win_color,
                    fg="#000000"
                )

            if winner == "X":
                self.x_score += 1

            else:
                self.o_score += 1

            self.update_score()

            self.status_label.config(
                text=f"🎉 Player {winner} Wins!"
            )

            self.root.after(
                500,
                lambda: messagebox.showinfo(
                    "Game Over",
                    f"Player {winner} wins!"
                )
            )

            return True

        # Draw
        if "" not in self.board:

            self.game_over = True

            self.draw_score += 1

            self.update_score()

            self.status_label.config(
                text="🤝 It's a Draw!"
            )

            self.root.after(
                500,
                lambda: messagebox.showinfo(
                    "Game Over",
                    "It's a draw!"
                )
            )

            return True

        return False

    # --------------------------------------------------
    # TURN SYSTEM
    # --------------------------------------------------

    def switch_player(self):

        if self.current_player == "X":
            self.current_player = "O"

        else:
            self.current_player = "X"

        if self.mode == "Player vs Computer":

            if self.current_player == "X":
                self.status_label.config(
                    text="Your Turn — X"
                )

            else:
                self.status_label.config(
                    text="Computer — O"
                )

        else:

            self.status_label.config(
                text=f"Player {self.current_player}'s Turn"
            )

    # --------------------------------------------------
    # NEW GAME
    # --------------------------------------------------

    def new_game(self):

        self.board = [""] * 9
        self.current_player = "X"
        self.game_over = False

        for button in self.buttons:

            button.config(
                text="",
                bg=self.button_bg,
                fg=self.text_color
            )

        if self.mode == "Player vs Computer":

            self.status_label.config(
                text="Your Turn — X"
            )

        else:

            self.status_label.config(
                text="Player X's Turn"
            )

    # --------------------------------------------------
    # SCORE
    # --------------------------------------------------

    def update_score(self):

        self.x_score_label.config(
            text=f"X\n{self.x_score}"
        )

        self.o_score_label.config(
            text=f"O\n{self.o_score}"
        )

        self.draw_score_label.config(
            text=f"DRAW\n{self.draw_score}"
        )

    def reset_score(self):

        self.x_score = 0
        self.o_score = 0
        self.draw_score = 0

        self.update_score()

        self.new_game()

    # --------------------------------------------------
    # MODE
    # --------------------------------------------------

    def change_mode(self):

        if self.mode == "Player vs Computer":

            self.mode = "Player vs Player"

            self.mode_button.config(
                text="Player vs Player"
            )

        else:

            self.mode = "Player vs Computer"

            self.mode_button.config(
                text="Player vs Computer"
            )

        self.new_game()

    # --------------------------------------------------
    # DIFFICULTY
    # --------------------------------------------------

    def change_difficulty(self):

        if self.difficulty == "Easy":

            self.difficulty = "Medium"

        elif self.difficulty == "Medium":

            self.difficulty = "Hard"

        else:

            self.difficulty = "Easy"

        self.difficulty_button.config(
            text=self.difficulty
        )


# ------------------------------------------------------
# START GAME
# ------------------------------------------------------

root = tk.Tk()

game = TicTacToe(root)

root.mainloop()