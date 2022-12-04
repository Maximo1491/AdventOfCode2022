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
        response = requests.get(uri, cookies={'session': login_info.SESSION_ID}, headers={'User-Agent': login_info.USER_AGENT})
        f = open("day{day}.txt".format(day=current_day), "w")
        f.write(response.content.decode("utf-8"))
        f.close()
        input = open("day{day}.txt".format(day=current_day), "r").readlines()
        return [__tryeval(i) for i in input]

def __tryeval(val):
    try:
        return ast.literal_eval(val)
    
    #Means its a more complex string so just pass the whole line back
    except SyntaxError:
        return val.strip()
    except ValueError:
        return val.strip()

    