import re


def solution(new_id):
    # answer = new_id
    answer = new_id.lower()
    answer = re.sub(r'[^a-z0-9-_. ]','',answer).strip()
    answer = re.sub('(([.])\\2{1,})','.',answer)
    answer = answer.strip(".")
    answer = answer.replace(' ','a')
    # 아랫것은 왜 안됐지?
    # answer.strip("a")
    answer = answer[0:15]
    answer = answer.strip(".")
    if answer == '':
        answer = 'a'
    while(1):
        if len(answer) <= 2:
            answer += answer[-1]
        else:
            break
    # print(answer[-1])


    return answer


new_id = "=.="


result = solution(new_id)

print(result)