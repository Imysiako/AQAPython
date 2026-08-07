# task 1
# """ Задача - надрукувати табличку множення на задане число, але
# лише до максимального значення для добутку - 25.
# Код майже готовий, треба знайти помилки та випраавити\доповнити.
#
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier

        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f'{number} x {multiplier} = {result}')

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(6)

#Task 2
def sum_two(number_1, number_2):
    sum_ = number_1 + number_2
    print(f'{number_1} + {number_2} = {sum_}')

sum_two(2,56)

def average(numbers):

    avr = sum(numbers) / len(numbers)
    print(avr)

average([1,3,2,1])

# # task 4
# """  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.

def incorrect(word):
    revers = ""
    for k in word:
        revers = k + revers
    return revers

print(incorrect("plant"))

# task 5
# """  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.

def longest(listed):
    return max(listed, key=len)

longest(['mary', 's', 'mnbhfjryyatgh'])
print(f"The longest word is: {longest(['mary', 's', 'mnbhfjryyatgh'])}")

# task 6
# """  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
# у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
# не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)
str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

# task 7
def kredit_payment(monthly_payment, months):
    """
    This function returns the whole final price of credit product.
    :param monthly_payment: amount of money that needs to be payd monthly some period of time
    :param months: amount of months for credit period
    :return: final price of product
    """
    total_amount = monthly_payment * months
    return total_amount

print(kredit_payment(1230, 12))


# task 8

# # """
# # Площа Чорного моря становить 436 402 км2, а площа Азовського
# # моря становить 37 800 км2. Яку площу займають Чорне та Азов-
# # ське моря разом?
# """
def sum_all(squre_1, squre_2):
    """
    This function returns sum of two objects.
    :param squre_1: first value in km2
    :param squre_2: second value in km2
    :return: sum of squares
    """
    result = squre_1 + squre_2

    return f"{result} км2"

print(sum_all(456, 567))


# task 9
def word_with_h(some_data):
    """
    This function is checking if your word contains letter 'h'.
    :param some_data: some word
    :return: check if this word has letter 'h'
    """
    if "h" not in some_data.lower():
        return f"Your word is {some_data}. Please type word with letter 'h'."
    else:
        return f"Thank you! Your word is '{some_data}'. That's correct"

print(word_with_h("Check my mail"))

# task 10

def remainder(value_1, value_2):
    """
    This function return remainder of division of two numbers.
    :param value_1: Dividend
    :param value_2: Divisor
    :return:
    """
    rem = value_1 % value_2
    return rem
print(remainder(45,13))