input = open("Day 5\input.txt", "r")

setup = True
state = [[] for i in range(9)]

for line in input:
    if line.strip() == "": continue
    if line.find("1") != -1 and setup == True:
        setup = False
        for list in state:
            list.reverse()
        continue
    if setup:
        temp = line[1::4]
        for i in range(len(temp)):
            if temp[i] != " ":
                state[i].append(temp[i])
    else:
        commands = line.split(" ")
        
        amount = int(commands[1])
        origin = int(commands[3]) - 1
        to = int(commands[5]) - 1

        # for i in range(amount): # Part 1
        #     state[to].append(state[origin].pop())

        for i in range(amount):
            state[to].append(state[origin].pop(-(amount - i)))


for list in state:
    print(list.pop())