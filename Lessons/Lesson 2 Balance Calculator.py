'''
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
numberOfMonths = 12

for i in range(1, numberOfMonths+1):
    balance = round((balance - (balance * monthlyPaymentRate)) * \
            (annualInterestRate/12 + 1), 2)
    print("Month " + str(i) + " Remaining balance: " + str(balance))
'''

'''
balance = 3926
originalBalance = balance
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
payment = 10
i = 0

while balance > 0:
    balance = (balance - payment) * (1+ monthlyInterestRate)
    i += 1
    
    if i == 12 and balance > 0:
        balance = originalBalance
        payment += 10
        i = 0
        
print("Lowest Payment: " + str(payment))
'''

annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
balance = 320000
originalBalance = balance
high = balance
low = 0
middle = (high + low) / 2
i = 0

while balance != 0 and i != 12:
    balance = round((balance - middle) * (1+ monthlyInterestRate),2)
    i += 1
    
    if i == 12 and balance > 0:
        balance = originalBalance
        low = middle
        middle = (high + low) / 2
        i = 0
    
    if i == 12 and balance < 0:
        balance = originalBalance
        high = middle
        middle = (high + low) / 2
        i = 0

print("Lowest Payment: " + str(round((middle),2)))