def List_Sorter_main():
    print("Enter your list using the steps bellow!")
    a = 0
    import time
    time.sleep(1)
    print("Input the length of the list.")
    length = int(input())
    while a < length:
        lst.append(int(input("list[", a, "]: ")))
        time.sleep(0.5)
        a += 1
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
