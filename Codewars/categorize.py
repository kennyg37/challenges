def open_or_senior(data):
    results = []
    
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            results.append("Senior")
        else:
            results.append("open")
                
    return results
    
    
print(open_or_senior( [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))