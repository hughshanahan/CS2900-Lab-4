"""
Utility functions for CS2900 Lab 4 checkpoint test suite.

Author: Tom Kuipers
"""
import numpy as np

def check_code(regex):
    import inspect
    import re
    local_vars = str(inspect.currentframe().f_back.f_back.f_locals)
    no_match = len(re.findall(regex, local_vars)) == 0
    return no_match

