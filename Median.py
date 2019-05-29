def List_Sorter_median():
    print("Now that you've sorted your list, this will find the median!")
    userIn = ""
    lst = []
    while userIn != "stop":
        userIn = input()
        if userIn != "stop":
            lst.append(int(userIn))
    if len(lst) % 2 == 0:
        median1 = lst[int((len(lst) / 2) - 0.5)]
        median2 = lst[int((len(lst) / 2) + 0.5)]
        median = (median1 + median2) / 2
    else:
        median = lst[len(lst) / 2]
    return median
