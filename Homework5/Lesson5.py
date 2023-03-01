# 1.
"""
A = int(input("Type the number: "))
B = int(input("Type its power: "))

def power(A, B):
    if B == 1:
        return A
    elif B == 0:
        A = 1
        return A
    else:
        return A**B
print(f"The powered number will be {power(A, B)}")
"""
# 2.
"""
a = int(input("Type the numeral a: "))
b = int(input("Type the numeral b: "))

def sum(a, b):
    if a < 0 or b < 0:
        print("ERROR")
    else:
        if a == 0:
            return b
        return sum(a-1, b+1)

print(f"The summed number will be {sum(a,b)}")
"""