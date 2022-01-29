class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.account = account
     

    def check_balance(self):
        print("Your balance is :")
        print("coins = 100")
        print("notes = 200")

    def withdrawlc(self,coins):
        new_amount = 100 - coins
        print("You have withdrawn amount "+str(coins) + ". Your remaining balance is "+ str(new_amount))

    def withdrawln(self,notes):
        new_amount = 200 - notes
        print("You have withdrawn amount "+str(notes) + ". Your remaining balance is "+ str(new_amount))  


def main():
    Account = input("Enter your acount number: ")
    Card_number = input("Enter your card number: ")
    pin_number  = input("Enter your pin number: ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance   2.Withdraw")
    activity = int(input("Enter activity number: "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("Withdraw coins")
        print("Withdraw notes")

        choose = int(input("1.Coins  2.Notes: "))
        if (choose == 1):
           coins = int(input("Enter amount: "))
           new_user.withdrawlc(coins)
        if (choose == 2):
           notes = int(input("Enter amount: "))
           new_user.withdrawln(notes)

if __name__ == "__main__":
    main()