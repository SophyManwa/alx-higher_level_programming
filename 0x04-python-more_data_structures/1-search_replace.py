#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mylist = []
    for item in my_list:
        if item == search:
            mylist.append(replace)
        else:
            mylist.append(item)
            return mylist
