def carpet(N, C):
    def check(n, x, y):
        if n <= 1:
            return True
        n2 = n // 3
        if n2 <= x < n2 * 2 and n2 <= y < n2 * 2:
            return False
        return check(n2, x % n2, y % n2)

    for y in range(N):
        for x in range(N):
            if check(N, x, y):
                print(C, end='')
            else:
                print('' * len(C), end='')
        print('')

N = int(input())
C = input()
carpet(N, C)