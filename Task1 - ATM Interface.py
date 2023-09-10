from datetime import *
import time
import os
current_balance = 234000

def tanshistory():
    print("******************Transaction History******************")
    print("12-May-2023 12:12:30 IST  RS. 1000  Debit")
    print("16-August-2023 12:12:30 IST  RS. 5000  Debit")
    print("12-September-2023 12:12:30 IST  RS. 100   Credit")
    quit()


def withdraw():
    global current_balance
    print("********************Withdraw Money*********************")
    withdraw_amount = int(input("Enter the Amount: "))
    if withdraw_amount <= current_balance:
        current_balance -= withdraw_amount
        print("Rs. ", withdraw_amount, " withdrawn successfully!")
        print("Your current balance is: Rs.", current_balance)
        quit()
    else:
        print("Entered amount is greater than your current balance!.")


def deposit():
    global current_balance
    print("*********************Deposit Money*********************")
    deposit_amount = int(input("Enter the amount: "))
    if deposit_amount == 0:
        print("Please enter the amount greater than 0.")
    else:
        current_balance += deposit_amount
        print("Amount deposited successfully!")
        print("Your current balance is: Rs.", current_balance)
        quit()


def transfer():
    global current_balance
    print("********************Transfer Money*********************")
    print("Available Balance: Rs. ", current_balance)
    beneficiary_bank = input("Enter beneficiary's bank: ")
    beneficiary_account = int(input("Enter the beneficiary account number: "))
    transfer_amount = int(input("Enter the Amount: "))
    current_balance-=transfer_amount
    if len(str(beneficiary_account))==16:
        print("Amount transferred successfully!")
        print("Your current Balance is: Rs. ",current_balance)
        quit()
    else:
        print("Wrong Account Number Entered!")

def quit():
    print("*******************************************************")
    print("Exiting...")
    exit(0)

while True:
    today_time = time.time()
    print("***************Welcome to Bharat ATM*******************")
    print("Date: ", datetime.fromtimestamp(today_time))
    user_id = input("Enter your credentials- \nUser ID: ")
    pin = input("Pin: ")
    print("*******************************************************")
    print("Logged In Successfully!")
    print("*******************************************************")
    print("Account Type: \n1. Savings \n2. Current ")
    account_type = int(input("Enter (1/2): "))
    print("*******************************************************")
    print("Options: \n1. Withdraw \n2. Deposit \n3. Transfer \n4. Transaction History \n5. Exit")
    option = int(input("Enter (1/2/3/4/5): "))
    print("*******************************************************")
    if option == 1:
        withdraw()
    elif option == 2:
        deposit()
    elif option == 3:
        transfer()
    elif option == 4:
        tanshistory()
    elif option == 5:
        quit()
    else:
        print("Invalid Input Given!")
        cont = input("Do you want to continue? (Y/N): ")
        if cont == 'Y' or cont == 'y':
            continue
        else:
            quit()



