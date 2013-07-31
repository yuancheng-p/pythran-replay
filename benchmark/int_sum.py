#pythran export int_sum(int [])


def int_sum(y):
    N = len(y)
    x = y[0]
    for i in xrange(1, N):
        x += y[i]
    return x
