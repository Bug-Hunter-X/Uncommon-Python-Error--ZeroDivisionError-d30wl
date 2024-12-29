def function_with_uncommon_error(x):
    if x == 0:
        return float('inf') #Return positive infinity
    else:
        return 10 / x

result = function_with_uncommon_error(0)
print(result) # Output: inf 

#Another way
def function_with_uncommon_error(x):
    try:
        return 10 / x
    except ZeroDivisionError:
        return float('inf')

result = function_with_uncommon_error(0)
print(result) # Output: inf