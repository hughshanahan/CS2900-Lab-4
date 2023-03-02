test = {
    'name': 'checkpoint-8',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems doSVDFit is undefined. Have you defined it correctly?
                    >>> 'doSVDFit' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your doSVDFit function isn't returning the correct type.
                    >>> # We're expecting a tuple, not a NumPy array!
                    >>> p = doSVDFit(np.array([0, 1, 2, 3]), np.array([-1, 0.2, 0.9, 2.1]))
                    >>> type(p).__name__ == 'tuple'
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your doSVDFit function isn't returning the correct result.
                    >>> # Refer to the formula given and ensure you're calculating m and c
                    >>> # using the np.linalg.pinv function.
                    >>> x, y = np.load('tester/res/cp8_x.npy'), np.load('tester/res/cp8_y.npy')
                    >>> import math
                    >>> pr = doSVDFit(x, y) 
                    >>> math.isclose(pr[0],1.0) and math.isclose(pr[1],-0.95)
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
