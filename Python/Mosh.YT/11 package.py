#03:33:33 Package
# ecommerse -> name of package
# shipping -> name of module

# 3 ways to import
# 1. import package.module
import ecommerce.shipping 
ecommerce.shipping.calc_shipping() #very long code
ecommerce.shipping.calc_tax()

# 2. from package.module, import function(s)
from ecommerce.shipping import calc_shipping, calc_tax #shorter code
calc_shipping()
calc_tax()

# 3. from package, import the module
from ecommerce import shipping
shipping.calc_shipping()
shipping.calc_tax()


#03:37:00 Generating random number
import random
output = "("

#solution 1
for i in range(2):
    if(i % 2 == 1):
        output += ", "
    output += str(random.randint(1,6))

print(output + ")")

#solution 2
class Dice:
    val = (1,2,3,4,5,6)

    def roll(self):
        return random.choice(self.val)

game_dice = Dice()
print(f'({game_dice.roll()}, {game_dice.roll()})')



