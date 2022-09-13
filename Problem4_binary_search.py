n = int(input("Enter the size of the array: "))
print("Now the enter the value of this array: ")
array1 = []
for i in range(0, n):
    print("array[", i, "] =",end=" ")
    value = int(input())
    array1.append(value)

print("\nThe Array is : ", array1)
array1.sort()
print("\nNow the sorted array is : ", array1)


num = int(input("Now Enter the number which you want to search: "))


# array1 will be separated by two parts
highIndex = n - 1
lowIndex = 0
mid = -1
while (highIndex >= lowIndex):
    mid = (highIndex + lowIndex) // 2
    if num == array1[mid]:
        break
    if num < array1[mid]:
        highIndex = mid - 1
    else:
        lowIndex = mid + 1



if lowIndex > highIndex:
    print(num, "is not found in this array.")
else:
    print(num, "is found at position: ", mid+1)
