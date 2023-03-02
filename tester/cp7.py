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
                    >>> np.allclose(cmpInverses(A1), np.linalg.inv(A1))
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
