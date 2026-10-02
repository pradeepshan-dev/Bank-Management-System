class Account:

    def __init__(self,account_number,name,balance,set_pin):

        self.account_number = account_number

        self.account_holder_name= name

        self.balance = balance

        self.secret_pin = set_pin

    def deposit(self,amount):

        if amount > 0:

            self.balance += amount

            return f" ₹{amount} Credited to Your Account"

        else:

            return "Invalid Amount"

    def withdraw(self,amount):

        if amount > self.balance :

            print("Insufficient Balance")

            return f"Balance : ₹ {self.balance}"

        elif amount <= 0:

            return "Invalid Amount"

        else:

            self.balance -= amount

            return f"-₹{amount} Debited from Your Account"

    def show(self):

        return f" Balance : ₹ {self.balance}"

class Bank:

    def __init__(self):

        self.accounts = []

    def create_account(self):


        print("Welcome To Our Bank 🏦")

        print()

        try:

            account_number = int(input("Enter Account Number : "))

            for number in self.accounts:

                if account_number == number.account_number:

                    return "❌ Account Already Exist Create New Account Number"

        except ValueError:

            return "❌ Enter Number Only"

        name = input("Enter Your Name : ")

        try:

            balance = int(input("Enter Your balance : "))

            if balance <= 0:

                print("❌ Invalid balance")

                return "Balance must above 100 💸"

        except ValueError:

            return "❌ Enter Numbers Only"
        
        try:

            set_pin = int(input("Set 4 Digit Pin Number : "))

            if len(str(set_pin)) != 4:

                return "❌ Set 4 Digit Pin Number"

            else:

                print("✅ Pin Number Successfully Created")

        except ValueError:

            return "❌ Enter Numbers Only"
        
        else:

            print("✅ Account Created Successfully")

        acc = Account(account_number,name,balance,set_pin)

        self.accounts.append(acc)

        return self.accounts

    def search_account(self):

        try:

            search_account_number = int(input("Enter Account Number Search : "))

        except ValueError:

            return "❌ Enter Numbers Only"

        for number in self.accounts:

            if number.account_number == search_account_number:

                return number.__dict__

        else:

            return "❌ Account Number Not Found"

    def deposit(self):

        try:

            deposit_amount_by_accountNumber = int(input("Enter Account Number to Deposit Money : "))

        except:

            return "❌ Invalid Account"

        for number in self.accounts:

            if number.account_number == deposit_amount_by_accountNumber:

                try:

                    enter_secret_pin = int(input("Enter Your 4 Digit Secret Number : "))

                    if number.secret_pin == enter_secret_pin:

                        try:

                            amount = int(input("Enter Money to Deposit : "))

                            if amount <= 0:

                                return "❌ Invalid Amount"

                            else:

                                print(f"Balance :  ₹{number.balance + amount}")

                                number.balance += amount

                                return f" ₹ {amount} Amount Added Successfully ✅"

                        except ValueError:

                            return "❌ Enter Number Only"

                    else:

                        return "❌ Wrong Pin Number"

                except ValueError:

                    return "❌ Enter Number Only"

        else:

            return "❌ Account Number Not Found"

    def withdraw(self):

        try:

            withdraw_amount_by_Account_number = int(input("Enter Account Number to Withdraw Amount : "))

        except ValueError:

            return "❌ Enter Numbers Only"

        for number in self.accounts:

            if withdraw_amount_by_Account_number == number.account_number:

                try:

                    enter_secret_pin = int(input("Enter 4 Digit Secret Pin Number : "))

                    if number.secret_pin == enter_secret_pin:

                        try:

                            withdraw_amount = int(input("Enter Amount to Withdraw : "))

                            if withdraw_amount <= 0:

                                return "❌ Invalid Amount"

                            else:

                                if number.balance >= withdraw_amount:

                                    print(f"Balance : ₹{number.balance - withdraw_amount}")

                                    number.balance -= withdraw_amount

                                    return f" -₹{withdraw_amount} Withdraw Successfully ✅"

                                else:

                                    return "❌ Invalid Balance"

                        except ValueError:

                            return "❌ Enter Numbers Only"

                    else:

                        return "❌ Wrong Pin Number"
                                
                except ValueError:

                    return "❌ Enter Numbers Only"

        else:

            return "❌ Account Not Found"

    def check_balance(self):

        try:

            enter_account_number_tocheckbalance = int(input("Enter the Account Number to Check Balance : "))

        except:

            return "Enter Numbers Only"

        for number in self.accounts:

            if number.account_number == enter_account_number_tocheckbalance:

                try:

                    enter_secret_pin = int(input("Enter Your 4 Digit Pin Number : "))

                    if number.secret_pin == enter_secret_pin:

                        return f"✅ Balance : {number.balance}"

                    else:

                        return "❌ Wrong Pin Number"

                except ValueError:

                    return "❌ Enter Numbers Only"

        else:

            return "❌ Invalid Account"

    def delete_account(self):

        try:

            enter_account_number_todeleteaccount = int(input("Enter Account Number to Delete the Account : "))

        except:

            return "❌ Enter Numbers Only"

        for number in self.accounts:

            if number.account_number == enter_account_number_todeleteaccount:

                try:

                    enter_secret_pin = int(input("Enter 4 Digit Secret Pin Number : "))

                    if number.secret_pin == enter_secret_pin:

                        print("Account Number : ",number.account_number)

                        print("Account Holder : ",number.account_holder_name)

                        print("Balance : ",number.balance)

                        print("Are You Sure Of Deleting the Account Yes/No ❌")

                        user_want = input("Enter Yes/No for Account Deletion : ")

                        if user_want.lower() == "yes":

                            self.accounts.remove(number)

                            return "Account Deleted Successfully ✅"

                        elif user_want.lower() == "no":

                            return "Account Deletion Cancelled ❌"

                        else:

                            return "Enter Yes/No Only"

                    else:

                        return "❌ Wrong Pin Number"

                except ValueError:

                    return "❌ Enter Numbers Only"

        else:

            return "❌ Invalid Account"

    def showall_account(self):

        if len(self.accounts) == 0:

            return "Create a new Account to Join Our Bank 🏦"

        for number in self.accounts:

            print("=========================")

            print("Account Number : ",number.account_number)

            print("Name : ",number.account_holder_name)

            print("Balance : ",number.balance)

            print("=========================")

        else:

            return f"Number 1 Bank in India is APPP Bank 🏦"

    def update_account(self):

        try:

            enter_accountnumber_updatename = int(input("Enter Account Number to Update Name : "))

            for number in self.accounts:

                if number.account_number == enter_accountnumber_updatename:

                    try:

                        enter_secret_pin = int(input("Enter Your 4 Digit Secret Number : "))

                        if enter_secret_pin == number.secret_pin:

                            print()

                            print("1. Update Name")

                            print("2. Update Pin Number ")

                            print("3. Back")

                            print()

                            try:

                                upadate_value_id = int(input("Enter Values From Display To Update : "))

                                if upadate_value_id == 1:

                                    print("Name : ", number.account_holder_name)

                                    update_name = input("Enter New Name to Update : ")

                                    number.account_holder_name = update_name

                                    return "✅ Name Updated Successfully"

                                elif upadate_value_id == 2:

                                    try:

                                        upadate_pin = int(input("Enter a New Pin to Update : "))

                                        number.secret_pin = upadate_pin

                                        return "✅ Pin Updated Successfully"

                                    except ValueError:

                                        return "❌ Enter Numbers Only"

                                elif upadate_value_id == 3:

                                    return "Thankyou For Coming Have a Great Day 🤗"

                                else:

                                    return "❌ Enter Numbers From Display"

                            except ValueError:

                                return "❌ Enter Numbers Only"

                        else:

                            return "❌ Wrong Pin Number"

                    except ValueError:

                        return "❌ Enter Numbers Only"

            else:

                return "❌ Invalid Account"
            
        except ValueError:

            return "❌ Enter Number Only"

    def transfer_amount(self):

        try:

            enter_senderaccount_number = int(input("Enter Sender Account Number : "))

        except ValueError:

            return "❌ Enter Number Only"

        for number in self.accounts:

            if number.account_number == enter_senderaccount_number:

                sender_account = number

                try:

                    enter_secret_pin = int(input("Enter Your 4 Digit Secret Number : "))

                    if enter_secret_pin == sender_account.secret_pin:

                        try:

                            enter_receiver_account = int(input("Enter Receiver Account Number : "))


                        except:

                            return "❌ Enter Number Only"
                        
                        for numbers in self.accounts:

                            if enter_receiver_account == numbers.account_number:

                                receiver_account = numbers

                                if enter_senderaccount_number == enter_receiver_account:

                                    return "❌ Cannot Transfer Money to Same Account"

                                try:

                                    enter_amount_tosend = int(input("Enter Amount to Send : "))

                                    if enter_amount_tosend <= sender_account.balance:

                                        sender_account.balance -= enter_amount_tosend

                                        receiver_account.balance += enter_amount_tosend

                                        return "✅ Amount Transfered Successfully"

                                    else:

                                        return "❌ Invalid Balance"

                                except:

                                    return "❌ Enter Number Only"

                        else:

                            return "❌ Invalid Account"
                                
                    else:

                        return "❌ Wrong Pin Number"

                except:

                    return "❌ Enter Number Only"

        else:

            return "❌ Invalid Accoun / Account Not Found"
        
bank = Bank()

while True:

    print()

    print("=====================================================================")

    print()

    print(" 🏦 💰 Welcome To APPP Bank (Arun,Priya,Preethi,Pradeep) 💸 🤗 ")

    print()

    print("=====================================================================")

    print()

    print("1. Create New Accout")

    print("2. Search Account")

    print("3. Deposit Amount")

    print("4. Withdraw Amount")

    print("5. Check Balance")

    print("6. Delete Account")

    print("7. Show All Account")

    print("8. Update Account")

    print("9. Transfer Money")

    print("10. Exist")

    print()

    try:

        user_choice = int(input("Enter Numbers from display : "))

    except ValueError:

        print("❌ Enter Numbers Only")

    if user_choice == 1:

        print(bank.create_account())

    elif user_choice == 2:

        print(bank.search_account())

    elif user_choice == 3:

        print(bank.deposit())

    elif user_choice == 4:

        print(bank.withdraw())

    elif user_choice == 5:

        print(bank.check_balance())

    elif user_choice == 6:

        print(bank.delete_account())

    elif user_choice == 7:

        print(bank.showall_account())

    elif user_choice == 8:

        print(bank.update_account())

    elif user_choice == 9:

        print(bank.transfer_amount())

    elif user_choice == 10:

        break

    else:

        print("Enter Numbers from display ")

        print()