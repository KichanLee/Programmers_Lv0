def solution(n):
    answer = []
    for i in range(1, n + 1):
        if(i % 2 == 1):
            answer.append(i)
    return answer


'''
처음에 시도한 코드
for i in range(n):
    if(n % i == 1)

이렇게 하게 되면 n이 계속입력되어서 
잘못된 코드인것을 늦게 알았다
sorted()를 쓰게 되면 새롭게 배열이 생성된다.


다른 사람풀이

def soultion(n):
    return list(range(1, n+1, 2))


'''
