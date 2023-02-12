# 1.
"""
a = int(input("type the first numeral: "))
b = int(input("type the second numeral: "))
c = int(input("type the third numeral: "))

print(f"{a} + {b} + {c} = {a + b + c}")
"""
# 2.
"""
a = int(input("how many cranes has Peta made: "))
b = int(a)
c = int((a + b) * 2)

print(f"{a} + {c} + {b} = {a + b + c}")
"""

# 3.
"""
a = input("type the 6 digit numeral: ")

s11 = int(a[0])
s12 = int(a[1])
s13 = int(a[2])
s1 = s11 + s12 + s13
s21 = int(a[3])
s22 = int(a[4])
s23 = int(a[5])
s2 = s21 + s22 + s23


if s1 == s2:
    print("this number is lucky")
else:
    print("this number is not lucky")
"""

# 4.
"""
n = int(input("type the n of the chocolate: "))
m = int(input("type the m of the chocolate: "))
k = int(input("type how many pieces you want to break: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print(f"you can break chocolate into {k} rectangle pieces")
else:
    print(f"you cant break chocolate into {k} rectangle pieces")
"""