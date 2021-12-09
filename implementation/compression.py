import sys
def solution(input_s):
    length = len(input_s)
    
    result = []
    count = 1

    comparison = length
    check_len = 0

    #문자열의 크기를 1부터 전체 길이의 절반까지 순차대로 늘리면서 압축실행
    for i in range(1, (length//2)+1):
        #압축이 가능한지 비교하는 문자열
        base = input_s[:i]
        
        for j in range(i+i , length+1, i):
            #문자열이 압축 가능하면 count를 추가하고 다음 문자열 검사
            if input_s[j-i:j] == base:
                count += 1
                continue
            #비교 문자열과 다음 문자열이 다를 경우 
            else:
                #count가 1이 아닐 경우 result 리스트에 숫자를 추가
                if count > 1:
                    result.append(str(count))
                
                result.append(base)    

            #문자열 마지막까지 result에 담겼는지 확인을 위한 변수 check_len
            check_len += (count*i)    
            count = 1        

            #비교 문자열을 새로운 문자열로 수정
            base = input_s[j-i:j]

        #문자열을 다 돌고 마지막 문자열(base)을 추가할 지 확인
        if count != 1:
            result.append(str(count))

            check_len += (count*i)
            count = 1
            result.append(base)

        #result에 담긴 문자열이 입력된 문자열을 압축한 것보다 짧으면 남은 문자들 추가
        if check_len < length:
            temp_s = input_s[check_len:]
            result.append(temp_s)

        check_len = 0

        temp = len(''.join(result))
        
        result = []

        if temp < comparison:
            comparison = temp

    return comparison

################################################################################################################
#참신한 풀이#
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution_new(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
##############################################################################################################

input_s = sys.stdin.readline().strip()

print(solution(input_s))
print(solution_new(input_s))