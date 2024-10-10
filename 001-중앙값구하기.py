def solution(array):
    array.sort()

    return  array.pop(int(len(array) //2) )

# /2 해서 float으로 형변환이 되었고 오류가 발생했다.
# // 을 통해서 몫을 적극 활용할것
# 다른 사람 풀이


return sorted(array)[len(array) // 2]
array = [3, 1, 4, 1, 5]
sorted_array = sorted(array)
print(sorted_array)  # [1, 1, 3, 4, 5]
print(array)  # [3, 1, 4, 1, 5] (원본 배열은 그대로)


