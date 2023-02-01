test = {
    'name': 'checkpoint-3',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems that runDiffusion is undefined. Have you defined it correctly?
                    >>> 'runDiffusion' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems that runDiffusion is not returning a numpy vector. Have you defined it correctly?
                    >>> # Remember if the adjacency matrix is an NxN matrix then it should return an N-dim column vector.
                    >>> runDiffusion(np.array([[0,1],[1,0]]),1e-5).shape = (2,)
                    True
                    """
                },                
                {
                    'code': r"""
                    >>> # Your version of runDiffusion isn't giving the correct output.
                    >>> # Please have another look at the algorithm. 
                    >>> finalAnswercp3 = np.array([0.33217593, 0.33287037, 0.16689815, 0.11064815, 0.05740741])
                    >>> np.allclose(finalAnswercp3,runDiffusion(np.array([[0,1,0,0,0], [1,0,1,0,0], [1,0,0,1,1], [1,0,0,0,0], [0,0,0,1,0]],0.01),atol=10**-2, rtol=0) 
                    True
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
