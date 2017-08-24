import random

pick_number = int(input("How many quick picks?"))
for i in range(pick_number):
    quick_pick = []
    for n in range(6):
        number = (random.randint(1,45))
        quick_pick.append(number)
    quick_pick.sort()
    print (" ".join(str(j) for j in quick_pick))


