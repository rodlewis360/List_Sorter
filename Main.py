def List_Sorter_main():
    print("Enter your list using the steps bellow!")
    lst = []
    print("Input the numbers one by one!")
    print("Press \"stop\" when you are done!")
    userIn = ""
    while userIn != "stop":
        userIn = input()
        if userIn != "stop":
            lst.append(int(userIn))
    dictionary = {}
    for a in lst:
        c = 0
        for b in lst:
            if a > b:
                c += 1
        dictionary[a] = c
    a = 0
    newlst = []
    while a < len(lst):
        newlst.append(0)
        a += 1
    for a in dictionary:
        newlst[dictionary.get(a)] = a
    return newlst
