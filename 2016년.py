import random
import re
from collections import Counter
from itertools import combinations
from itertools import permutations



def solution(a,b):
    if a == 1 or a == 3 or a ==5 or a ==7 or a ==8 or a ==10 or a ==12:
        if a ==8 or a ==10 or a ==12:
            b = (b + (a - 1) * 31) - ((int(a / 2)-1))
        else:
            b = (b+(a-1)*31)-(int(a/2))
        if a > 2:
            b -= 1
    elif a == 2 or a ==4 or a ==6 or a ==9 or a ==11:
        if a ==9 or a ==11:
            b = (b + (a - 1) * 31) - ((int(a / 2)-1))
        else:
            b = b + ((a - 1) * 30) + (int(a / 2))
        if a > 2:
            b -= 1
    Yoil = ['FRI','SAT','SUN','MON','TUE','WED','THU']



    return Yoil[(b%7)-1]



a = 8
b = 31
r = solution(a ,b)
print(r)

