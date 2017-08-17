name = str(input("Enter name: "))
print("(H)ello\n(G)oodbye\n(Q)uit")
choice =  str(input(">>>"))
while choice != "Q":
    if choice == "H":
        print ("hello ", name)
    elif choice == "G":
        print("goodbye ", name)
    else:
        print("invalid option")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = str(input(">>>"))
print("finished")

