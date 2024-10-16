def solution(numer1, denom1, numer2, denom2):
    
    answer = [denom1 * numer2 + denom2 * numer1, denom1 * denom2]
    gcd = 1
    maxx = min(answer[0], answer[1])
    for i in range(1, maxx + 1):
        if(answer[0] % i == 0 and answer[1] % i == 0):
            gcd = i
    
    return [answer[0] // gcd, answer[1] // gcd]

# 이렇게 하면 시간복잡도가 O(N)
# 하지만 유클리드 최대공약법을 사용하는 방법이 있다.
'''
    처음에 두수중 max값을 기준으로 했는데 그것보다 min으로
    하는게 최대공약수에 알맞는 방법이다.

    부가적으로 최소공배수는 어떻게 구할것인가?

    두 수의 곱 / gcd

'''
import math

def solution(numer1, denom1, numer2, denom2):
    # 분수 더하기
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2

    # 최대공약수 구하기
    gcd = math.gcd(numer, denom)

    # 기약분수로 만들기
    return [numer // gcd, denom // gcd]