import random

def create_random_number():
    number = random.randint(1000, 5000)
    return number

def clear():
    print('\n' * 10)

def verify(account):
    if account == 0:
        clear()
        print('WARNING: No account found in our system. Please create one\n')


account_value = 0
history = list()


while True:
    n = str(input('Welcome Bank J&J:\n1 - Create Account\n2 - Deposit\n3 - Withdraw\n4 - Balance\n5 - History\n6 - Leave\n>> '))

    options = [1,2,3,4,5,6]

    try:
        n = int(n) # Verify

        if n == 1:
            if account_value == 0:
                account_value = 1
                balance = 0
                number = create_random_number()
                clear()
                print(f'Account created successfully. Your account id is {number}\n')
            else:
                clear()
                print(f'This account already exists! Your id is {number}\n')    
        
        elif n == 2:
            if account_value != 0:
                clear()
                dolar = float(input('How much do you want to deposit into your account? '))
                balance += dolar
                history.append(f'{balance} deposit in your account')
            else:
                verify(account_value)
        
        elif n == 3:
            if account_value != 0:
                clear()
                dolar = float(input('How much do you want to withdraw from your account? '))
                if dolar > balance:
                    print('You dont have enough funds\n')
                else:
                    balance -= dolar
                    history.append(f'{dolar} withdraw in your account\n')
            else:
                verify(account_value)
        
        elif n == 4:
            if account_value != 0:
                clear()
                print(f'${balance}')
            else:
                verify(account_value)

        elif n == 5:
            if account_value != 0:
                for i in history:
                    print(i)
            else:
                verify(account_value)
        elif n == 6:
            break

        else:
            clear()
            print('Please answer [1-6]! Try again!')

    except ValueError:
        clear()
        print('ValueError! Try again!')
        

