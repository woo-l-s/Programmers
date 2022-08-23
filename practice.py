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


# def solution(ingredient):
# try:
#     cnt = 0
#     for k in range(0, len(ingredient)):
#         for i in range(0, len(ingredient)):
#             if ingredient[i] == 1:
#                 if ingredient[i+1] == 2:
#                     if ingredient[i+2] == 3:
#                         if ingredient[i+3] == 1:
#                             cnt+=1
#                             del ingredient[i:i+3:1]
#                             break
#     return cnt
# except:
#     return cnt
# list = []
# str = ''
# for i in ingredient:
#     if i == 1:
#         str = str + 'a'
#     elif i == 2:
#         str = str + 'b'
#     else:
#         str = str + 'c'
# # print(str)
# cnt = 0
# print(str.find('abcsassasda'))
# while(1):
#
#     if str.find('abca') == -1:
#         return cnt
#     if str.count('abca') > 1:
#         str = str.replace("abca", "", 1)
#     str = str.replace("abca", "",1)
#     cnt += 1
#     # str = str.lstrip("abca")
#     # print(str)

# 두 큐의 합 같게 만들기
# def solution(queue1, queue2):
#     cnt = 0
#
#     total_sum = float((sum(queue1) + sum(queue2)) / 2)
#     while (sum(queue1) != total_sum):
#         if (cnt > 1000):
#             return -1
#         cnt += 1
#         if (sum(queue1) > sum(queue2)):
#             n = queue1.pop(0)
#             queue2.append(n)
#             print(queue2)
#         else:
#             n = queue2.pop(0)
#             queue1.append(n)
#             print(queue1)
#     return cnt
#
#
# queue1 = [1, 2, 2]
# queue2 = [2, 1]
def solution(s):
    stack = []
    for i in s:
        if i == '(':  # '('는 stack에 추가
            stack.append(i)
        else:  # i == ')'인 경우
            if stack == []:  # 괄호 짝이 ')'로 시작하면 False 반환
                return False
            else:
                stack.pop()  # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거

    return stack == []


s = "(())()"
k = solution(s)
print(k)

# 65~122
