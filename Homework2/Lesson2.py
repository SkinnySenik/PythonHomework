# 1.
"""
from random import randint

CoinLength = int(input("How many coins I will use: "))
count0 = 0
count1 = 0

for i in range(CoinLength):
   
    Coin = randint(0,1)
    print(Coin)
    if Coin == 0:
        count0 += 1
    elif Coin == 1:
        count1 += 1
if count1 < count0:
    count = count1
else:
    count = count0

print(f"you need to flip atleast -{count}- coins for them to face same side")
"""

# 2.
"""
x = int(input("type the the numeral X: "))
y = int(input("type the the numeral Y: "))

S = x + y
P = x * y

print(f"the sum for 2 numerals will be -{S}- while the product will be -{P}-")
"""

# 3.
"""
N = int(input("Type the numeral: "))

k = 0
while k < N:
    if k < N:
        if k * 2 > N:
            break
        elif k == 0:
            print(1)
            k += 1
        else:
            k = k * 2
            print(k)
"""