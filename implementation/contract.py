#2023 kakao blind recruitment
def solution(today, terms, privacies):
    answer = []
    dic_terms = set_terms(terms)
    privacy_form = set_privacies(privacies)
    for i in range(len(privacy_form)):
        if check_delete(today, dic_terms[privacy_form[i][0]], privacy_form[i][1]):
            answer.append(i+1)
    return answer

#약관 종류:유효기간 딕셔너리 형식으로 변환
def set_terms(terms):
    dic_terms = {}
    for i in range(len(terms)):
        form, month = terms[i].split()
        dic_terms[form] = int(month)
    return dic_terms

#개인정보 수집일자와 약관 종류 분리해서 저장
def set_privacies(privacies):
    privacy_form = [] 
    for privacy in privacies:
        form = privacy[-1]
        gather_date = privacy[:-1]
        privacy_form.append((form, gather_date))
    return privacy_form

#삭제해야할 약관 구하기
def check_delete(today, term, privacy):
    today_Y, today_M, today_D = map(int, today.split('.'))
    privacy_Y, privacy_M, privacy_D = map(int, privacy.split('.'))
    
    end_year, end_month, end_day = end_date(privacy_Y, privacy_M, privacy_D, term)
    #True는 삭제 / False는 보관
    if end_year < today_Y:
        return True
    elif end_year == today_Y:
        if end_month < today_M:
            return True
        elif end_month == today_M:
            if end_day < today_D:
                return True
    return False

#약관 만료 날짜
def end_date(year, month, day, term):
    if day == 1:
        end_day = 28
        month -= 1
    else:
        end_day = day-1
    
    end_month = month + term
    end_year = year+end_month//12
    end_month = end_month%12
    if end_month == 0:
        end_month = 12
        end_year -= 1
        
    return (end_year, end_month, end_day)