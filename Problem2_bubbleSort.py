n = int(input("Enter the size of the array: "))
print("Now the enter the value of this array: ")
array1 = []
for i in range(0, n):
    print("array[", i, "] =",end=" ")
    value = int(input())
    array1.append(value)

print("\nThe Array is : ", array1)

for i in range(0, n):
    for j in range(0, n - i - 1):
        if array1[j] > array1[j+1]:
            temp = array1[j]
            array1[j] = array1[j+1]
            array1[j+1] = temp

print("After sorting the array is : ", array1)

