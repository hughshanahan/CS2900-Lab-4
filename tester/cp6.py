test = {
    'name': 'checkpoint-6',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems cmpCondNums is undefined. Have you defined it correctly?
                    >>> 'cmpCondNums' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your cmpCondNums function isn't returning the correct type.
                    >>> # We're expecting a tuple!
                    >>> cond_nums = cmpCondNums(test_array)
                    >>> type(cond_nums).__name__ == 'tuple'
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your cmpCondNums function isn't returning all the values.
                    >>> # We are looking for 3 values; BOTH calculations and the difference between them.
                    >>> cond_nums = cmpCondNums(test_array)
                    >>> len(cond_nums) == 3
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your first calculation is incorrect.
                    >>> # This calculation should use the np.linalg.cond function.
                    >>> import math
                    >>> test_array = np.load('tester/res/cp6.npy')
                    >>> cond_nums = cmpCondNums(test_array)
                    >>> math.isclose(cond_nums[0], np.linalg.cond(test_array), rel_tol=1e+7, abs_tol=0)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your second calculation is incorrect.
                    >>> # Check that you're getting computing the min and max elements correctly.
                    >>> # You need to divide them to find the condition number.
                    >>> import math
                    >>> test_array = np.load('tester/res/cp6.npy')
                    >>> cond_nums = cmpCondNums(test_array)
                    >>> math.isclose(cond_nums[1], np.linalg.cond(test_array), rel_tol=1e+7, abs_tol=0)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # The absolute difference is incorrect. It should simply be zero.
                    >>> import math
                    >>> test_array = np.load('tester/res/cp6.npy')
                    >>> cond_nums = cmpCondNums(test_array)
                    >>> math.isclose(cond_nums[2], 0.0, rel_tol=1e-5, abs_tol=0)
                    True
                    """
                },
                
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
