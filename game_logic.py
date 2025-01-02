import chess

class GameLogic:
    def __init__(self, chessboard, canvas, status_label):
        self.chessboard = chessboard
        self.canvas = canvas
        self.status_label = status_label
        self.player_turn = "White"
        self.selected_piece = None
        self.source_square = None

    def select_piece(self, square):
        piece = self.chessboard.board.piece_at(square)
        if piece and piece.color == (self.player_turn == "White"):
            self.selected_piece = piece
            self.source_square = square
        else:
            print("Invalid selection")

    def move_piece(self, target_square):
        move = chess.Move(self.source_square, target_square)
        if move in self.chessboard.board.legal_moves:
            self.chessboard.board.push(move)
            self.chessboard.draw_pieces(self.canvas)
            self.player_turn = "Black" if self.player_turn == "White" else "White"
            self.status_label.config(text=f"{self.player_turn} to move")
        else:
            print("Illegal move")
        self.selected_piece = None
        self.source_square = None
