def alternate(word1, word2):
    
    new = ""
    i = 0
    
    while i < max(len(word1), len(word2)):
        if i < len(word1):
            new += word1[i]
        else:
            pass
        
        if i < len(word2):
            new += word2[i]
        
        i += 1
        
    return new

print(alternate("right", "left"))