s = 'azcbobobegghakl'
finS = ""

for begIndex in s:
    subS = begIndex
    num = s.index(begIndex)+1
    for endIndex in s[num: ]:
        if endIndex >= subS [-1]:
            subS += endIndex
            if len(subS) > len(finS):
                finS = subS
        else :
            break


print ("Longest substring in alphabetical order is:", finS)
