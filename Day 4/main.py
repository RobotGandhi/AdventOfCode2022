input = open("Day 4\input.txt", "r")

containCount = 0

def isSubAssignment(smallAssignment, largeAssignment):
    #return smallAssignment[0] >= largeAssignment[0] and smallAssignment[1] <= largeAssignment[1] # Part 1
    return largeAssignment[0] <= smallAssignment[0] <= largeAssignment[1] or largeAssignment[0] <= smallAssignment[1] <= largeAssignment[1] # Part 2

for line in input:
    temp = line.strip()
    assignments = temp.split(",")
    firstElfAssignment = [int(i) for i in assignments[0].split("-")]
    secondElfAssignment = [int(i) for i in assignments[1].split("-")]
    
    firstElfAssignmentLength = int(firstElfAssignment[1]) - int(firstElfAssignment[0])
    secondElfAssignmentLength = int(secondElfAssignment[1]) - int(secondElfAssignment[0])

    if firstElfAssignmentLength > secondElfAssignmentLength:
        containCount += isSubAssignment(secondElfAssignment, firstElfAssignment)
    else:
        containCount += isSubAssignment(firstElfAssignment, secondElfAssignment)

print(containCount)