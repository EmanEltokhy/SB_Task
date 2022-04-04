import numpy as np

FileOfWeights = open("weight.txt")
list = [0, 97, 97, 99, 101, 103, 196, 198, 200, 202, 295, 297, 299, 299, 301, 394, 396, 398, 400, 400, 497]

# Load weight file
weightsDict = {}
for line in FileOfWeights:
    line = line.rstrip()
    column = line.split(" ")
    weightsDict[column[0]] = int(column[1])


# Input

# SpectrumList = []
# size = int(input("Enter the size of the list "))
# SpectrumList = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:size]
# Spectrum list : 0 97 97 99 101 103 196 198 200 202 295 297 299 299 301 394 396 398 400 400 497
# its size : 21


def unique(list1) -> list:
    x = np.array(list1)
    list1 = np.unique(x)
    return list1


def InitialList():
    initialList = []
    for key in weightsDict:
        for j in range(len(list)):
            if weightsDict[key] == list[j]:
                initialList.append(key)
    return initialList


print(InitialList())


def isConsistent(word, list):
    for i in range(1, len(word) + 1):
        for j in range(0, len(word)):
            mers = word[j:j + i]
            sum = 0
            if len(mers) > 1:
                for AA in mers:
                    sum += weightsDict[AA]
                if sum not in list:
                    return False
            else:
                if weightsDict[mers] not in list:
                    return False
    return True


initial_list = InitialList()
size = len(initial_list)
NewList = []


def ExtendFunction(initial_list):
    for index in range(size):
        if index == 0:
            for i in range(0, len(initial_list)):
                for j in range(0, len(initial_list)):
                    if i == j:
                        continue
                    else:
                        newString = initial_list[i] + initial_list[j]
                        if isConsistent(newString, list):
                            NewList.append(newString)
            N_mers_list = unique(NewList)
            print(N_mers_list)
            NewList.clear()
        else:
            for i in range(0, len(N_mers_list)):
                for k in N_mers_list[i]:
                    initial_list.remove(k)
                for j in range(0, len(initial_list)):
                    newString = N_mers_list[i] + initial_list[j]
                    if isConsistent(newString, list):
                        NewList.append(newString)
                for k in N_mers_list[i]:
                    initial_list.append(k)
            N_mers_list = NewList
            N_mers_list = unique(N_mers_list)
            print(N_mers_list)
            NewList.clear()


ExtendFunction(initial_list)
