import random
import math

def generate():
    arr = [i for i in range(9)]
    shuffled = arr[:]
    random.shuffle(shuffled)
    return shuffled
arr = generate()
print(arr)  # Output: A shuffled list of numbers from 0 to 8

def parity_checker(arr):
    arr[:] = [1,2,3,4,5,6,7,8,0]
    count = 0
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] and j<i and arr[j]> arr[i]: count+=1
    return count
        
def print_board(arr):
    for i in range(3):
        for j in range(3):
            print(arr[j+i*3], end=" ")
        print()

# def shift_left():
#     row = round(arr.index(0)/3)
#     col

    

print(parity_checker(arr))
print(arr)
print_board(arr)


print("hhhhhhhhhhhhhhh")
# for i in range(len(arr)):
#     row = math.floor(arr.index(i)/3)
#     print(row)
    
print(arr[0]/3)
print("hhhhhhhhhhhhhhh")

# col finding replace i by index hew hwhw wh wwh
for i in range(len(arr)):
    row = math.floor(i/3)
    col = i-(row*3)
    print(col)

