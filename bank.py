class Bank_Account:
   
    def __init__(self, account_name):
        self.account_name = account_name
        self.deposits=[]   #
        self.withdrawals=[]#
        self.loan_balance=0 #
       
    # def deposit(self, amount):
    #     self.balances += amount
    #     return f"You have deposited {amount} your new balance is {self.balances}"

#     def withdraw(self,amount):
#         if self.balances >= amount:
#             self.balances -= amount
#             return f"you have withdrawn {amount}your new balance is{self.balances}"
#         else:
#             f"your balance is {self.balances} you cannot withdraw this {amount}"
    
#     def get_account_number(self):
#         return self.account_number
   
#     def get_balance(self):
#         return self.balances

    def check_balance(self):
        balance=sum(self.deposits)-sum(self.withdrawals)-(self.loan_balance)
        return f"Confirmed .Your account balance is:{balance}"

    def deposit(self,amount):
        self.loan_balance+=amount
        self.deposits.append({"transaction_type":"deposit","amount":amount})

    def withdraw(self,amount):
        if self.loan_balance >=amount:
            self.loan_balance-=amount
            self.withdrawals.append({"transaction_type":"withdrawal","amount":amount})
        else:
            print(f"You have insufficient funds to withdraw :{amount}Your account balance is:{self.loan_balance} ")

    def print_statement(self):
        transaction_made= self.deposits + self.withdrawals
        for transactions in transaction_made:
            if transactions["type"]== "deposit":
                print"deposit-",transactions["amount"]
            else:
                print("Withdrawal-",transaction["amount"])


    def borrow_loan(self,amount):
        if self.loan_balance>0:
            return f"You have an outstanding loan "
        elif amount < 100:
            return f"Loan amount must be atleast 100"
        elif len (self.deposits)<10:
            return f"You must have at least 10 deposits to borrow"
        else:
            total_deposits=sum(transaction_made["amount"]for transaction_made in self.deposits)
            if amount > total_deposits / 3:
                return f"Amount required is more than 1/3 of your total deposits"
            else:
                self.loan_balance += amount
                self.balance += amount
                return "Loan request was successful"

    def repay_loan(self,amount):
        if amount > self.loan_balance:
            self.balance +=(amount-self.loan_balance)
            self.loan_balance=0
            print(f"Loan fully repaid")
        else:
            self.loan_balance-=amount
            print(f"Loan partially repaid")


    def transfer(self,amount,account):
        if amount <=self.check_balance():
            self.withdrawal(amount)
            account.deposit(amount)
            print(f"Transfer successful")
        else:
            print(f"Transfer failed.Insufficient balance.")
            

                



