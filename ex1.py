print("hello world")
#print("hello again")
print("i like typing this.")
print("this is fun.")
print('Yay! printing.')
print("i'd much rather you 'not'.")
print('i"said"do not touch this.')

def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr