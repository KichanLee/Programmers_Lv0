def solution(s1, s2):

    answer = 0
    for x in s1:
        for y in s2:
            if(x == y):
                 answer +=1
    return answer
# 내꺼 시간복잡도 n^2

'''
def solution(s1, s2):
    answer = 0

    이사람꺼는 O(N)

    for word in s1:
        if word in s2:
            answer += 1
        else:
            continue

    return answer


'''