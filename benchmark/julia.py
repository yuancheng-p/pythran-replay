#pythran export julia(float, float, int, float, float, float)
# Authors: Kurt W. Smith, Serge Guelton
# License: MIT

import numpy as np


def kernel(zr, zi, cr, ci, lim, cutoff):
    ''' Computes the number of iterations `n` such that
        |z_n| > `lim`, where `z_n = z_{n-1}**2 + c`.
    '''
    count = 0
    while ((zr*zr + zi*zi) < (lim*lim)) and count < cutoff:
        zr, zi = zr * zr - zi * zi + cr, 2 * zr * zi + ci
        count += 1
    return count

def julia(cr, ci, N, bound, lim, cutoff):
    ''' Pure Python calculation of the Julia set for a given `c`.  No NumPy
        array operations are used.
    '''
    julia = np.empty((N, N), np.uint32)
    grid_x = np.linspace(-bound, bound, N)
    "omp parallel for private(i, x, j, y)"
    for i, x in enumerate(grid_x):
        for j, y in enumerate(grid_x):
            julia[i,j] = kernel(x, y, cr, ci, lim, cutoff)
    return julia
