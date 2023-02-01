test = {
    'name': 'checkpoint-4',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems that runPageRank is undefined. Have you defined it correctly?
                    >>> 'runPageRank' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems that runPageRank is not returning a numpy vector. Have you defined it correctly?
                    >>> # Remember if the adjacency matrix is an NxN matrix then it should return an N-dim column vector.
                    >>> runDiffusion(np.array([[0,1],[1,0]]),1e-5,0.8).shape = (2,)
                    True
                    """
                },                
                {
                    'code': r"""
                    >>> # Your version of runPageRank isn't giving the correct output.
                    >>> # Please have another look at the algorithm. 
                    >>> finalAnswercp4 = np.array([0.31795041, 0.29431393, 0.1577554,  0.1478989,  0.08208136] )
                    >>> np.allclose(finalAnswercp4,runPageRank(np.array([[0,1,0,0,0], [1,0,1,0,0], [1,0,0,1,1], [1,0,0,0,0], [0,0,0,1,0]],0.01),atol=10**-2, rtol=0) 
                    True
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
