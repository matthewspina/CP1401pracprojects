x = int(input("First number:"))
y = int(input("Second number:"))
print ("(1) Show the even numbers between ", x, " and ",y,"\n(2) Show the odd numbers between ", x, " and ",y ,"\n(3) Show the squares from ", x, " and ",y, "\n(4) Exit the program")
choice = int(input(">>>"))
if choice == 1:
    if x%2 == 0:
        for i in range(x, y, 2):
            print(i, end=" ")
    else:
        for i in range(x + 1, y, 2):
            print(i, end=" ")

x = int(input("First number:"))
y = int(input("Second number:"))
print ("(1) Show the even numbers between ", x, " and ",y,"\n(2) Show the odd numbers between ", x, " and ",y ,"\n(3) Show the squares from ", x, " and ",y, "\n(4) Exit the program")
choice = int(input(">>>"))


