number_of_items = int(input("Number of items"))
if number_of_items > 0:
    i = 0
    total = 0
    while i != number_of_items:
        item = float(input("Price of item:"))
        total = total + item
        i = i + 1
    if total > 100:
        total = total * 1.1
    print("Total price for ", number_of_items, " items is $", total)
else:
    print("invalid option")
