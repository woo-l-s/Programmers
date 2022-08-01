# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)




def solution(n):
    answer = 0
    list = []
    for i in range(1,n+1):
        if (n % i) == 0:
            list.append(i)
    return sum(list)



n = 12
k = solution(n)
print(k)

# 65~122