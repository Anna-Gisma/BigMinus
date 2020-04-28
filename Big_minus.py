def BigMinus(s1, s2):
    new = []
    res = []
    r_s1 = []
    r_s2 = []
    for i in reversed(s1):
        r_s1.append(i)

    for i in reversed(s2):
        r_s2.append(i)

    if len(r_s1) > len(r_s2):
        big = list(r_s1)
        sml = list(r_s2)
    else:
        big = list(r_s2)
        sml = list(r_s1)
    
    for i in range(len(s2)):
        if r_s1[i] >= r_s2[i]:
            x = str(int(r_s1[i]) - int(r_s2[i]))
            new.append(x)
        else:
            x = str((int(r_s1[i]) + 10) - int(r_s2[i]))
            r_s1[i+1] = str(int(r_s1[i+1]) - 1)
            new.append(x)
    for i in range(len(new)):
        r_s1[i] = new[i]
    for i in reversed(r_s1):
        res.append(i)
    strk_res = ''.join(res)
    
    return strk_res


import random
strk = []
for i in range(10**2):
    a = str(random.randint(1, 9))
    strk.append(a)
strkstr = ''.join(strk)
s1 = strkstr
s2 = '1'
print('str', strkstr)
print('big', BigMinus(s1, s2))
