def List_Sorter_main():
    print("Enter your list!")
    a = 0
    print("Input the length of the list.")
    while a < input():
        lst.append(input("list[", a, "]:"))
    dictionary = {}
    for a in lst:
        for b in lst:
            if a > b:
                c += 1
        dictionary[a] = c
    print(dictionary)
    a = 0
    newlst = []
    while a < len(lst):
        newlst.append(0)
        a += 1
    for a in dictionary:
        newlst[dictionary.get(a)] = a
    print(newlst)
    return newlst
