def countdown(n):
    n = n
    i = -1
    def down():
        nonlocal i, n
        i += 1
        return n - i
    return down

n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')