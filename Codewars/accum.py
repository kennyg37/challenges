def accum(st):
    return "-".join(i.upper() + i.lower() * index for index, i in enumerate(st))

print(accum("hello"))
