import tkinter as tk
import random

class SlidingPuzzle:
    def __init__(self, master):
        self.master = master
        self.master.title("3x3 Sliding Puzzle")
        self.size = 3
        self.tiles = list(range(1, self.size*self.size)) + [None]
        self.buttons = []
        self.create_widgets()
        self.shuffle()

    def create_widgets(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                btn = tk.Button(self.master, font=('Arial', 24), width=4, height=2,
                                command=lambda x=i, y=j: self.move_tile(x, y))
                btn.grid(row=i, column=j, padx=2, pady=2)
                row.append(btn)
            self.buttons.append(row)
        self.update_buttons()

    def shuffle(self):
        while True:
            random.shuffle(self.tiles)
            if self.is_solvable() and not self.is_solved():
                break
        self.update_buttons()

    def is_solvable(self):
        inv = 0
        arr = [t for t in self.tiles if t is not None]
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    inv += 1
        return inv % 2 == 0

    def is_solved(self):
        return self.tiles == list(range(1, self.size*self.size)) + [None]

    def move_tile(self, x, y):
        idx = x * self.size + y
        empty_idx = self.tiles.index(None)
        ex, ey = divmod(empty_idx, self.size)
        if (abs(ex - x) == 1 and ey == y) or (abs(ey - y) == 1 and ex == x):
            self.tiles[empty_idx], self.tiles[idx] = self.tiles[idx], self.tiles[empty_idx]
            self.update_buttons()
            if self.is_solved():
                tk.messagebox.showinfo("Congratulations!", "You solved the puzzle!")

    def update_buttons(self):
        for i in range(self.size):
            for j in range(self.size):
                val = self.tiles[i * self.size + j]
                btn = self.buttons[i][j]
                if val is None:
                    btn.config(text="", state="disabled", bg="lightgray")
                else:
                    btn.config(text=str(val), state="normal", bg="SystemButtonFace")

if __name__ == "__main__":
    root = tk.Tk()
    import tkinter.messagebox
    game = SlidingPuzzle(root)
    root.mainloop()