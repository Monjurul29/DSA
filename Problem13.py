def enqueue(arr, n):
    l = len(arr)
    if l == n:
        print("The array is full. No number will be added")
    else:
        i = int(input("Enter which number you want to add: "))
        arr.append(i)
        print("After enqueue, the array is : ", arr)

def dequeue(arr, n):
    l = len(arr)
    if l == 0:
        print("The array is empty. so no item will be deleted")
    else:
        del arr[0]
        print("After dequeue, the array is : ", arr)


n = int(input("Enter the size of an array: "))
print("Enter the array: ", end=" ")
arr = list(int(i) for i in input().split())[:n]
print("Now the array is : ", arr)
while 1:
    print("If you want to enqueue an element, press 1")
    print("If you want to dequeue an element, press 2")
    print("If you want to quite, press 3")
    press = int(input("Enter the press: "))
    if press == 1:
        enqueue(arr, n)
    elif press == 2:
        dequeue(arr, n)
    else:
        print("Thank you! see you again")
        break