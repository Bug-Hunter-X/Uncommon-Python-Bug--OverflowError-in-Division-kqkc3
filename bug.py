def function_with_uncommon_error(x, y):
    if x == 0:
        return 0  # Correct handling for x == 0
    elif y == 0:
        return float('inf') #This line may result in an OverflowError if calculations lead to extremely large values
    else:
        result = x / y
        return result

#Example that may cause an OverflowError
result = function_with_uncommon_error(1,0)
print(result) #Output: inf

result = function_with_uncommon_error(float('inf'),1)
print(result) #Output: inf

result = function_with_uncommon_error(float('inf'), float('inf'))
print(result) #Output: nan

#Example where it may not cause an OverflowError
result = function_with_uncommon_error(10,2)
print(result) #Output: 5.0