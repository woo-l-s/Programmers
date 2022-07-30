# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)

def solution(s):
    answer = True
    if s.count('p') + s.count('P') == s.count('y') + s.count('Y'):
        return True
    else:
        return False





s = "pPoooyY"

r = solution(s)
print(r)



