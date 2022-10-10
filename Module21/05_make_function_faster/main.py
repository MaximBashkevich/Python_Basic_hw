def calculating_math_func(data, factorial={1: 1}):
    if data in factorial:
        result = factorial[data]
    else:
        result = max(factorial.values())
    for index in range(max(factorial.keys()) + 1, data + 1):
        result *= index
        factorial[index] = result
    result /= data ** 3
    result = result ** 10
    return result



calculating_math_func(5)
calculating_math_func(10)
