#pythran export float_sum(float [])


def float_sum(y):
    N = len(y)
    x = y[0]
    for i in xrange(1, N):
        x += y[i]
    return x
