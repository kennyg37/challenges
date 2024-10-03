def dig_pow(n, p):
    num_list = []
    for index, num in enumerate(str(n)):
        print(str(n))
        new = int(num)**p
        num_list.append(new)
        p += 1
    print(num_list)
        
    for i in num_list:
        int_sum = sum(num_list)
        print(int_sum)
        if int_sum % n == 0:
            k = (int_sum/n)
            k = round(k)
            return k
        else:
            return -1
        
        
print(dig_pow(46288, 3))
        