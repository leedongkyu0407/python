def prepare(a):
    ls = []
    temp = ''
    for s in a:
        if s != '+' and s != '-':
            temp += s
        
        else:
            ls.append(int(temp))
            ls.append(s)
            temp = ''

    ls.append(int(temp))

    return ls

def solution(ls):
    minus_count = 0
    result = 0

    for l in ls:
        if l == '-':
            minus_count += 1
            continue
        elif l == '+':
            continue

        else:
            if minus_count != 0:
                result -= l
            
            else:
                result += l

    return result

def opt_solution(a):
    ls = []
    result  = 0

    for i in a[0].split('+'):
        result += int(i)

    for i in a[1:]:
        for j in i.split('+'):
            result -= int(j)

    return result

a = input().split('-') #- 기준으로 문자열 분리
print(opt_solution(a))
'''
input()으로 그냥 받아왔을 경우 사용
    ls = prepare(a)
    print(solution(ls))
'''