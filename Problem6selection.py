def selection(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j

        if min != i:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp


n = int(input("Enter the size of an array: "))
print("Enter the array: ")
arr = [int(input()) for i in range(n)]
selection(arr)
print("After selection sorting: ", arr)
