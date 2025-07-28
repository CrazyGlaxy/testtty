import random
import math
import pyxel

class Board:
    def __init__(self):
        self.generate()
        while self.parity_checker() %2 != 0:
            self.generate()
            

    def generate(self)->None:
        self.arr = [i for i in range(9)]
        shuffled = self.arr[:]
        random.shuffle(shuffled)
        self.arr = shuffled
        self.arr[:] = [1,2,3,4,5,6,7,8,0]

    def parity_checker(self):
        count = 0
        for i in range(len(self.arr)):
            for j in range(i):
                if self.arr[i] and self.arr[j]> self.arr[i]: count+=1
        return count
            
    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.arr[j+i*3], end=" ")
            print()

    @staticmethod
    def row(arr):
        return (arr.index(0)//3)
        
    @staticmethod
    def col(arr):
        return arr.index(0)%3

    def shift(self, direction: str)->bool:
        row = Board.row(self.arr)
        col = Board.col(self.arr)

        if direction == "right" and col != 0:
            target = row*3 + col - 1
        elif direction == "left" and col != 2:
            target = row*3 + col + 1
        elif direction == "down" and row != 0:
            target = row*3 + col - 3
        elif direction == "up" and row != 2:
            target = row*3 + col + 3
        else:
            return False
        
        self.arr[row*3 + col] = self.arr[target]
        self.arr[target] = 0
        
        return True
    
    def shift_left(self)->bool:
        return self.shift("left")
        
    def shift_right(self)->bool:
        return self.shift("right")
        
    def shift_up(self):
        return self.shift("up")
    
    def shift_down(self):
        return self.shift("down")
    




# board = Board()
# board.print_board()
# print()
# print(board.arr)
# print("Checking Parity:", board.parity_checker(), "\n")
# print("row: ",board.row())
# print("col: ", board.col())

class Search:
    def __init__(self, board: Board):
        self.board = board
        self.frontier = [board.arr]
        self.completed = []

    def frontierGen(self, board):
        self.frontier.extend(state for state in self.neighbor() if state not in self.completed)
        print(self.frontier)

    def neighbor(self, arr):
        i = Board.row(arr)
        j = Board.col(arr)
        neighbor = []
        neighborBoard = []
        side = int(len(arr)**.5)

        for r, c in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
            if r>=0 and c>=0 and r<len(arr)**.5 and c<len(arr)**.5:
                neighbor.append([r,c])
        for r, c in neighbor:
            tempBoard = arr.copy()
            tempBoard[i*(side)+j] , tempBoard[r*(side)+c] = tempBoard[r*(side)+c] , tempBoard[i*(side)+j]
            neighborBoard.append(tempBoard) 
            
        return neighborBoard
    
    def printNei(self, arr):
        for index, item in enumerate(self.neighbor(arr)):
            print()
            print(index + 1,":")
            for i in range(3):
                for j in range(3):
                    print(item[j+i*3], end=" ")
                print()
    
class Test:
    def __init__(self):
        board = Board()
        board.print_board()
        print()
        print(board.arr)
        print("Checking Parity:", board.parity_checker(), "\n")
        print("row: ",board.row())
        print("col: ", board.col())
        print("shift left:", board.shift_left())
        board.print_board()
        print("shift left:", board.shift_left())
        board.print_board()
        print("shift left:", board.shift_left())
        board.print_board()
        print()
        
        # shift right
        print("shift right:", board.shift_right())
        board.print_board()
        print("shift right:", board.shift_right())
        board.print_board()
        print("shift right:", board.shift_right())
        board.print_board()

        # shift up
        print("shift up:", board.shift_up())
        board.print_board()
        print("shift up:", board.shift_up())
        board.print_board()
        print("shift up:", board.shift_up())
        board.print_board()

        # shift down
        
        print("shift down:", board.shift_down())
        board.print_board()
        print("shift down:", board.shift_down())
        board.print_board()
        print("shift down:", board.shift_down())
        board.print_board()
        
# Test()

class TileGrid:
    board = Board()
    arr = board.arr
    def __init__(self):
        pyxel.init(96, 96)
        self.tile_size = 32

        # 3x3 grid stored as a flat list (row-major)
        # 0 = blank tile
        self.tiles = self.arr

        pyxel.run(self.update, self.draw)

    def update(self):
        # Keyboard input for arrow keys
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.board.shift_left()
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.board.shift_right()
        elif pyxel.btnp(pyxel.KEY_UP):
            self.board.shift_up()
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.board.shift_down()

        # Mouse click input to move tiles
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mouse_x = pyxel.mouse_x
            mouse_y = pyxel.mouse_y

            col = mouse_x // self.tile_size
            row = mouse_y // self.tile_size
            clicked_index = row * 3 + col
            blank_index = self.board.arr.index(0)

            # Check if clicked tile is adjacent to blank tile
            if clicked_index in self._get_adjacent(blank_index):
                # Use your Board class to swap tiles by updating arr
                self.board.arr[blank_index], self.board.arr[clicked_index] = (
                    self.board.arr[clicked_index],
                    self.board.arr[blank_index],
                )

    def _get_adjacent(self, index):
        adj = []
        row = index // 3
        col = index % 3

        if col > 0:
            adj.append(index - 1)  # left neighbor
        if col < 2:
            adj.append(index + 1)  # right neighbor
        if row > 0:
            adj.append(index - 3)  # top neighbor
        if row < 2:
            adj.append(index + 3)  # bottom neighbor

        return adj



    def draw(self):
        pyxel.cls(0)

        for i in range(9):
            value = self.tiles[i]
            row = i // 3
            col = i % 3
            x = col * self.tile_size
            y = row * self.tile_size

            if value != 0:
                # Draw filled tile
                pyxel.rect(x, y, self.tile_size, self.tile_size, 5)  # filled tile (color 5)
                pyxel.text(x + 12, y + 12, str(value), 7)  # draw tile number
            else:
                # Draw empty tile border
                pyxel.rectb(x, y, self.tile_size, self.tile_size, 1)

# TileGrid()
board = Board()
# print(board.parity_checker())
# search = Search(board)
# search.frontierGen()

print(Search(board).neighbor(board.arr))

Search(board).printNei(board.arr)
