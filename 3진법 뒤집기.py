# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)
from xlwt.compat import long

# Not_prime = []
# def prime_number(number):  # number를 입력 받아 소수인지 아닌지 구분하는 함수
#     if number in Not_prime:
#         pass
#     # number가 1이 아니면, (1은 소수가 아님)
#     if number != 1:
#         # 2, 3, 4, ..., (number - 1)까지의 인수에 대해서
#         for f in range(2, number):
#             # number가 위의 인수 중의 하나로 나누어지면, (나머지가 0이면)
#             if number % f == 0:
#                 return False  # 소수가 아님
#     else:  # number가 1이라면,
#         return False  # 소수가 아님
#
#     # number가 1이 아니면서, 2부터 (number - 1)까지의 수로 나눠지지 않으므로
#     # 소수로 판별됨 (소수는 1과 자신만을 인수로 갖는 수)
#     return True


def solution(n):
    result=''
    while n:
        result+=str(n%3)
        n=n//3
    return int(result,3)





n = 45
k =solution(n)
print(k)
# a, b = map(int, input().strip().split(' '))
# k = a



# 65~122