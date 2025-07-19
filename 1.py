import random
import math

class Board:
    def __init__(self):
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

    def row(self):
        return (self.arr.index(0)//3)
        
    def col(self):
        index = self.arr.index(0)
        return (index - self.row()*3)

    def shift(self, direction: str)->bool:
        row = self.row()
        col = self.col()

        if direction == "left" and col != 0:
            target = row*3 + col - 1
        elif direction == "right" and col != 2:
            target = row*3 + col + 1
        elif direction == "up" and row != 0:
            target = row*3 + col - 3
        elif direction == "down" and row != 2:
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
        
Test()