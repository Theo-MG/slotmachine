def deposit():
    while True:
        amount = input('What would yyou like to deposite? $')
        if amount.isdigit():
            amount = int(amount)