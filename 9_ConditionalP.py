# fake data on how much stuff people purchase given their age range.
# 100,000 random people randomly in 20's, 30's, 40's, 50's, 60's, and 70's.

from numpy import random
random.seed(0)

# "totals" contains the total number of people in each age group.
totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
# "purchases" is the number of things purchased by people in each age group.
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0

# use '_' as the iterator as we do not need it in loop body
for _ in range(100000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    # elders have a higher probability to buy things
    # toggle following two lines to change probability
    purchaseProbability = float(ageDecade) / 100.0
    # purchaseProbability = 30.0 / 100.0
    totals[ageDecade] += 1
    if (random.random() < purchaseProbability):
        totalPurchases += 1
        purchases[ageDecade] += 1
        
print(totals)
print(purchases)
print(totalPurchases)

# the probability of people in 30s bought something
PEF = float(purchases[30]) / float(totals[30])
print('P(purchases|30s):',str(PEF))
# 0.29929598652145134

# the probability of people in 30s
PF = float(totals[30] / 100000.0)
print('P(30s):',str(PF))
# 0.16619

# the overall probability of buying things
PE = float(totalPurchases / 100000)
print('P(Purchases):',str(PE))
# 0.45012

# if F and E were independent, P(E|F) should be close to P(E)
# while P(E|F) is 0.30 and P(E) is 0.45, which means they are dependent

# P(E)P(F)
print('P(30s)P(Purchase):', str(PE*PF))
# 0.07480544280000001

# notice P(E,F) is not close to P(E)P(F) which means E and F are dependent
print('P(30s,Purchase):', str(float(purchases[30])/100000.0))
# 0.04974

# check if P(E|F) = P(E,F)/P(F)
print((purchases[30]/100000.0)/PF)
# 0.29929598652145134