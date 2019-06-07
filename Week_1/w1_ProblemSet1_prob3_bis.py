s = 'azcbobobegghakl'
finS = ""
begIndex = 0
while begIndex < len(s):
    subS = s[begIndex]
    for endIndex in s[begIndex +1: ]:
        if endIndex >= subS [-1]:
            subS += endIndex
            if len(subS) > len(finS):
                finS = subS
        else :
            if finS == "":
                finS = s[0]
            break
    begIndex += 1

print ("Longest substring in alphabetical order is:", finS)

