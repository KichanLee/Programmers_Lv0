
def solution(rsp):
    answer = ""
    for x in rsp:
        if(x == '2'):
            answer += "0"
        elif(x == '0'):
            answer += "5"
        elif(x == '5'):
            answer += "2"
    return answer

'''
def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp
'''