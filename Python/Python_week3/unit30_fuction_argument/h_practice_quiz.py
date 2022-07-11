import math


def get_max_score(*args):
    max_score = 0
    for i in range(len(args)):
        if args[i] > max_score:
            max_score = args[i]
    return max_score

korean, english, mathematics, science = 100, 86, 81, 91

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)