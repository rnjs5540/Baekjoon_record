def solution(survey, choices):    
    answer = ''
    scores = {'RT':0,'CF':0,'JM':0,'AN':0}
    for one_survey, choice in zip(survey, choices):
        choice -= 4
        if one_survey not in scores:
            one_survey = one_survey[::-1]
            print('뒤집')
            choice *= -1
        scores[one_survey] += choice
    print(scores)
    
    for key, val in scores.items():
        if val > 0:
            answer += key[1]
        else:
            answer += key[0]
    
    return answer