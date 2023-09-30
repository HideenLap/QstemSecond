from random import randint


def user_input():
    command = input("Enter your command: ")
    return command


def account_number_generate():
    return randint(5000, 50000)


def create_new_account(accounts):
    print('You are creating a new account')
    name = input("Enter your name: ")
    account_number = account_number_generate()
    password = input("Enter your new password: ")
    account = {
        "User_name": name,
        "Account_number": account_number,
        "Password": password,
        "balance": 0
    }
    accounts[account_number] = account
    print('New account created')
    print(
        f'Your account details. Your name = {account["User_name"]}, your account number = {account["Account_number"]}, and your balance = {account["balance"]}')


def deposit_funds(accounts):
    print("To deposit money into your account, we need your account number.")
    acc_number = int(input("Enter your account number: "))
    if acc_number in accounts:
        account = accounts[acc_number]
        balance = account["balance"]
        print(f'Your current balance is {balance}')
        print('You have 2 options')
        print('1: Deposit money')
        print('2: Cancel this operation')
        command = int(user_input())
        if command == 1:
            amount_of_money = int(input("Enter how much you want to deposit: "))
            if amount_of_money <= 0:
                print("Error sum of money cant negative or zero")
            else:
                account["balance"] += amount_of_money
                print(f'New balance: {account["balance"]}')
        elif command == 2:
            print('You canceled this operation')
        else:
            print("Wrong operation code")
    else:
        print("Account not found.")


def withdraw_funds(accounts):
    print('You want to withdraw your funds')
    print('You will have 5 tries')
    counts = 5
    while counts != 0:
        acc_number = int(input('First we enter your account number: '))
        if acc_number in accounts:
            passcode = input("Now enter you password: ")
            if passcode == accounts[acc_number]["Password"]:
                print(f'Your current balance is {accounts[acc_number]["balance"]}')
                withdraw = int(input("How much you want to withdraw: "))
                if withdraw > accounts[acc_number]["balance"]:
                    print("You dont have enough money")
                else:
                    accounts[acc_number]["balance"] -= withdraw
                    print(f'Now you have {accounts[acc_number]["balance"]}')
            else:
                print("Wrong password")
                counts -= 1
                print(f"U have {counts} tries left")
        else:
            print("Wrong account number")
            counts -= 1
            print(f"U have {counts} tries left")


def check_balance(accounts):
    print('You want to check your balance')
    print('You will have 5 tries')

    max_attempts = 5
    for attempt in range(max_attempts, 0, -1):
        acc_number = int(input("Enter your account number: "))
        if acc_number in accounts:
            password = input("Enter your password: ")
            if password == accounts[acc_number]["Password"]:
                print(f'You have {accounts[acc_number]["balance"]}')
                break
            else:
                print('Wrong password')
        else:
            print('Wrong account number')

        if attempt > 1:
            print(f'You have {attempt - 1} tries left')
        else:
            print('No more attempts. Exiting...')


def update_info(accounts):
    print('You chose to update info')
    max_attempts = 5
    for attempt in range(max_attempts, 0, -1):
        acc_number = int(input("Enter your account number: "))
        if acc_number in accounts:
            password = input("Enter your password: ")
            if password == accounts[acc_number]["Password"]:
                print('You have 3 options')
                print('1: Update your password')
                print('2: Generate a new account number')
                print('3: Cancel this operation')
                command = input()
                if command == "1":
                    new_password = input("Enter a new password: ")
                    if new_password == accounts[acc_number]["Password"]:
                        print("New password can't be the same as the old one")
                    else:
                        accounts[acc_number]["Password"] = new_password
                        break
                elif command == "2":
                    new_account_number = account_number_generate()
                    accounts[new_account_number] = accounts.pop(acc_number)
                    print(f'Your new account number is {new_account_number}')
                    break
                elif command == "3":
                    print('You canceled this operation')
                    break
            else:
                print("Wrong password")
        else:
            print("Wrong account number")


def menu():
    print('Hello user')
    flag = True
    accounts = {}
    while flag:
        print('You have 6 options')
        print('1: Create a new account')
        print('2: Deposit funds')
        print('3: Withdraw funds')
        print('4: Check balance')
        print('5: Update your account data')
        print('6: Exit')
        command = user_input()
        if command == "1":
            create_new_account(accounts)
        elif command == "2":
            deposit_funds(accounts)
        elif command == "3":
            withdraw_funds(accounts)
        elif command == "4":
            check_balance(accounts)
        elif command == "5":
            update_info(accounts)
        elif command == "6":
            print("Goodbye")
            flag = False
        else:
            print("Error, please try again")


def main():
    menu()


if __name__ == '__main__':
    main()
