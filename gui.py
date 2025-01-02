import tkinter as tk
from tkinter import messagebox, simpledialog
import chess
from chessboard import ChessBoard
from game_logic import GameLogic
from leaderboard import Leaderboard

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.fullscreen = False

        self.chessboard = ChessBoard()
        self.leaderboard = Leaderboard()
        self.canvas = None
        self.logic = None

        self.show_welcome_screen()

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)

    def show_welcome_screen(self):
        self.welcome_frame = tk.Frame(self.root)
        self.welcome_frame.pack()

        tk.Label(self.welcome_frame, text="Welcome to the Chess Game!").pack(pady=10)
        tk.Button(self.welcome_frame, text="New Game", command=self.show_game_options).pack(pady=5)
        tk.Button(self.welcome_frame, text="View Leaderboard", command=self.display_leaderboard).pack(pady=5)
        tk.Button(self.welcome_frame, text="Toggle Fullscreen", command=self.toggle_fullscreen).pack(pady=5)
    
    def show_game_options(self):
        self.welcome_frame.pack_forget()
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack()

        tk.Label(self.options_frame, text="Choose Game Mode").pack(pady=10)
        tk.Button(self.options_frame, text="1 Player", command=lambda: self.get_player_names(1)).pack(pady=5)
        tk.Button(self.options_frame, text="2 Players", command=lambda: self.get_player_names(2)).pack(pady=5)
    
    def get_player_names(self, num_players):
        self.options_frame.pack_forget()
        self.name_frame = tk.Frame(self.root)
        self.name_frame.pack()

        self.player_names = []
        if num_players == 1:
            self.player_names.append(simpledialog.askstring("Player Name", "Enter your name"))
        else:
            self.player_names.append(simpledialog.askstring("Player 1 Name", "Enter name for Player 1"))
            self.player_names.append(simpledialog.askstring("Player 2 Name", "Enter name for Player 2"))

        self.start_game()

    def start_game(self):
        self.name_frame.pack_forget()

        self.canvas = tk.Canvas(self.root, width=480, height=480)
        self.canvas.pack()
        self.draw_board()
        self.chessboard.draw_pieces(self.canvas)

        self.status_label = tk.Label(self.root, text="White to move")
        self.status_label.pack()
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        self.logic = GameLogic(self.chessboard, self.canvas, self.status_label)
        
        self.create_menu()

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        game_menu = tk.Menu(menu)
        menu.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="New Game", command=self.new_game)
        game_menu.add_command(label="Quit", command=self.root.quit)

        options_menu = tk.Menu(menu)
        menu.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Player vs Player", command=self.set_player_vs_player)
        options_menu.add_command(label="Player vs Computer", command=self.set_player_vs_computer)
        options_menu.add_command(label="Set Player Names", command=self.show_game_options)
        options_menu.add_command(label="Toggle Fullscreen", command=self.toggle_fullscreen)

    def draw_board(self):
        colors = ["#DDB88C", "#A66D4F"]
        for row in range(8):
            for col in range(8):
                x1 = col * 60
                y1 = row * 60
                x2 = x1 + 60
                y2 = y1 + 60
                color = colors[(row + col) % 2]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def on_canvas_click(self, event):
        col = event.x // 60
        row = 7 - (event.y // 60)
        square = chess.square(col, row)
        if self.logic.selected_piece:
            self.logic.move_piece(square)
        else:
            self.logic.select_piece(square)

    def new_game(self):
        self.canvas.pack_forget()
        self.status_label.pack_forget()
        self.show_game_options()

    def set_player_vs_player(self):
        self.logic.player_vs_computer = False

    def set_player_vs_computer(self):
        self.logic.player_vs_computer = True

    def display_leaderboard(self):
        leaderboard_text = self.leaderboard.display()
        messagebox.showinfo("Leaderboard", leaderboard_text)
