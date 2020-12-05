def commonChars(s1, s2):
    s = None
    if (len(s1) < len(s2)):
        s = s1
        l = s2
    else:
        s = s2
        l = s1

    c = 0
    for i in s:
        if i in l:
            c = c + 1
    return c
    

print(commonChars('hello','world'))
