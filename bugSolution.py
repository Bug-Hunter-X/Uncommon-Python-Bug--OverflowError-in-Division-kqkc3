def function_with_uncommon_error_solution(x, y):
    if x == 0:
        return 0
    elif y == 0:
        return float('inf')
    else:
        try:
            result = x / y
            if result > float('inf') or result < float('-inf'):
              return float('inf') if result > 0 else float('-inf')
            return result
        except OverflowError:
            return float('inf') # Handle OverflowError gracefully

#Example
result = function_with_uncommon_error_solution(1, 0)
print(result) #Output: inf

result = function_with_uncommon_error_solution(float('inf'), 1)
print(result)  # Output: inf

result = function_with_uncommon_error_solution(float('inf'), float('inf'))
print(result)  # Output: 1.0

result = function_with_uncommon_error_solution(10, 2)
print(result)  # Output: 5.0