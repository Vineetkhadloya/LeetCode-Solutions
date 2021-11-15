def arrayEvenAndOdd(arr):
    
    i = -1

    for j in range(len(arr)):
        if arr[j] % 2 == 0:
            i += 1
            print(i,j)
            arr[i],arr[j] = arr[j],arr[i]
            print(arr)
    print(arr)

arr = [ 1, 3, 2, 4, 7, 6, 9, 10 ]
# n = len(arr)
print(arr)
# Function call
arrayEvenAndOdd(arr)
 