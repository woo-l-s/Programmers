# 람다함수의 예시
# (lambda x,y: x + y)(10, 20)
from xlwt.compat import long


def solution(arr1, arr2):
    list = []
    for i in range(1, len(arr1) + 1):
        list1 = []
        for j in range(1, len(arr1[i-1])+1):

            # print(arr1[i-1][j-1] + arr2[i-1][j-1])
            list1.append(arr1[i-1][j-1] + arr2[i-1][j-1])
        list.append(list1)
            # list[i-1].append(arr1[i-1][j-1] + arr2[i-1][j-1])
    print(list)

    return 0







arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
k = solution(arr1, arr2)
print(k)

# 65~122