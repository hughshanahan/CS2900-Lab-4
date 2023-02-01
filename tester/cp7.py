test = {
    'name': 'checkpoint-7',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems cmpInverses is undefined. Have you defined it correctly?
                    >>> 'cmpInverses' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your cmpInverses function isn't returning the correct result.
                    >>> # The value you have computed manually doesn't match the actual inverse.
                    >>> # Check that you're computing this correctly. 
                    >>> # You should use np.matmul to multiply the matrices.
                    >>> cmpInverses(np.load('tester/res/cp7.npy')) == np.linalg.inv(test)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # I can't find your sqDiffMatrices function from lab 2.
                    >>> # Have you copied it across?
                    >>> # Make sure you keep the function name the same!
                    >>> 'sqDiffMatrices' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems cmpInverses is undefined. Have you defined it correctly?
                    >>> 'sqDiff' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm...your sqDiff is incorrect.
                    >>> # Have you hard-coded something you shouldn't have?
                    >>> import math
                    >>> math.isclose(sqDiff, 999410.2525124999, rel_tol=1e-5, abs_tol=0)
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
