file = open("weight.txt")

proteindic = {}
for line in file:
    line = line.strip()
    llist = line.split(" ")
    proteindic[llist[0]] = int(llist[1])
def isConsistent(word,list):
    for i in range(1, len(word)+1):
        for j in range(0, len(word)):
            merc = word[j:j + i]
            sum = 0
            if len(merc)>1:
                for l in merc:
                   sum+=proteindic[l]
                if sum not in list:
                    return False
            else:
                if proteindic[merc] not in list:
                    return False
    return True

