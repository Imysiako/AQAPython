some_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sum_d = []
for k in some_list:
    if k %2 ==0:
        sum_d.append(k)
print(sum_d)
print(sum(sum_d))