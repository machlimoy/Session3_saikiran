import math

def dayRate(hourRate,discount=0.0):
    return 8 * hourRate * (1-discount)


def monthRate(hourRate,discount):
    return math.ceil(dayRate(hourRate,discount)*22)


def dayInBudget(budget,hourRate,discount):
    dayrate = dayRate(hourRate,discount)
    return math.floor(budget/dayrate)

print(dayRate(89))
print(monthRate(89,0.42))
print(dayInBudget(20000,89,0.2002))