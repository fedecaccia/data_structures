def sort(s):

    l = ""
    u = ""
    n = ""

    for c in s:

        if c.isdigit():
            n += c
        elif c.isupper():
            u += c
        else:
            l += c

    return u+l+n


assert(sort("cdBnC52c") == "BCcdnc52")
assert(sort("123abA") == "Aab123")