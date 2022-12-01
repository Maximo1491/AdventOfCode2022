import helper

def part1():
    input = helper.get_daily_input()
    current_count = 0
    hightest_count = 0
    for i in input:
        if i == "\n":
            if current_count > hightest_count:
                hightest_count = current_count
            current_count = 0
            continue
        current_count += i

    return hightest_count

def part2():
    input = helper.get_daily_input()
    count = 0
    values = []
    for i in input:
        if i == "\n":
            values.insert(1, count)
            count = 0
            continue
        count += i

    values.sort(reverse=True)

    return values[0] + values[1] + values[2]