def commonChars(s1, s2):
    c = 0
    cT = []
    for i in s1:
        if i in s2 and i not in cT:
            c = c + 1
            cT.append(i)
    return c  

print(commonChars('hellt','worrdl'))
