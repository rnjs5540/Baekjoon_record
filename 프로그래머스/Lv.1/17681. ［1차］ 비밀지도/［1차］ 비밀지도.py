def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append("")
    
    for r in range(n):
        n1 = format(arr1[r], 'b').zfill(n)
        n2 = format(arr2[r], 'b').zfill(n)
        print(n1, n2)
        
        for c in reversed(range(n)):
            if n1[c] == '1' or n2[c] == '1':
                answer[r] = '#' + answer[r]
            else:
                answer[r] = ' ' + answer[r]
            
    return answer