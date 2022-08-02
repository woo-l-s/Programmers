# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)




def solution(n,m):
    k = n* m
    n_list = []
    m_list = []
    ans = []
    for i in range(1,n+1):
        if n % i == 0:
            n_list.append(i)
    n_list = set(n_list)
    for i in range(1,m+1):
        if m % i == 0:
            m_list.append(i)
    m_list = set(m_list)
    a = max(n_list & m_list)
    ans.append(a)

    for i in range(1,k+1):
        if i%n == 0 and i%m == 0:
            ans.append(i)
            break
    return ans
n = 2
m = 5
k = solution(n,m)
print(k)

# 65~122