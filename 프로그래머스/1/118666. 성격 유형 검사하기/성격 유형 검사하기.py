def solution(survey, choices):
    answer = ''
    scores = {
        'RT':0,
        'CF':0,
        'JM':0,
        'AN':0,
    }
    
    for s, c in zip(survey, choices):
        c -= 4
        if s == 'TR' or s == 'FC' or s == 'MJ' or s == 'NA':
            c *= -1
            # tmp = s[0]
            # s[0] = s[1]
            # s[1] = tmp
            # 파이썬에선 str이 아이템 수정이 안된다네,,
            s = s[1] + s[0]
        scores[s] += c
    
    for key, val in scores.items():
        if val <= 0:
            answer += key[0]
        else:
            answer += key[1]
    
    return answer 