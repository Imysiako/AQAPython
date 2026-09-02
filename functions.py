
def average(numbers=list):

    avr = sum(numbers) / len(numbers)
    return avr

def kredit_payment(monthly_payment, months):
    """
    This function returns the whole final price of credit product.
    :param monthly_payment: amount of money that needs to be payd monthly some period of time
    :param months: amount of months for credit period
    :return: final price of product
    """
    total_amount = monthly_payment * months
    return total_amount

def sum_all(squre_1, squre_2):
    """
    This function returns sum of two objects.
    :param squre_1: first value in km2
    :param squre_2: second value in km2
    :return: sum of squares
    """
    result = squre_1 + squre_2

    return f"{result} км2"

def remainder(value_1, value_2):
    """
    This function return remainder of division of two numbers.
    :param value_1: Dividend
    :param value_2: Divisor
    :return:
    """
    rem = value_1 % value_2
    return rem

def multiplication_table(number):
    result = []
    multiplier = 1

    while multiplier <= 10:
        product = number * multiplier
        if product > 25:
            break
        result.append(product)
        multiplier += 1

    return result


def factorial(n: int):

    if n < 0:
        raise ValueError(f'You have to use 0 or positive numbers. You put {n}')

    if type(n) != int:
        raise TypeError(f'Only int allowed, you put {type(n)}')

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_anagram(word1: str, word2: str):
    """
    description
    """
    return sorted(word1.lower()) == sorted(word2.lower())


def filter_even_numbers(lst: list[int|float]):
    return [num for num in lst if num % 2 == 0]


def find_primes(n: int) -> list:

    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def triangle_area(a: int|float, b: int|float, c: int|float):
    # if a + b <= c or a + c <= b or b + c <= a:
    #     return 0
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


def convert_to_24_hour(time_str: str):

    if type(time_str) == list:
        raise TypeError

    if type(time_str) == dict:
        raise ValueError

    parts = time_str.split()
    if len(parts) != 2:
        raise ValueError('Time format is not a `hh:mm period`')
    time, period = parts
    hours, minutes = map(int, time.split(':'))
    if period.lower() == 'pm' and hours != 12:
        hours += 12
    elif period.lower() == 'am' and hours == 12:
        hours = 0
    return f'{hours:02}:{minutes:02}'