def bubble_sort(arr):
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print("\nAfter bubble_sorting the new array is : ", arr)


n = int(input("Enter the size of array: "))
arr = []
print("Enter the elements of array: ")
for i in range(0, n):
    print("arr[", i , "] = ", end=" ")
    ele = int(input())
    arr.append(ele)

print("Now the array: ", arr)

bubble_sort(arr)
