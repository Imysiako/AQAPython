# Task 1

def even_numbers(n):
    num = 0
    while num <= n:
        yield num
        num += 2

for item in even_numbers(10):
    print(item)

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibb = fibonacci_generator()
for g in range(20):
    print(next(fibb))

# Task 2

class IterNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        data = self.current
        self.current += 2
        return data

n = 22
e_iter = IterNumbers(n)

for n in e_iter:
    print(n)

class IterNumbers_1:
    def __init__(self, my_list):
        self.my_list = my_list
        self.index = len(my_list) - 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        data = self.my_list[self.index]
        self.index -= 1
        return data


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e_iter = IterNumbers_1(my_list)

for n in e_iter:
    print(n)
#
# Task 3

def my_decorator(func):
    def wrapper(*args, **kwargs):

        print(f"Here is the input argument: {args[0] if args else kwargs}")
        result = func(*args, **kwargs)
        print(f"Here is the result: {result}")
        return result

    return wrapper


@my_decorator
def reverse_word(word):
    revers = ""
    for k in word:
        revers = k + revers
    return revers

reverse_word("plant")

def exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] Execution of '{func.__name__}' raise error:  {type(e).__name__} - {e}")
            return None

    return wrapper


@exceptions
def incorrect(word):
    revers = ""
    for k in word:
        revers = k + revers
    return revers

result_err = incorrect(12345)
print(result_err)