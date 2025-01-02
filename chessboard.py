import chess
from tkinter import PhotoImage
from PIL import Image, ImageTk

class ChessBoard:
    def __init__(self):
        self.board = chess.Board()
        self.piece_images = {}
        self.piece_map = {
            'P': 'wp',
            'p': 'bp',
            'N': 'wn',
            'n': 'bn',
            'B': 'wb',
            'b': 'bb',
            'R': 'wr',
            'r': 'br',
            'Q': 'wq',
            'q': 'bq',
            'K': 'wk',
            'k': 'bk'
        }

    def load_images(self):
        for piece, filename in self.piece_map.items():
            try:
                image = Image.open(f"images/{filename}.png")
                image = image.resize((60, 60), Image.LANCZOS)
                self.piece_images[piece] = ImageTk.PhotoImage(image)
                print(f"Loaded image for {piece}: images/{filename}.png")
            except Exception as e:
                print(f"Error loading image for {piece}: {e}")

    def draw_pieces(self, canvas):
        canvas.delete("piece")
        for row in range(8):
            for col in range(8):
                piece = self.board.piece_at(chess.square(col, 7 - row))
                if piece:
                    piece_str = str(piece)
                    piece_image = self.piece_images.get(piece_str)
                    if piece_image:
                        x = col * 60 + 30
                        y = (7 - row) * 60 + 30
                        canvas.create_image(x, y, image=piece_image, tags="piece")
                        print(f"Drew {piece_str} at {chess.square_name(chess.square(col, 7 - row))}")
                    else:
                        print(f"Image not found for piece: {piece_str}")
