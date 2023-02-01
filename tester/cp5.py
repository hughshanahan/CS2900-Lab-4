test = {
    'name': 'checkpoint-5',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems checkDims is undefined. Have you defined it correctly?
                    >>> 'checkDims' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems A_svd is undefined. Have you defined it correctly?
                    >>> 'A_svd' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your matrix A_svd[0] is not correct. Double check your values.
                    >>> np.allclose(A_svd[0], np.load('tester/res/A_svd0.npy'), atol=10**-1, rtol=0)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your matrix A_svd[1] is not correct. Double check your values.
                    >>> np.allclose(A_svd[1], np.load('tester/res/A_svd1.npy'), atol=10**-1, rtol=0)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your matrix A_svd[2] is not correct. Double check your values.
                    >>> np.allclose(A_svd[2], np.load('tester/res/A_svd2.npy'), atol=10**-1, rtol=0)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your matrix A_svd[3] is not correct. Double check your values.
                    >>> np.allclose(A_svd[3], np.load('tester/res/A_svd3.npy'), atol=10**-1, rtol=0)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your checkDims doesn't give the correct output for A_svd[0].
                    >>> # Have you handled your dimensions, specifically D, correctly?
                    >>> checkDims(A_svd[0]) == (2, 2, 2, 3, 3, 3)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your checkDims doesn't give the correct output for A_svd[1].
                    >>> # Have you handled your dimensions, specifically D, correctly?
                    >>> checkDims(A_svd[1]) == (2, 2, 2, 4, 4, 4)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your checkDims doesn't give the correct output for A_svd[2].
                    >>> # Have you handled your dimensions, specifically D, correctly?
                    >>> checkDims(A_svd[2]) == (3, 3, 3, 2, 2 ,2)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your checkDims doesn't give the correct output for A_svd[3].
                    >>> # Have you handled your dimensions, specifically D, correctly?
                    >>> checkDims(A_svd[3]) == (4, 4, 4, 2, 2, 2)
                    True
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
