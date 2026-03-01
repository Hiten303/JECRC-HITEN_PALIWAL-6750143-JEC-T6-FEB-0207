units = int(input('Enter Unit: '))
bill_amount = None

if units > 0:
    if units <= 100:
        bill_amount = units*5
    elif 101 <= units <= 300:
        bill_amount = units * 7
    else:
        bill_amount = units * 10
    
    if bill_amount > 5000:
        bill_amount = bill_amount*0.95

    print(f'Bill amount after discount: {bill_amount}')

else:
    print('Enter valid units!')














