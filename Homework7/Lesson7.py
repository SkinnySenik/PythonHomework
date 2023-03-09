# 1.
"""
line = "пара-ра-рам рам-пам-папам па-ра-па-да"
lines = line.split()
 
print(lines)
 
lst = [sum(x in 'уеыаоэяию' for x in lin)
 for lin in lines]
 
if len(set(lst)) == 1 :
    res = "Парам пам-пам"  
else: res = "Пам парам"
 
print(res)
"""
# 2.
"""
def print_operation_table(operation, num_rows = 6, num_columns = 6):

    for i in range(1, num_columns + 1):
        table = []
        for j in range(1, num_rows + 1):
            table.append(str(operation(i, j)))
        print("".join(f'{e:<4}' for e in table))

        

print_operation_table(lambda x, y: x*y)
"""
