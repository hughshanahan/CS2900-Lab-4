test = {
    'name': 'checkpoint-1',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems that A1 is undefined. Have you defined it correctly?
                    >>> 'A1' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems that D1hand is undefined. Have you defined it correctly?
                    >>> 'D1hand' in dir()
                    True
                    """
                },                
                {
                    'code': r"""
                    >>> # It seems the dimensons of D1hand are incorrect.
                    >>> # Are you checking if the dimensions of D1hand are those of A1? 
                    >>> D1hand.shape == (5,5) 
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # The diffusion matrix of A1 computed using compDiffusion does not match with D1hand. 
                    >>> # Have you checked your calculation of D1hand?
                    >>> np.allclose(compDiffusion(A1),D1hand,rtol=0.01) 
                    True
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
