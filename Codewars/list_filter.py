def filter_list(l):
    new_arr = []
    for i in l:
        if not isinstance(i, str):
            new_arr.append(i)
    return new_arr


print(filter_list([1,2,'a','b']))