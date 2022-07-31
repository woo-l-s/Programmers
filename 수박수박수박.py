# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)




def solution(n):
    answer = '수박'
    if n % 2 == 0:
        return answer * int(n/2)
    else:
        return answer * int(n / 2) + '수'
    return answer


n = 3
k = solution(n)
print(k)
