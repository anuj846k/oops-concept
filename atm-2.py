class ATM:
    # Static Variable
    __counter = 1

    def __init__(self):

        # Instance variables
        self.__pin = ""
        # py change the name internally into _ATM__pin ( name mangling)  It’s to avoid accidental conflicts and misuse.
        self.__balance = 0
        # py change the name internally into _ATM__balance

        self.serialno = ATM.counter
        ATM.__counter = ATM.__counter + 1

        self.menu()

    @staticmethod
    # They dont need objects to run as they are static methods
    def get_counter():
        return ATM.__counter

    @staticmethod
    def set_counter(new):
        if type(new) == int:
            ATM.__counter = new
        else:
            print("nowt allowed")

    def menu(self):
        while True:

            user_input = input(
                """
                            Hello how would you like to proceed
                            1. Enter 1 to create pin
                            2. Enter 2 to deposit 
                            3. Enter 3 to withdraw
                            4. Enter 4 to check balance
                            5. Enter 5 to exit
                            
                            
                            """
            )

            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            else:
                print("BYE")
                break

    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("PIN SET SUCCESSFULLY!!!!")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            self.__balance = self.__balance + amount
            print("DEPOSIT SUCCESS!!")
        else:
            print("INVALID PIN")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("operation successful")
            else:
                print("Insufficient funds!!!")
        else:
            print("Invalid Pin")

    def check_balance(self):
        temp = input("Enter the pin: ")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid pin")


atm = ATM()
print(atm.serialno)
