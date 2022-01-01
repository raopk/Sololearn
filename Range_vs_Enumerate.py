"""RANGE VS. ENUMERATE"""
def fizz_buzz(numbers):
    ''''
    Given a list of integers:
    1. Replace all integers that are evenly divisible by 3
    with "fizz"
    2. Replace all integers divisible by 5 with "buzz"
    3. Replace all integers divisible by both 3 and 5 with 
    "fizzbuzz" 
    >>> numbers = [45,22,14,65,97,72]
    >>> fizz_buzz(numbers)
    >>> numbers
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    '''
    for i in range (len(numbers)):
        num = numbers[i]
        if num % 3 == 0:
            numbers[i] = 'fizz'
        if num % 3 == 0:
            numbers[i] = 'buzz'
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = 'fizzbuzz'

#pseudo_code 
# for i in range (len(numbers)):
#  num = numbers[i] 
# if num % 3 == 0 number[i] =  'fizz'
# if i % 5 == 0 number[i] = 'buzz'
# if i % 3 == 0 and i % 5 == 0  number[i] = 'fizzbuzz'  



def add(a: int, b: int) -> int:
    """A function that sums two integers
        Args:
            a (int): The first number
            b (int): The second number

        Returns:
            int: The sum
    """
    return a + b