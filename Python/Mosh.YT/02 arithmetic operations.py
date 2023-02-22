#49:29 arithmetic operations
print(10 / 3) # prints floating point
print(10 // 3) # prints integer
print(10 % 3) # prints integer
print(10 ** 3) # 10^3

#round
print("round(): ")
print(round(2.9))
print(round(2.1))
print(round(2.5))

#absolute value
print("abs(): ")
print(abs(-123))
print(abs(123))

import math
print('using import math module')
print(math.pi)
print(math.e)
print(math.sqrt(25))
print(math.ceil(4.3))
print(math.floor(4.3))

#if statements
is_hot_day = True

if is_hot_day:
    print("It's a hot day!")
    print("Drink plenty of water")
elif not is_hot_day:
    print("It's a cold day!")
    print("Wear warm clothes")
else:
    print("It's a wonderful day!")

has_good_credit = False
price = 1000000

if has_good_credit:
    downpay = .10 * price
else:
    downpay = .20 * price

print(f"Downpay: ${downpay}...")    



