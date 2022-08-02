# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)
from xlwt.compat import long


def solution(num):
    n = long(num)
    # print(n)
    cnt = 0
    while(1):
        if n == 1:
            return cnt
            break
        if n >500:
            return -1

        else:
            if n % 2 == 0:
                n = n/2
                cnt+=1
            else:
                n = n * 3 + 1
                cnt+=1
        print(n)



num = 100
k = solution(num)
print(k)

# 65~122