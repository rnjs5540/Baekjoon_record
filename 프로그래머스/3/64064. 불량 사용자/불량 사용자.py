def is_same(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    for ch1, ch2 in zip(user_id, banned_id):
        if ch2 != '*' and ch1 != ch2:
            return False
    return True


def dfs(same_lists, list_index, cur_list, answer_set):  
    
    for el in same_lists[list_index]:
        if el in cur_list:
            continue
        cur_list.append(el)
        
        if len(cur_list) == len(same_lists):
            answer_set.add(tuple(sorted(cur_list)))
            
        if list_index + 1 < len(same_lists):
            dfs(same_lists, list_index+1, cur_list, answer_set)
        cur_list.remove(el)
        
            
def solution(user_ids, banned_ids):
    answer_set = set()
    same_lists = []
    for banned_id in banned_ids:
        same_list = []  # banned_id당 일치하는 아이디들
        for user_id in user_ids:
            if is_same(user_id, banned_id):
                same_list.append(user_id)
        same_lists.append(same_list)
    
    dfs(same_lists, 0, [], answer_set)
    
    return len(answer_set)