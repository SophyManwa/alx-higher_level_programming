#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mylist = []
    for item in range(len(my_list)):
        if my_list[item] == search:
            mylist.append(replace)
        else:
            mylist.append(mylist[item])
            return mylist
