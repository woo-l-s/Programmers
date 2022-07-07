def solution(id_list, report, k):
    answer = []
    singoja = []
    singodang = []
    dictionary1 = {string: 0 for string in id_list}
    dictionary2 = {string: 0 for string in id_list}

    for s in report:
        a,b = s.split(' ')
        if b in dictionary1:
            dictionary1[b] += 1
        else:
            continue
    #print(dictionary)
    for s in report:
        a,b = s.split(' ')
        if dictionary1[b] >= k:
            dictionary2[a] += 1
        else:
            continue
    #print(dictionary2)

    answer = list(dictionary2.values())

    return answer


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
result = solution(id_list, report, k)

print(result)