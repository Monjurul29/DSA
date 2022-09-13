def binary_search(arr, num):
    mid = -1
    higher_index = len(arr) - 1
    lower_index = 0
    while lower_index <= higher_index:
        mid = (lower_index + higher_index) // 2
        if num == arr[mid]:
            break
        elif num < arr[mid]:
            higher_index = mid - 1
        elif num > arr[mid]:
            lower_index = mid + 1
    if mid == -1:
        print("\n The number is not found in this array")
    else:
        print("\n The number is at position : ", mid + 1)




n = int(input("Enter the size of array: "))
arr = []
print("Enter the elements of array: ")
for i in range(0, n):
    print("arr[", i , "] = ", end=" ")
    ele = int(input())
    arr.append(ele)

print("Now the array: ", arr)
arr.sort()
print("Now the sorted array: ", arr)

num = int(input("Enter the number which you want to search: "))

binary_search(arr, num)