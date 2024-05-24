# "8zerothree2" → 8032
# "seven73nine" → 7739
# "two53eightfour" → 25384
def solution(s):
    num_dict = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }
    
    for str in num_dict:
        
        s = s.replace(str, num_dict[str])
    answer = int(s)
    return answer
