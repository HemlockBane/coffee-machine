class CoffeeMachine:
    espresso_supplies = [250, 0, 16, 1, 4]
    latte_supplies = [350, 75, 20, 1, 7]
    cappucino_supplies = [200, 100, 12, 1, 6]
    all_supplies = [espresso_supplies, latte_supplies, cappucino_supplies]

    def __init__(self):
        self.water_available = 400
        self.milk_available = 540
        self.coffee_beans_available = 120
        self.disposable_cups_available = 9
        self.money_available = 550
        self.is_running = True

    def get_available_supplies(self):
        return [self.water_available, self.milk_available, self.coffee_beans_available, self.disposable_cups_available, self.money_available]

    def fill_supplies(self):
        self.water_available = self.water_available + \
            int(input("Write how many ml of water do you want to add:"))
        self.milk_available = self.milk_available + \
            int(input("Write how many ml of milk do you want to add:"))
        self.coffee_beans_available = self.coffee_beans_available + \
            int(input("Write how many grams of coffee beans do you want to add:"))
        self.disposable_cups_available = self.disposable_cups_available + \
            int(input("Write how many disposable cups do you want to add:"))
        print("")

    def make_coffee_choice(self, water, milk, coffee_beans, disposable_cups, money):
        self.water_available = self.water_available - water
        self.milk_available = self.milk_available - milk
        self.coffee_beans_available = self.coffee_beans_available - coffee_beans
        self.disposable_cups_available = self.disposable_cups_available - disposable_cups
        self.money_available = self.money_available + money

    def has_enough_supplies(self, coffee_choice: int):
        required_supplies = CoffeeMachine.all_supplies[coffee_choice - 1]
        available_supplies = self.get_available_supplies()
        names_of_supplies = ["water", "milk",
                             "coffee beans", "disposable cups"]
        has_enough_supplies = True

        supplies_num = len(required_supplies)
        for idx in range(supplies_num - 1):
            difference = available_supplies[idx] - required_supplies[idx]
            if difference < 0:
                print(f"Sorry, not enough {names_of_supplies[idx]}")
                has_enough_supplies = False
                break

        if has_enough_supplies:
            print("I have enough resources, making you a coffee!")

        return has_enough_supplies

    def buy_coffee(self):
        coffee_choice = input(
            "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino:")
        if coffee_choice == "1":  # espresso
            if self.has_enough_supplies(int(coffee_choice)):
                self.make_coffee_choice(250, 0, 16, 1, 4)
        elif coffee_choice == "2":  # latte
            if self.has_enough_supplies(int(coffee_choice)):
                self.make_coffee_choice(350, 75, 20, 1, 7)
        elif coffee_choice == "3":  # cappucino
            if self.has_enough_supplies(int(coffee_choice)):
                self.make_coffee_choice(200, 100, 12, 1, 6)

    print("")

    def print_remaining_supplies(self):
        print("The coffee machine has:")
        print(f"{self.water_available} of water")
        print(f"{self.milk_available} of milk")
        print(f"{self.coffee_beans_available} of coffee beans")
        print(f"{self.disposable_cups_available} of disposable cups")
        print(f"${self.money_available} of money", end="\n\n")

    def take_money(self):
        print(f"I gave you ${self.money_available}", end="\n\n")
        self.money_available = 0

    def handle_option(self, user_option):
        if user_option == "exit":
            self.is_running = False
            return
        elif user_option == "buy":
            self.buy_coffee()
        elif user_option == "fill":
            self.fill_supplies()
        elif user_option == "take":
            self.take_money()
        elif user_option == "remaining":
            self.print_remaining_supplies()

    def run_coffee_machine(self):
        while self.is_running:
            user_option = input(
                "Write action (buy, fill, take, remaining, exit):")
            print("")
            self.handle_option(user_option)


coffee_machine = CoffeeMachine()
coffee_machine.run_coffee_machine()
