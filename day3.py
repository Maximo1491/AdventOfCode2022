import helper

def part1():
    input = helper.get_daily_input()
    count = 0
    for i in input:
        compartment1 = i[:int(len(i)/2)]
        compartment2 = i[int(len(i)/2):]
        for c in compartment1:
            if c in compartment2:
                if(c.isupper()):
                    count += ord(c) - 38
                else:
                    count += ord(c) - 96
                break
    return count

def part2():
    input = helper.get_daily_input()
    input = [input[i:i + 3] for i in range(0, len(input), 3)]
    count = 0
    for i in input:
        group = i
        for g in group[0]:
            if g in group[1] and g in group[2]:
                if(g.isupper()):
                    count += ord(g) - 38
                else:
                    count += ord(g) - 96
                break
    return count