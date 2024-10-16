def solution(array):
    return [max(array) ,array.index(max(array))]


# 크기비교를 통해 max를 파악한다.
def solution(array):
    answer = [0, 0]
    num = array[0]
    for i in range(len(array)):
        if num < array[i]:
            num = array[i]
            answer[0] = num
            answer[1] = i
    return answer