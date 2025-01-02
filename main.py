import tkinter as tk
from gui import ChessGame

def main():
    root = tk.Tk()
    app = ChessGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
