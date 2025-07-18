import random
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

print(parity_checker(arr))
print(arr)
print_board(arr)


