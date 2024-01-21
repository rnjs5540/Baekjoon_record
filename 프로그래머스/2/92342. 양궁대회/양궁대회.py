from itertools import combinations_with_replacement
def solution(n, apeach_answer):
    # nums = [0,1,2,3,4,5,6,7,8,9,10] # 작은 수부터 조합을 만들기 때문에 점수차같을때 가장 낮은거 먼저
    nums = [10,9,8,7,6,5,4,3,2,1,0]
    result = [-1]
    
    # 점수 계산 함수
    def calc_score():
        lion_score=0
        apeach_score=0
        
        for i in range(10):
            if lion_answer[i] == 0 and apeach_answer[i] == 0:
                continue
            elif lion_answer[i] > apeach_answer[i]:
                lion_score += 10-i
            else:
                apeach_score += 10-i
            # if lion_answer[i] == 0 and apeach_answer[i] == 0:
            #     continue
            # if lion_answer[i] > apeach_answer[i]:
            #     lion_score += (10-i)
            # else: apeach_score += (10-i)
            
        return lion_score, apeach_score
    
    def is_efficient(lion_answer):
        # 10~1점 중 비효율적인 것 있는지 체크
        for i in range(10):
            if lion_answer[i] > apeach_answer[i] + 1:
                return False
            if 0 < lion_answer[i] and lion_answer[i] <= apeach_answer[i]:
                return False

            # # 점수따는데 필요한 것보다 불필요하게 많은 화살 쏨
            # if lion_answer[index] < 0:
            #     return False
            # lion_answer[index] -= 1
        
        # 0점이 아닌 곳 중 점수 못얻을 정도만 화살 쏜 곳 있는지 체크
        # for i in range(9):
        #     if lion_answer_copy[i] > 0:
                
        return True

    
    maximum_diff=0
    # 라이언이 쏜 화살s
    for arrows in combinations_with_replacement(nums,n):
        # # 어피치보다 1개만 더 쏘면 댐
        lion_answer = [0 for _ in range(11)]
        for arrow in arrows:
            lion_answer[arrow] += 1
        
        if not is_efficient(lion_answer):
            continue
            
        lion_score,apeach_score = calc_score()
        
        if maximum_diff < lion_score - apeach_score:
            maximum_diff = lion_score - apeach_score
            result = lion_answer

            
    return result

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
