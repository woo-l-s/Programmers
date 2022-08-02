# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)




def solution(n):
    k = str(n)
    list = []
    for i in k:
        list.append(i)
    list.sort()
    list.reverse()
    n = '"'+str("".join(list)) + '"'


    return n



n = 118372
k = solution(n)
print(k)

# 65~122