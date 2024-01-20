def getList(str1):
    list1 = []
    for i in range(len(str1)-1):
        if not str1[i].isalpha() or not str1[i+1].isalpha():
            continue
        list1.append(str1[i] + str1[i+1])
    return list1

def getUsado(list1, list2):
    if len(list1) == 0 and len(list2) == 0:
        return 1
    
    sameCount = 0
    for el in list1:
        if el in list2:
            list2.remove(el)
            sameCount += 1
    hapJipHap = list1 + list2
    return sameCount / len(hapJipHap)
        

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    list1 = getList(str1)
    list2 = getList(str2)
    print(list1)
    print(list2)
    usado = getUsado(list1, list2)
    print(usado)
    answer = int(usado * 65536)
    print(int(answer))
    
    return answer