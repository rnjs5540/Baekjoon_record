def solution(survey, choices):    
    answer = ''
    correct_order = ("RT", "CF", "JM", "AN")
    scores = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for one_survey, choice in zip(survey, choices):
        scores[one_survey[1]] += choice-4
    print(scores)
    
    def get_answer(answer, A, B):
        if scores[A] < scores[B]:
            answer += B
        else:
            answer += A
        return answer
    
    for order in correct_order:
        answer = get_answer(answer, order[0], order[1])
    
    return answer