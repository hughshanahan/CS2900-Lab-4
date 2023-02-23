test = {
    'name': 'checkpoint-2',
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
                    >>> # It seems that D1Thand is undefined. Have you defined it correctly?
                    >>> 'D1Thand' in dir()
                    True
                    """
                },                
                {
                    'code': r"""
                    >>> # It seems the dimensons of D1Thand are incorrect.
                    >>> # Are you checking if the dimensions of D1Thand are those of A1? 
                    >>> D1Thand.shape == (5,5) 
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # The transpose of the diffusion matrix of A1 computed using compDiffusion does not match with D1Thand. 
                    >>> # Have you checked your calculation of D1hand?
                    >>> np.allclose(compDiffusion(A1),D1Thand,rtol=0.01) 
                    True
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
