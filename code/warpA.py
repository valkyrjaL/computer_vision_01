import numpy as np

def warp(im, A, output_shape):
    """ Warps (h,w) image im using affine (3,3) matrix A
    producing (output_shape[0], output_shape[1]) output image
    with warped = A*input, where warped spans 1...output_size.
    Uses nearest neighbor interpolation."""
    invA = np.linalg.inv(A)
    warped = np.zeros(output_shape)
    for i in range(output_shape[0]):
        for j in range(output_shape[1]):
            ps = np.rint(np.dot(invA, [i, j, 1])).astype(int)
            if ps[0] >= 0 and ps[0] < output_shape[0] and ps[1] >=0 and ps[1] < output_shape[1]:
                warped[i][j] = im[ps[0]][ps[1]]
    return warped
