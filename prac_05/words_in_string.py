string = str(input("Text: "))
string_list = string.split(" ")
string_list.sort()
my_dict = {}
i = 0
for word in string_list:
    count = str(string_list.count(word))
    my_dict[string_list[i]] = count
    i = i + 1
for k, v in my_dict.items():
    print("{:<4s} : {:<1s}".format(k,v))

