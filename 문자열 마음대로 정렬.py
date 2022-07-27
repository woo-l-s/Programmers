# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)

def solution(strings, n):
    str = []
    for i in strings:
        str.append(i[n] + i)
    str.sort()
    return [i[1:] for i in str]




strings = ["sun", "bed", "car"]
n = 1

r = solution(strings, n)
print(r)



