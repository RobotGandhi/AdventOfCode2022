input = open("Day 2\input.txt", "r")

moveDict = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

scoreDict = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
    "Loss": 0,
    "Draw": 3,
    "Win": 6
}

resultDict = {
    "X": "Loss",
    "Y": "Draw",
    "Z": "Win"
}

totalScore = 0

def choosePlay(opponentPlay, desiredResult):
    yourPlay = ""
    match desiredResult:
        case "Draw":
            yourPlay = opponentPlay
        case "Win":
            match opponentPlay:
                case "Rock":
                    yourPlay = "Paper"
                case "Paper":
                    yourPlay = "Scissors"
                case "Scissors":
                    yourPlay = "Rock"
        case "Loss":
            match opponentPlay:
                case "Rock":
                    yourPlay = "Scissors"
                case "Paper":
                    yourPlay = "Rock"
                case "Scissors":
                    yourPlay = "Paper"
    print(desiredResult)
    return yourPlay

def calculateRoundScore(yourPlay, opponentPlay):
    result = ""
    match yourPlay:
        case "Rock":
            match opponentPlay:
                case "Rock":
                    result = "Draw"
                case "Paper":
                    result = "Loss"
                case "Scissors":
                    result = "Win"
        case "Paper":
            match opponentPlay:
                case "Rock":
                    result = "Win"
                case "Paper":
                    result = "Draw"
                case "Scissors":
                    result = "Loss"
        case "Scissors":
            match opponentPlay:
                case "Rock":
                    result = "Loss"
                case "Paper":
                    result = "Win"
                case "Scissors":
                    result = "Draw"
    return scoreDict[yourPlay] + scoreDict[result]


for line in input:
    #totalScore += calculateRoundScore(moveDict[line[2]], moveDict[line[0]]) # Part 1
    totalScore += calculateRoundScore(choosePlay(moveDict[line[0]], resultDict[line[2]]), moveDict[line[0]]) # Part 2

print(totalScore)