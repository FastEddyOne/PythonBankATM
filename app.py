# write a Bank ATM program. Your ATM should allow the user to:

# Check (B)alance
# Make a (D)eposit
# (W)ithdraw money
# (Q)uit
# You should create a function for each of the first three options above.

# The program needs to keep running until the user decides to quit the program.


def check_balance(balance):
    print(f"Your current balance is ${balance}")

def make_deposit(balance):
    deposit = input("How much would you like to deposit? ")
    balance = balance + int(deposit)
    print(f"Your new balance is ${balance}")
    return balance

def make_withdrawal(balance):
    withdrawal = input("How much would you like to withdraw? ")
    balance = balance - int(withdrawal)
    print(f"Your new balance is ${balance}")
    return balance

def main():
    balance = 0
    while True:
        user_input = input("What would you like to do? (B)alance, (D)eposit, (W)ithdraw, (Q)uit: ")
        if user_input.upper() == "B":
            check_balance(balance)
        elif user_input.upper() == "D":
            balance = make_deposit(balance)
        elif user_input.upper() == "W":
            balance = make_withdrawal(balance)
        elif user_input.upper() == "Q":
            print("Thanks!")
            break
        else:
            print("Invalid input. Please try again.")

main()