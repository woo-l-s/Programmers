# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)




def solution(n):
    k = str(n)
    list = []
    for i in k:
        list.append(int(i))


    return sum(list)



n = 123
k = solution(n)
print(k)

# 65~122