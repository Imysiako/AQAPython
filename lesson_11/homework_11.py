new_q = ['1,2,3,4', '1,2,3,4,50','"qwerty1",2,3']

def sum_elements(lst):
    for item in lst:
        try:
            number = [int(n) for n in item.split(',')]
            print(sum(number))
        except ValueError:
            print('I can\'t do that')


sum_elements(new_q)
