input = open("Day 1\input.txt", "r")

bestElves = [0, 0, 0]
bestElvesCalories = [0, 0, 0]

currentElf = 1
currentCalories = 0

for line in input:
    if line == "\n":
        if currentCalories > bestElvesCalories[0]:
            bestElvesCalories[2] = bestElvesCalories[1]
            bestElvesCalories[1] = bestElvesCalories[0]
            bestElvesCalories[0] = currentCalories
            bestElves[2] = bestElves[1]
            bestElves[1] = bestElves[0]
            bestElves[0] = currentElf
        elif currentCalories > bestElvesCalories[1]:
            bestElvesCalories[2] = bestElvesCalories[1]
            bestElvesCalories[1] = currentCalories
            bestElves[2] = bestElves[1]
            bestElves[1] = currentElf
        elif currentCalories > bestElvesCalories[2]:
            bestElvesCalories[2] = currentCalories
            bestElves[2] = currentElf
        currentCalories = 0
        currentElf += 1
    else:
        currentCalories += int(line)

print(bestElves)
print(bestElvesCalories)
print(sum(bestElvesCalories))
