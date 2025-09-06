#Inheritance in Python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
# Creating instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

#Polymorphism in Python
def animal_sound(animal):
    print(animal.speak())
animal_sound(dog)  # Output: Buddy says Woof!
animal_sound(cat)  # Output: Whiskers says Meow!

#Encapsulation in Python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds or invalid withdrawal amount")

    def get_balance(self):
        return self.__balance
    
# Creating a BankAccount instance
account = BankAccount("Alice", 1000)
account.deposit(500)          # Output: Deposited: 500
account.withdraw(200)         # Output: Withdrew: 200
print(account.get_balance())  # Output: 1300
# Trying to access the private attribute directly will raise an AttributeError
# print(account.__balance)  # Uncommenting this line will cause an error
# print(account.__balance)  # Uncommenting this line will cause an error
# Instead, use the provided method to access the balance
print(account.get_balance())  # Output: 1300




    
