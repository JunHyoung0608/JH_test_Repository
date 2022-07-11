def get_min_max_score(*args):
    max_score = 0
    min_score = 100
    for i in range(len(args)):
        if args[i] > max_score:
            max_score = args[i]
    for i in range(len(args)):
        if args[i] < min_score:
            min_score = args[i]
    return min_score, max_score

def get_average(korean, english, mathematics, science):
    average_score = (korean + english + mathematics + science)/4
    return average_score 

korean, english, mathematics, science = map(int, input().split())

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))