#!/usr/bin/python3


def magic_calculation(a, b):
	 """Perform a magic calculation based on two input values.

    This function calculates a magic value by raising the first input value
    (a) to the power of the second input value (b), and then dividing by the
    range of integers from 1 to 3. If the value of i in the loop is greater
    than a, a ValueError is raised and the magic value is calculated by
    adding the values of a and b together.

    Args:
        a: A numeric input value.
        b: A numeric input value.

    Returns:
        The magic value calculated by the function.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Value of i is too large')
            else:
                result += (a ** b) / i
        except ValueError:
            result = b + a
            break
    return result
