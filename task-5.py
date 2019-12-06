w1 = list(s1)
w2 = list(s2)

def twoStrings(s1, s2):
    a = any(elem in s1 for elem in s2)
    if a:
        return 'YES'
    else:
        return 'NO'