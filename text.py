arr = [1,2,3,
       4,5,6,
       7,8,0] 

def row(arr):
    return (arr.index(0)//3)
    
def col(arr):
    index = arr.index(0)
    return (index -row(arr)*3)

class ass:
    def __init__(self, arr):
        self.arr = arr

  
    def neighbor(self,arr):
        i = row(self.arr)
        j = col(self.arr)
        neighbor = []
        neighborBoard = []
        side = int(len(self.arr)**.5)

        for r, c in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
            if r>=0 and c>=0 and r<len(self.arr)**.5 and c<len(self.arr)**.5:
                neighbor.append([r,c])
        for r, c in neighbor:
            tempBoard = self.arr.copy()
            tempBoard[i*(side)+j] , tempBoard[r*(side)+c] = tempBoard[r*(side)+c] , tempBoard[i*(side)+j]
            neighborBoard.append(tempBoard) 
            
        return neighborBoard

# print(row(arr))
# print(col(arr))

print(ass(arr).neighbor(ass))

# neighbor(arr)
# x = neighbor(arr)


# print(x)


