def lin_search(arr, num):
    pos = -1
    for i in range(0, len(arr)):
        if num == arr[i]:
            pos = i + 1
            break
    if pos == -1:
        print("This number is not included in the array.")
    else:
        print("The position of this number : ", pos)


n = int(input("Enter the size of the array: "))
print("Now the enter the value of this array: ")
array1 = []
for i in range(0, n):
    print("array[", i, "] =",end=" ")
    value = int(input())
    array1.append(value)

print("\nThe Array is : ", array1, end="\n\n")
num = int(input("Enter the number which you want to search: "))
lin_search(array1, num)

