import math 

dailyRate = 8 
monthBillableDays = 22

def dayRate(hourRate:int):
    return 8*hourRate

def monthRate(hourRate:int, discount: float):
    total = 22*dayRate(hourRate=hourRate)
    return int(math.ceil(total - (discount * total)))

def noWorkdays(budget:int, hourRate: int, discount: float):
    hourrate = dayRate(hourRate) - (dayRate(hourRate)*discount)

    return int(budget/hourrate)

print(dayRate(89))
print(monthRate(89,0.42))
print(noWorkdays(20000, 89, 0.2002))