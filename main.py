# Global constant
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ENTER_NUMBER_MSG = 'Please enter a number'


def deposit():
    while True:
        amount = input('What would you like to deposite? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print(ENTER_NUMBER_MSG)
    return amount


def get_bet():
    while True:
        amount = input('What would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print('Enter a valid number')
        else:
            print(ENTER_NUMBER_MSG)
    return amount


def get_number_of_lines():
    while True:
        lines = input(f'Enter the number of lines to bet on (1-{MAX_LINES})?')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines')
        else:
            print(ENTER_NUMBER_MSG)
    return lines


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"Sorry, you don't have enough credit, current balance: ${balance}")
        else:
            break

    print(f"You're betting ${bet} on {lines} lines. Total bet: ${total_bet}")


main()
