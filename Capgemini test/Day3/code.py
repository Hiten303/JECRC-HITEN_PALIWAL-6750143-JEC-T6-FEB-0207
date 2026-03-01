'''
It is a type of statement which controls the flow of the execution of a program.
'''
## conditional Statements : based upon one condition, the flow of the execution of a program will be decided.

'''
1. if statement (simple if),
2. if else statement
3. elif statement
4. nested if statement
'''

## WAP to check whether the username or password is correct or not. if correct print login successfully completed. if not , do nothing

user = {
    'username': 'user123',
    'password': '1234'
}

un = input("Enter username: ")
ps = input("Enter password: ")

if un == user['username'] and ps == user['password']:
    print("Login Successfully Completed!")
else:
    print("Login Failed")