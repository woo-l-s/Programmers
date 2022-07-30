# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)

def solution(s):
    if (len(s) == 4) or (len(s) == 6):
        if s.isdigit():
            return True
        else:
            return False
    else:
        return False





s = "a234"

r = solution(s)
print(r)



