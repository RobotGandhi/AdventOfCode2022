input = open("Day 6\input.txt", "r")
counter = 0
bufferMaxSize = 4
buffer = []
for line in input:
    for char in line:
        counter += 1
        buffer.append(char)
        if len(buffer) == bufferMaxSize:
            if len(buffer) != len(set(buffer)):
                buffer.pop(0)
            else: 
                if bufferMaxSize == 4:
                    bufferMaxSize = 14
                else: break

print(counter)

