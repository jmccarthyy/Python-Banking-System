#Banking system
import itertools

class Customer():
    #This is to give a customer a unique id
    newid = itertools.count()
    #Default value of customer, need to pass in each except balance
    def __init__(self, firstName, lastName, balance = 0):
        self.customerNumber = next(self.newid)
        self.firstName = firstName
        self.lastName = lastName
        self.balance = balance

    #functions for each action
    def showAccountDetails(self):
        return f"({self.customerNumber}) {self.firstName} {self.lastName} - Balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print(f"New balance: {self.balance}")

    def withdraw(self, amount):
        confirm = input("Are you sure? (y/n)")
        if confirm.lower() == "y":
                self.balance -= amount
        else:
            print("You decided not to withdraw any money.")
                
    def deleteAccount(self):
        customers.remove(self)

#Pre-existing customers
customer1 = Customer("Luke", "McCarthy", 100)
customer2 = Customer("Jake", "McCarthy", 10)
customer3 = Customer("Ben", "Chalmers", 25)
customer4 = Customer("Gaz", "Beadle", 10000)
customer5 = Customer("Victoria", "Kelly", 3500)
customer6 = Customer("Rachel", "Patterson", 1200)
customer7 = Customer("Terry", "Wogan", 4567)


#Customer Database
customers = [
    customer1,
    customer2,
    customer3,
    customer4,
    customer5,
    customer6,
    customer7,
    
]

#main function
def main():
    run = True
    customer = None
    while(run):
        while(customer == None):
            choice = input("Enter account number or type new to create new account: ")
            if choice.lower() == "new":
                firstName = input("Enter first name: ")
                lastName = input("Enter last name: ")
                balance = int(input("Enter starting balance: "))
                customer = Customer(firstName, lastName, balance)
                customers.append(customer)
                
            else:
                for cust in customers:
                    if int(choice) == cust.customerNumber:
                        customer = cust
                        print("Hello, " + customer.firstName)
                        
                if customer == None:
                    print("Customer not found")

        print("What would you like to do now? ")
        choice = input("Show Details (s) | Deposit (d) | Withdraw (w) | Delete Acc (delete) | Quit (q) ")
        if choice.lower() == "s":
            print(customer.showAccountDetails())
        if choice.lower() == "d":
            value = int(input("Enter an amount: "))
            customer.deposit(value)
        if choice.lower() == "w":
            value = int(input("Enter an amount: "))
            customer.withdraw(value)
        if choice.lower() == "delete":
            confirm = input("Are you sure? (y/n)")
            if confirm.lower() == "y":
                customer.deleteAccount()
                print("Account deleted")
                customer = None
            else:
                print("You decided not to delete your account")
            
        if choice.lower() == "q":
            print("Terminating program. Goodbye.")
            run = False
            
main()
