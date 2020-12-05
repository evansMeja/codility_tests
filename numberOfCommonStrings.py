"""
check number of common letters in two strings

example 

'hello' and 'well' return 3 coz l appears twice and e appears once
"""
def commonChars(s1, s2):
    c = 0
    cT = []
    for i in s1:
        if i in s2 and i not in cT:
            c = c + 1
            cT.append(i)
    t = 0

    for i in cT:
        oc = 0
        time_it_appears_s1 = 0
        for x in s1:
            if i == x:
                time_it_appears_s1 = time_it_appears_s1 + 1
        
        time_it_appears_s2 = 0

        print(time_it_appears_s1)
        
        for x in s2:
            if i == x:
                time_it_appears_s2 = time_it_appears_s2 + 1

        print(time_it_appears_s2)

        if time_it_appears_s1 < time_it_appears_s2:
            oc = time_it_appears_s1
        else:
            if time_it_appears_s2 < time_it_appears_s1:
                oc = time_it_appears_s2
            else:
                if time_it_appears_s2 == time_it_appears_s2:
                    oc = time_it_appears_s2
        t = t + oc
    return t

print(commonChars('helltth','worrdllh'))
