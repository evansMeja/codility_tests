"""
check number of common letters in two strings

example 

'hello' and 'well' return 3 coz l appears twice and e appears once
"""
def commonChars(s1, s2):
    c = 0
    cT = []
    t=0
    c = []
    for i in s1:
        if i not in c:
            oc = 0
            time_it_appears_s1 = s1.count(i)
            time_it_appears_s2 = s2.count(i)
            if time_it_appears_s1 != 0 and time_it_appears_s2 != 0:   
                if time_it_appears_s1 < time_it_appears_s2:
                    oc = time_it_appears_s1
                else:
                    if time_it_appears_s2 < time_it_appears_s1:
                        oc = time_it_appears_s2
                    else:
                        oc = time_it_appears_s2
                t = t + oc
            c.append(i)
    return t
