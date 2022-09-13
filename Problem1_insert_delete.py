def insertion(arr):
    pos = int(input("Enter the position from which you want to add: "))
    num = int(input("Enter the number to add: "))
    arr.insert(pos, num)
    print("Now the array is: ", arr)
    print("\n")
    return arr


def deletation(arr):
    pos = int(input("Enter the index which you want to delete: "))
    del arr[pos]
    print("Now the array is : ", arr)
    print("\n")
    return arr


n = int(input("Enter the size of the array: "))
print("Now the enter the value of this array: ")
array1 = []
print()
for i in range(0, n):
    print("array[", i, "] = ", end=" ")
    value = int(input())
    array1.append(value)

print("\nThe Array is : ", array1)


while 1:
    print("\nIf you want to insert, press 1")
    print("If you want to delete, press 2")
    print("If you want to quite, press 3")

    press = int(input("\nPress: "))

    if press == 1:
        print()
        insertion(array1)
    if press == 2:
        print()
        deletation(array1)
    if press == 3:
        print()
        print("Ok program is closed. Bye")
        break