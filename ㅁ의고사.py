# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)
from xlwt.compat import long


def solution(answers):
    answer = []
    a = [0,0,0]
    onesupo = [1, 2, 3, 4, 5]
    twosupo = [2, 1, 2, 3, 2, 4, 2, 5]
    threesupo = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(0, len(answers)):
        if answers[i] == onesupo[i%5]:
            a[0] += 1
            pass
        if answers[i] == twosupo[i%8]:
            a[1] += 1
            pass
        if answers[i] == threesupo[i % 10]:
            a[2] += 1
    # print(a[0])
    # print(a[1])
    # print(a[2])
    print(a)
    # print(a.index(max(a))+1)
    if a.count(max(a)) == 1:
        answer.append(a.index(max(a)) + 1)
        return answer
    else:
        for i in range(1, a.count(max(a))+1):
            answer.append(a.index(max(a))+1)
            a[a.index(max(a))] = 0
        return answer





answer = [3,3,2,3,5,3,3,2,3,5]
k = solution(answer)
print(k)
# a, b = map(int, input().strip().split(' '))
# k = a



# 65~122