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
    elif len(r_s1) < len(r_s2) :
        big = list(r_s2)
        sml = list(r_s1)
    else:
        if int(s1) > int(s2):
            big = list(r_s1)
            sml = list(r_s2)
        else:
            big = list(r_s2)
            sml = list(r_s1)
    
    for i in range(len(sml)):
        if big[i] >= sml[i]:
            x = str(int(big[i]) - int(sml[i]))
            new.append(x)
        else:
            x = str((int(big[i]) + 10) - int(sml[i]))
            big[i+1] = str(int(big[i+1]) - 1)
            new.append(x)
    for i in range(len(new)):
        big[i] = new[i]
    for i in reversed(big):
        res.append(i)
    strk_res = ''.join(res)
    
    return strk_res



