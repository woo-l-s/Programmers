# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)




def solution(n):
    k = n ** (1/2)
    if k % 1 == 0:
        return (k+1)**2
    else:
        return -1





n = 121
k = solution(n)
print(k)

# 65~122