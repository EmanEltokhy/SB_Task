FileOfWeights = open("weight.txt")
weightsDict = {}
for line in FileOfWeights:
      line = line.rstrip()
      column = line.split(" ")
      weightsDict[column[0]] = int(column[1])
#print(weightsDict)
SpectrumList = []
size = int(input("Enter the size of the list "))
SpectrumList = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:size]
#Spectrum list : 0 97 97 99 101 103 196 198 200 202 295 297 299 299 301 394 396 398 400 400 497
#its size : 21
def InitialList():
      initialList = []
      for key in weightsDict:
        for j in range(len(SpectrumList)):
          if weightsDict[key] == SpectrumList[j]:
            initialList.append(key)
      return initialList, len(initialList)

print(InitialList())
