def solution(lottos, win_nums):
    answer = []
    win_l= (set(lottos) & set(win_nums))
    # print(len(win_l))
    # print(lottos.count(0))
    if (len(win_l) == 0) and (lottos.count(0) != 6):
        lottos.append(0)
    answer.append((7-(len(win_l) + lottos.count(0))))
    if len(win_l) != 0:
        pass
    else:
        win_l.add(0)
    answer.append((7 - (len(win_l))))
    # print(answer)

    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

result = solution(lottos, win_nums)

print(result)