input = open("Day 3\input.txt", "r")

totalPrio = 0
batchCounter = 0
elfBatch = ['', '', '']

for line in input:
    temp = line.strip()
    # splitPos = int(len(temp) / 2) # Part 1
    # firstHalf = temp[:splitPos]
    # secondHalf = temp[splitPos:]

    # for char in secondHalf:
    #     if char in firstHalf:
    #         if (char.isupper()):
    #             totalPrio += ord(char) - ord('A') + 27
    #         else:
    #             totalPrio += ord(char) - ord('a') + 1
    #         break
    elfBatch[batchCounter] = temp
    if batchCounter != 2:
        batchCounter += 1
    else:
        elfBatch.sort(key=len)
        for char in elfBatch[0]:
            if char in elfBatch[1] and char in elfBatch[2]:
                if (char.isupper()):
                    totalPrio += ord(char) - ord('A') + 27
                else:
                    totalPrio += ord(char) - ord('a') + 1
                batchCounter = 0
                break


print(totalPrio)
