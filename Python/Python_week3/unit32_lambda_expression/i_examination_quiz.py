files = input().split()

print(list(map(lambda x : '{0:0>8}'.format(x) if len(x.split('.')[1]) == 4 else '{0:0>7}'.format(x), files)))