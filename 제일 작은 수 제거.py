# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)




def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0:
        return [-1]
    else:
        return arr






arr = [4,3,2,1]
k = solution(arr)
print(k)

# 65~122