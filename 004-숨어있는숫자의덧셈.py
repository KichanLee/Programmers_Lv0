def solution(my_string):
    answer = 0

    for i in my_string:
        if(i.isdigit()):
            answer += int(i)
    return answer


'''
내가 원래 풀고자 했더 방식

def solution(my_string):
    answer = 0

    for i in my_string:
        if '0' <= i <= '9':  # 숫자인지 확인
            answer += ord(i) - ord('0')  # ASCII 코드로 숫자 변환
    return answer

ord는 ascii코드로 변환해주는 함수

'''