input = open("Day 7\input.txt", "r")

content = input.readlines()
currentLineNumber = 1
result = 48381165
minimum = 8381165

def sizeOfDirectory(name):
    size = 0
    global currentLineNumber
    global result
    while True:
        currentLineNumber = currentLineNumber + 1
        if currentLineNumber >= len(content): break
        temp = content[currentLineNumber].strip().split(" ")
        if temp[0] == "$":
            if temp[2] == "..":
                break
            else: 
                currentLineNumber += 1
                size += sizeOfDirectory(temp[2])
        elif temp[0] != "dir":
            size += int(temp[0])
    # if size <= 100000: # Part 1
    #     print(name + ": " + str(size))
    #     result += size
    if minimum <= size <= result:
        print("New minimum: " + name + " with size " + str(size))
        result = size
    return size

sizeOfDirectory("/")

print(result)