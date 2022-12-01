import login_info
import requests
import ast

current_day = 0

def get_daily_input():
    try:
        input = open("day{day}.txt".format(day=current_day), "r").readlines()
        return [__tryeval(i) for i in input]
    except FileNotFoundError:
        uri = 'http://adventofcode.com/2022/day/{day}/input'.format(day=current_day)
        response = requests.get(uri, cookies={'session': login_info.SESSION_ID}, headers={'User-Agent': 'github.com/Maximo1491/AdventOfCode2022 by maximo1491@hotmail.com'})
        f = open("day{day}.txt".format(day=current_day), "w")
        f.write(response.content.decode("utf-8"))
        f.close()
        input = open("day{day}.txt".format(day=current_day), "r").readlines()
        return [__tryeval(i) for i in input]

def __tryeval(val):
    if val == "\n":
        return val

    try:
        return ast.literal_eval(val)
    except ValueError:
        print(f"Error in __tryeval, failed to convert {val}")
        pass

    