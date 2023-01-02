from statistics import mean
# mypy functions.py

# Example1 - Functions
def calculate(args):
    return mean(args)

scores = [7, 9, 10]
average = calculate(scores)

# Example2 - Functions with Docstring - help(max) show Docstring
def max(a, b):
    """ Docstring - This function calculate max between two values, both must be integer """
    if a > b:
        max_value = a
    else:
        max_value = b
    return max_value

# Example3 - Functions with types declared    
def min(a: int, b: int) -> int:
    """ Docstring - This function calculate min between two values, both must be integer """
    if a < b:
        min_value = a
    else:
        min_value = b
    return min_value

print(average)
print(max(2, 3))
print(min(7, 5))

# Example4 - Lambda functions

def converse_to_pesos(value: float) -> float:
    return value * 346

# Long
prices_in_dollar = [20, 15.5, 215]
prices_in_pesos = []

for price_in_dollar in prices_in_dollar:
    prices_in_pesos.append(float(price_in_dollar) * 346)

# Short Option 1
prices_in_pesos = list(map(
    converse_to_pesos, prices_in_dollar
))

# Short Option 2 - Example with map() and lambda function
prices_in_pesos = list(map(
    lambda dollar: float(dollar) * 346,
    prices_in_dollar
))

print(prices_in_pesos)
