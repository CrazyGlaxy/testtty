import random

class Board:
    def __init__(self):
        self.generate()
        while self.parity_checker() % 2 != 0:
            self.generate()

    def generate(self):
        self.arr = [i for i in range(9)]
        random.shuffle(self.arr)
        self.arr[:] = [2, 7, 1, 0, 6, 4, 3, 5, 8] #174037
    def parity_checker(self):
        count = 0
        for i in range(len(self.arr)):
            for j in range(i):
                if self.arr[i] and self.arr[j] > self.arr[i]:
                    count += 1
        return count

    def print_board(self):
        for i in range(3):
            print(self.arr[i*3:(i+1)*3])

    @staticmethod
    def row(arr): return arr.index(0) // 3
    @staticmethod
    def col(arr): return arr.index(0) % 3

class Search:
    def __init__(self, board: Board):
        self.board = tuple(board.arr)
        self.frontier = [self.board]
        self.frontier_set = {self.board}
        self.completed = set()
        self.child_parent = [[self.board, -1]]
        self.state_index = {self.board: 0}
        print("self.board:", self.board)
    def frontierGen(self):
        while self.frontier:
            current = self.frontier.pop(0)
            self.frontier_set.remove(current)

            if current == tuple(range(1, 9)) + (0,):
                break

            self.completed.add(current)

            for neighbor in self.neighbor(current):
                if neighbor not in self.completed and neighbor not in self.frontier_set:
                    self.frontier.append(neighbor)
                    self.frontier_set.add(neighbor)
            # print("frontier size:", len(self.frontier))
        print("✅ Total discovered states:", len(self.completed))

    def neighbor(self, arr):
        i, j = Board.row(arr), Board.col(arr)
        side = 3
        moves = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        valid = [(r, c) for r, c in moves if 0 <= r < side and 0 <= c < side]

        neighbors = []
        parent_index = self.state_index[arr]

        for r, c in valid:
            temp = list(arr)
            from_idx, to_idx = i * side + j, r * side + c
            temp[from_idx], temp[to_idx] = temp[to_idx], temp[from_idx]
            state = tuple(temp)

            if state not in self.state_index:
                self.child_parent.append([state, parent_index])
                self.state_index[state] = len(self.child_parent) - 1
                neighbors.append(state)

        return neighbors

    def trackParent(self):
        current = tuple(range(1, 9)) + (0,)
        tracked = []

        while current != self.board:
            tracked.append(current)
            current = self.child_parent[self.state_index[current]][1]
            current = self.child_parent[current][0]

        tracked.append(self.board)
        return list(reversed(tracked))


board = Board()
search = Search(board)
search.frontierGen()
solution_path = search.trackParent()  # <- no print, returns list of states

print(solution_path)