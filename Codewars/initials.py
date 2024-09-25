"""Code to convert names to initials """
def abbrev_name(name):
    initials = []
    name = name.upper()
    
    for index, char in enumerate(name):
        if index == 0 or name[index - 1] == " ":
            initials.append(char)
            
        dotted = '.'.join(initials)
    return dotted            


print(abbrev_name("ken ganza"))