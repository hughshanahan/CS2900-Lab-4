test = {
    'name': 'checkpoint-1',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems compDiffusion is undefined. Have you defined it correctly?
                    >>> 'compDiffusion' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems compDiffusion doesn't check if the matrix passed to it is an adjacency matrix.
                    >>> # Are you checking if the matrix is a square matrix with integer entries? 
                    >>> # Does compDiffusion return -1 if it is not the case?
                    >>> compDiffusion(np.array([[1,2,3],[3,2,1]])) == -1 and compDiffusion(np.array([[1,2.0],[3.0,2]])) == -1 
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # compDiffusion is not returning the right type of matrix.
                    >>> # Does it return a matrix with the same dimensions as the inputted matrix?
                    >>> compDiffusion(np.array([[0,1,1],[1,0,0],[1,0,0]])).shape == (3,3)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # compDiffusion is not returning a matrix with floating point numbers.
                    >>> compDiffusion(np.array([[0,1,1],[1,0,0],[1,0,0]])).dtype == 'float64'
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # compDiffusion does not compute the correct diffusion matrix. 
                    >>> # For example the adjacency matrix 
                    >>> # (0,1,1)
                    >>> # (1,0,0)
                    >>> # (1,0,0)
                    >>> # should return 
                    >>> # (0.0, 1.0, 1.0)       
                    >>> # (0.5, 0.0, 0.0)    
                    >>> # (0.5, 0.0, 0.0)       
                    >>> # please check your function again
                    >>> np.allclose(compDiffusion(np.array([[0,1,1],[1,0,0],[1,0,0]])), np.transpose(np.array([[0,0.5,0.5],[1.0,0,0],[1.0,0,0]])), atol=10**-2, rtol=0)
                    True
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
