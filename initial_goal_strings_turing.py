def isSubset(initial, partial_goal):

    if partial_goal in initial:
        return True

    lp = list(partial_goal)[::-1]
    li = list(initial)[::-1]

    pp = lp.pop()

    while len(li)>0:
        ii = li.pop()
        if ii==pp and len (lp)==0:
            return True

        if ii==pp:
            pp = lp.pop()        

    return False

def minimumConcat(initial, goal):
    #Put your code here

    # if initial == goal:
    #     return(1)

    ini = list(initial)
    g = list(goal)
    for gg in g:
        if gg not in ini:
            return(-1)

    still = goal
    n_sub=0

    # count = 0

    while len(still) > 0:
    # while len(still) > 0 and count<5:
        # count += 1
        # print("count", count)

        for i in range(len(still)):
            # print("i", i)

            if i == 0:
                if isSubset(initial, still):
                    n_sub += 1
                    still = ''
                    break
            else:
                if isSubset(initial, still[:-i]):
                    n_sub += 1
                    still = still[-i:]
                    break

    return(n_sub)


assert(isSubset('abc', 'abc'))
assert(isSubset('xyz', 'xz'))

assert(isSubset('abc', 'abc'))

assert (minimumConcat('abc', 'abc') == 1)
assert (minimumConcat('abc', 'abcd') == -1)
assert (minimumConcat('abcdef', 'abcdef') == 1)
assert (minimumConcat('abc', 'g') == -1)
assert (minimumConcat('abc', 'acdbc') == -1)
assert (minimumConcat('abc', 'abcbc') == 2)
assert (minimumConcat('xyz', 'xzyxz') == 3)