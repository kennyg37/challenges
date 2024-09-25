"""This code takes in a list, array or string and returns a new list of
of unique values but in order
"""
def unique_in_order(sequence):
    new = []
    for i in sequence:
        if len(new) == 0 or i != new[-1]:
            new.append(i)
    return new
    
print(unique_in_order([1,2,2,3]))