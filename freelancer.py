import math

def dayRate(roh,discount=0.0):
    return roh*8*(1-discount)


def monthRate(roh,discount):
    return math.ceil(dayRate(roh,discount)*22)

    
def daysInBudget(budget,roh,discount):
    dayrate=dayRate(roh,discount)
    return math.floor(budget/dayrate)

print(dayRate(89))
print(monthRate(89,0.42))
print(daysInBudget(20000,89,0.2002))