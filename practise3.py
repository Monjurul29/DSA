def lin_search(arr, ele):
    pos = -1
    for i in range(0, len(arr)):
        if arr[i] == ele:
            pos = i + 1
    if pos == -1:
        print("The number is not in the array")
    else:
        print("The number is at position: ", pos)


n = int(input("Enter the size of array: "))
arr = []
print("Enter the elements of array: ")
for i in range(0, n):
    print("arr[", i , "] = ", end=" ")
    ele = int(input())
    arr.append(ele)

print("Now the array: ", arr)

ele = int(input("Enter the element that you want to search: "))

lin_search(arr, ele)