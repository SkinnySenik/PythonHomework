# 1.
"""
n = map(int,input("amount of numerals in the first pack: "))
m = map(int,input("amount of numerals in the second pack: "))

a = map(int, input("type in numerals in the first pack: ").split())
a1 = set(a)
b = map(int, input("type in numerals in the second pack: ").split())
b1 = set(b)

print(*sorted(a1 & b1))
"""
# 2.
"""
n = int(input("how many there are bushes: "))
a = list(map(int, input("how many berries have grown on each bush: ").split()))

sum = 0
i = 1

for i in range(1, n-1):
    if (a[i]+a[i+1]+a[i-1] > sum):
        sum = a[i]+a[i+1]+a[i-1]

print(sum)
"""