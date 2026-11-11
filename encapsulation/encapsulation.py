# Encapsulation
#
# Python has no real "private" keyword. Instead it uses naming conventions:
#   name     -> public: anyone can read and modify it
#   _name    -> protected: "internal use", accessible but should not be touched from outside
#   __name   -> private: Python renames it (name mangling) to make outside access harder

class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0) -> None:
        self.owner: str = owner                  # public
        self._bank: str = "Python Bank"          # protected
        self.__balance: float = initial_balance  # private

    # Read-only property: there is a getter but no setter
    @property
    def balance(self) -> float:
        return self.__balance

    # The only way to change the balance is through methods that validate the input
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("The deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("The withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.__name: str = name
        self.__salary: float = salary

    # Getter
    @property
    def name(self) -> str:
        return self.__name

    # Setter with validation
    @name.setter
    def name(self, value: str) -> None:
        if len(value.strip()) < 2:
            print("The name must have at least 2 characters.")
            return
        self.__name = value

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, value: float) -> None:
        if value < 0:
            print("The salary cannot be negative.")
            return
        self.__salary = value


# --- BankAccount ---
account = BankAccount("Ana", 100)

print(f"Owner: {account.owner}")        # public: free access
print(f"Bank: {account._bank}")         # protected: works, but it's a convention not to do it
print(f"Balance: {account.balance}")    # private, read through the property

account.deposit(50)
account.withdraw(500)  # rejected: insufficient funds
account.deposit(-10)   # rejected: invalid amount

# account.balance = 1_000_000   # AttributeError: the property has no setter
# print(account.__balance)      # AttributeError: private attribute

# Name mangling: Python stores __balance as _BankAccount__balance.
# It is still reachable, which shows that "private" in Python is a convention, not a lock.
print(f"Mangled name: {account._BankAccount__balance}")

# --- Employee ---
employee = Employee("Luis", 2500)

employee.name = "L"       # rejected by the setter
employee.salary = -100    # rejected by the setter
employee.salary = 3000    # accepted

print(f"Employee: {employee.name}, Salary: {employee.salary}")