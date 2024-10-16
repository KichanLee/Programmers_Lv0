def solution(my_string):
    answer = ""
    for i in range(len(my_string)):
        if('a'<= my_string[i] <= 'z'):
            answer += chr(ord(my_string[i]) - 32)
        else:
            answer += chr(ord(my_string[i]) + 32)
    return answer
# ord 와 chr 에 대해서 알아야한다.
# 문자열은 수정이 안된다.
def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer
