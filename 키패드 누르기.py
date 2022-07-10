import re


def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    pad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]
    }
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer+= 'L'
            left = i
        elif i == 3 or i == 6 or i == 9:
            answer+= 'R'
            right = i
        elif i==0 or i == 2 or i == 5 or i == 8:
            lx_axis = abs(pad[i][0] - pad[left][0])
            ly_axis = abs(pad[i][1] - pad[left][1])
            rx_axis = abs(pad[i][0] - pad[right][0])
            ry_axis = abs(pad[i][1] - pad[right][1])
            #거리가 아닌 칸 수이다~!
            # lx_axis = pad[i][0] - pad[left][0]**2
            # ly_axis = (pad[i][1] - pad[left][1])**2
            # rx_axis = (pad[i][0] - pad[right][0]) ** 2
            # ry_axis = (pad[i][1] - pad[right][1]) ** 2
            left_distance = lx_axis + ly_axis
            right_distance = rx_axis + ry_axis

            if (left_distance < right_distance):
                answer += 'L'
                left = i
            elif left_distance == right_distance:
                if hand == "left":
                    answer += "L"
                    left = i
                else:
                    answer += "R"
                    right = i
            else:
                answer += "R"
                right = i



    # # print(pad[3][0])
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

result = solution(numbers, hand)
print(result)
