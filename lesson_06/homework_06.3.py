lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst_2 =[]
for k in lst1:
    if type(k) is str:
        lst_2.append(k)
print(lst_2)