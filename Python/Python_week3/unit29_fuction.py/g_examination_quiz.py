def all_calculation(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    return add, sub, mul, div

x, y = map(int, input().split())
a, s, m, d = all_calculation(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곰셈: {2}, 나눗셈: {3}'.format(a, s, m ,d))