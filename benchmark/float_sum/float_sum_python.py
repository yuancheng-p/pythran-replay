#pythran export float_sum_python(float [])


def float_sum_python(y):
    N = len(y)
    x = y[0]
    for i in xrange(1, N):
        x += y[i]
    return x
