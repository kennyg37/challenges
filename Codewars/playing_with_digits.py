def dig_pow(n, p):
    num_list = []
    for index, num in enumerate(str(n)):
        new = int(num)**p
        p += 1
        num_list.append(new)
    int_sum = sum(num_list)
    if int_sum % n == 0:
        k = round(int_sum/n)
        return k
    else:
        return -1
        
        
print(dig_pow(46288, 3))
        