def solution(data, ext, val_ext, sort_by):
    answer = []
    dic_data = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    for d in data:
        if d[dic_data[ext]] < val_ext:
            answer.append(d)
    answer.sort(key=lambda x:x[dic_data[sort_by]])
    
    return answer