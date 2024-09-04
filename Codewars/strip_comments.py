def strip_comments(string, markers):
    lines = string.split('\n')
    result = []
    
    for line in lines:
        for marker in markers:
            if marker in line:
                line = line.split(marker)[0].rstrip()
        result.append(line)
    
    return '\n'.join(result)

print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])) 