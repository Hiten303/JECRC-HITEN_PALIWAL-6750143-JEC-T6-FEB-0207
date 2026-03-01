salary = int(input('Enter your salary: '))
cibil_score = int(input('Enter your score: '))

if salary > 25000 and cibil_score > 700:
   if salary > 50000 and cibil_score > 750:
        print('Instant approved')
   else:
        print('wait approved')
else:
    print('rejected')