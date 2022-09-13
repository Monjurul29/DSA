def insertion(arr):
    num = int(input("Enter the number which you want to insert: "))
    pos = int(input("Enter the position in which you want to insert: "))
    arr.insert(pos, num)
    print("\nAfter inserting, the array is: ")
    print(arr)


def deletation(arr):
    pos = int(input("Enter the position which you want to delete from the array: "))
    del arr[pos]
    print("\nAfter deleting, the array is: ")
    print(arr)



n = int(input("Enter the size of array: "))
arr = []
print("Enter the elements of array: ")
for i in range(0, n):
    print("arr[", i , "] = ", end=" ")
    ele = int(input())
    arr.append(ele)

print("Now the array: ", arr)

while 1:
    print("\nIf you want to insert, press 1")
    print("If you want to delete, press 2")
    print("If you want to quite, press 3")

    press = int(input("press: "))
    if press == 1:
        insertion(arr)
    elif press == 2:
        deletation(arr)
    elif press == 3:
        print("\nOk, Thank you!")
        break