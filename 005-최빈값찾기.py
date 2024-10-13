def solution(array):    
    check_list = [0] * 1000

    for i in array:
        check_list[i] += 1
    
    cnt = 0
    answer = 0
    for j in range(len(check_list)):
        if(check_list[j] == max(check_list)):
            cnt += 1
            answer = j
    
    if(cnt > 1):
        return -1
    return answer

'''
    다른 사람의 풀이


    idx = [0] * 1001

    for i in array:
        idx[i] += 1
    
    if(idx.count(max(idx) > 1)
        return -1
    return idx.index(max(idx))

'''