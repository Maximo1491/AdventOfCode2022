import helper

def part1():
    input = helper.get_daily_input()
    score = 0

    for i in input:
        throws = i.split(" ")
        throws[1] = throws[1].strip()
        if throws[0] == "A":
            if throws[1] == "X":
                score += 4
            elif throws[1] == "Y":
                score += 8
            elif throws[1] == "Z":
                score += 3
        elif throws[0] == "B":
            if throws[1] == "X":
                score += 1
            elif throws[1] == "Y":
                score += 5
            elif throws[1] == "Z":
                score += 9
        elif throws[0] == "C":
            if throws[1] == "X":
                score += 7
            elif throws[1] == "Y":
                score += 2
            elif throws[1] == "Z":
                score += 6
    return score

def part2():
    input = helper.get_daily_input()
    score = 0

    for i in input:
        throws = i.split(" ")
        throws[1] = throws[1].strip()
        if throws[0] == "A":
            if throws[1] == "X":
                score += 3
            elif throws[1] == "Y":
                score += 4
            elif throws[1] == "Z":
                score += 8
        elif throws[0] == "B":
            if throws[1] == "X":
                score += 1
            elif throws[1] == "Y":
                score += 5
            elif throws[1] == "Z":
                score += 9
        elif throws[0] == "C":
            if throws[1] == "X":
                score += 2
            elif throws[1] == "Y":
                score += 6
            elif throws[1] == "Z":
                score += 7
    return score