class Puppy:
    n_puppies = 0  # number of created puppies

    # define __new__
    def __new__(cls):
        if cls.n_puppies < 10:
            cls.n_puppies += 1
            return object.__new__(cls)


for i in range(12):
    puppy = Puppy()
    print(puppy)

# Create a class PiggyBank with 2 instance variables: dollars & cents
# Initialise the instance variables in the constructor
# Create a method called add_money that accepts 2 parameters: deposit_dollars $ deposit_cents
#  Use deposit_dollars and deposit_cents to increase the value of dollars and cents respectively
# NB: Cents cannot be higher than 99. 100 cents == 1 dollar


class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        total_cents = self.cents + deposit_cents
        carry_over, self.cents = str(total_cents/100).split(".")

        self.dollars = self.dollars + deposit_dollars + int(carry_over)

    def to_string(self):
        print(f"dollars: {self.dollars}, cents: {self.cents}")


piggy_bank = PiggyBank(1, 1)
piggy_bank.add_money(500, 500)
piggy_bank.to_string()